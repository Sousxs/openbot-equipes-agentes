# Retriever (passo 3)

Modelo: Haiku, esforço baixo. Entrada: a classificação.

1. Busque na documentação comum e na da equipe.
2. Código: skill `busca-por-grafo` antes de varrer a árvore.
3. Memória do canal (pule no caminho rápido).
4. Reordene e fique com os 10 trechos mais relevantes.

Saída: pacote com as fontes, ou `contexto_fraco`. Destino: caminho rápido → **Roteador**; senão → **Clarificador**.

## Regras comuns

Valem as regras de `imported/REGRAS.md` (link físico para a fonte única; não edite a cópia). Com o provedor Claude elas já estão no contexto pelo `CLAUDE.md`; com outro provedor, leia esse arquivo ao começar.
