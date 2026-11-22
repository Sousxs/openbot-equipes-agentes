# Roteador (passo 5)

Modelo: Haiku, esforço baixo. Spec dos tiers: `config/llm.json`.

1. Confirme o caminho (`direto` | `bugfix` | `feature` | `so_revisao`).
2. Atribua o score de complexidade 1–5 e declare a premissa.
3. Escolha UM provedor e UM tier:
   - score 1–2 → barato; 3 → médio; 4–5 → caro;
   - provedor na ordem das regras comuns; desça só se o anterior estiver indisponível ou no limite.
4. Proibido tier caro em score 1–2 sem duas falhas prévias no tier atual.
5. Enfileire o handoff na primeira equipe do caminho.

Gate: caminho e orçamento confirmados. Na dúvida, prefira barato.

## Regras comuns

Valem as regras de `imported/REGRAS.md` (link físico para a fonte única; não edite a cópia). Com o provedor Claude elas já estão no contexto pelo `CLAUDE.md`; com outro provedor, leia esse arquivo ao começar.
