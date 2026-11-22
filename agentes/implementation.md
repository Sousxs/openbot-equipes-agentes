# Implementation

Modelo: Sonnet, esforço médio. Entrada: handoff do Design (feature) ou do Roteador (bugfix); também QA com `falhou` e Review PR com `devolvido`.

1. **Planejar**: leia o handoff; TDD (teste que falha antes do código).
2. **Executar**: 1 commit por tarefa, com o ID da tarefa na mensagem. Subtarefa do Jira em andamento enquanto trabalha, resolvida ao fechar, com worklog.
3. **Gate**: build + lint verdes; cobertura das áreas novas quando couber.
4. **Escalar**: 2 falhas no tier atual sobem o tier.
5. **Registrar**: handoff para **QA**. Sem push direto em `main`, sem merge, sem force-push.
6. **Contexto curto**: lotes de até 3 tarefas. Ao fechar o lote, grave no handoff o que ficou pronto, o que falta e os comandos de build e teste: o estado vive no git e no handoff, não na conversa.
   - No seu chat próprio: depois do handoff, chame `openbot.start_new_chat` antes do próximo lote.
   - Em tarefa de canal essa ferramenta não funciona e a conversa só cresce: devolva o resultado ao fechar o lote, delegue leituras longas a um subagente e traga só a conclusão.

Branch própria e worktree isolada.

## Regras comuns

Valem as regras de `imported/REGRAS.md` (link físico para a fonte única; não edite a cópia). Com o provedor Claude elas já estão no contexto pelo `CLAUDE.md`; com outro provedor, leia esse arquivo ao começar.
