"""Mede quanto a escolha de modelo por papel e o cache de prompt economizam no OpenBot.

Lê o banco do OpenBot só para leitura (nunca grava) e compara, para os registros do
provedor Claude:
  - real: o custo estimado que o próprio OpenBot gravou (preço de lista, não fatura);
  - tudo em Opus: os mesmos tokens cobrados pela tabela do Opus;
  - sem cache: a entrada lida do cache cobrada como entrada normal, no modelo usado
    (proporção calculada pela tabela e aplicada ao custo real de cada registro).

Preços em US$ por 1M de tokens (tabela de contexto curto que o OpenBot usa). Para registros
em contexto longo o OpenBot cobra mais, então "tudo em Opus" sai conservador.

Uso: python -I medir-economia.py [caminho do openbot.db]
"""
import collections
import json
import os
import sqlite3
import sys

# entrada, entrada em cache, escrita de cache, saída
PRECO = {
    "claude-opus-5-5": (4, 0.2, 8, 20),
    "claude-sonnet-5-5": (2, 0.1, 4, 10),
    "claude-haiku-5-5": (0.1, 0.01, 0.2, 0.5),
}
EQUIPES = (" A", " B", " C", " D")


def custo(t, p):
    return (t["uncachedInput"] * p[0] + t["cachedInput"] * p[1]
            + t["cacheCreation"] * p[2] + t["output"] * p[3]) / 1e6


def papel(nome):
    for s in EQUIPES:
        if nome.endswith(s):
            nome = nome[:-2]
    return nome.split("· ")[-1]


def medir(db):
    con = sqlite3.connect(f"file:{db.replace(os.sep, '/')}?mode=ro", uri=True)
    nomes = {}
    for (j,) in con.execute("select agent_json from projection_agents"):
        a = json.loads(j)
        nomes[a["id"]] = papel(a["name"])
    por_papel = collections.defaultdict(collections.Counter)
    for aid, modelo, tj, est in con.execute(
            "select agent_id, model, tokens_json, estimated_cost_usd "
            "from agent_usage_records where provider = 'claude'"):
        if modelo not in PRECO:
            continue
        t = json.loads(tj)
        p = PRECO[modelo]
        sem_cache = dict(t, uncachedInput=t["uncachedInput"] + t["cachedInput"], cachedInput=0)
        linha = {
            "tokens": sum(t.values()),
            "cache": t["cachedInput"],
            "real": est or 0,
            "tudo_opus": custo(t, PRECO["claude-opus-5-5"]),
            # mesma proporção sem/com cache, aplicada ao custo real do registro
            "sem_cache": (est or 0) * custo(sem_cache, p) / max(custo(t, p), 1e-12),
        }
        for alvo in (nomes.get(aid, "(removido)"), "TOTAL"):
            por_papel[alvo].update(linha)
    periodo = con.execute(
        "select min(occurred_at), max(occurred_at) from agent_usage_records where provider = 'claude'").fetchone()
    return por_papel, periodo


def demo():
    t = {"uncachedInput": 1_000_000, "cachedInput": 0, "cacheCreation": 0, "output": 1_000_000}
    assert custo(t, PRECO["claude-opus-5-5"]) == 24
    assert papel("Mestre · Orquestrador B") == "Orquestrador" and papel("QA") == "QA"


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    demo()
    db = sys.argv[1] if len(sys.argv) > 1 else os.path.expandvars(r"%APPDATA%\OpenBot\openbot.db")
    dados, (ini, fim) = medir(db)
    print(f"Período: {ini[:10]} a {fim[:10]}  (US$, preço de lista)\n")
    print(f"{'papel':16s} {'tokens':>9s} {'cache':>6s} {'real':>9s} {'tudo Opus':>10s} {'sem cache':>10s}")
    for nome, d in sorted(dados.items(), key=lambda x: (x[0] != "TOTAL", -x[1]["real"])):
        print(f"{nome:16s} {d['tokens'] / 1e6:8.0f}M {100 * d['cache'] / max(d['tokens'], 1):5.1f}% "
              f"{d['real']:9.2f} {d['tudo_opus']:10.2f} {d['sem_cache']:10.2f}")
    t = dados["TOTAL"]
    print(f"\nModelo por papel: {t['real']:.0f} em vez de {t['tudo_opus']:.0f} "
          f"({100 * (1 - t['real'] / t['tudo_opus']):.0f}% a menos que tudo em Opus)")
    print(f"Cache de prompt: {t['real']:.0f} em vez de {t['sem_cache']:.0f} "
          f"({100 * (1 - t['real'] / t['sem_cache']):.0f}% a menos que sem cache)")
