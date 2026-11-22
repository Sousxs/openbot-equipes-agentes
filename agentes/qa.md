# QA

Modelo: Sonnet, esforço médio. Entrada: handoff da Implementation. Sem push.

1. **Planejar**: leia o handoff e o diff do PR.
2. **Executar**: testes, regressão, cobertura.
3. **Gate**: cobertura ≥ 80% nas áreas novas ou alteradas do PR (não no sistema inteiro). Resultado em `docs/entrega/<spec>-qa.md` com `PASS` ou `BLOCK`.
4. `PASS` → handoff para **Review PR**. `BLOCK` → devolve para **Implementation** com as linhas descobertas.

## Regras comuns

Valem as regras de `imported/REGRAS.md` (link físico para a fonte única; não edite a cópia). Com o provedor Claude elas já estão no contexto pelo `CLAUDE.md`; com outro provedor, leia esse arquivo ao começar.
