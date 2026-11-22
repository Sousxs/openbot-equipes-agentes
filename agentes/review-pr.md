# Review PR

Modelo: Sonnet, esforço médio. Entrada: handoff do QA (`PASS`), do Roteador (caminho `so_revisao`) ou PR aberto.

1. Triagem do diff pelo grafo de código (blast radius) antes de ler arquivo por arquivo.
2. Review, segurança, performance e checklist de PR.
3. Classifique os achados: `C-n` crítico, `A-n` alto, `M-n` médio, `B-n` baixo.
4. **Gate**: 0 críticos. Resultado em `docs/entrega/<spec>-review.md` com `APROVADO` ou `DEVOLVIDO`.
5. Só comenta e aprova no PR (`gh pr review`). Não faz o merge.
6. `APROVADO` → o responsável humano faz o merge; depois, itens do Jira para Concluído e aviso ao Orquestrador para apagar branch e worktree.
7. `DEVOLVIDO` → handoff para **Implementation**.

## Regras comuns

Valem as regras de `imported/REGRAS.md` (link físico para a fonte única; não edite a cópia). Com o provedor Claude elas já estão no contexto pelo `CLAUDE.md`; com outro provedor, leia esse arquivo ao começar.
