# Regras comuns (todas as equipes)

> Fonte única. Cada workspace recebe uma cópia por link físico (`scripts/sincronizar-regras.ps1`); não edite as cópias.

- Fale em português, de forma direta e curta.
- Fale com as outras equipes pelo nome, nas mensagens de agente para agente do OpenBot: Filtro, Classificador, Retriever, Clarificador, Roteador, Design, Implementation, QA, Review PR. O lead é o Orquestrador.
- Handoff no formato da skill `handoff-entre-equipes` (modelo em `imported/handoff.template.md`): id do item, origem, status `ok|falhou|devolvido`, próxima equipe, prazo, artefatos, premissas, motivo.
- Rastreio no Jira pelas ferramentas MCP. Sem token de API no chat. Se as ferramentas não estiverem na sessão, não improvise: anote "Jira pendente" no handoff e siga.
  - Todo item que a esteira criar fica atribuído ao responsável humano e entra na sprint ativa (descubra pela JQL `sprint in openSprints()`, nunca fixe o nome).
  - Horas são de esforço de trabalho, não o tempo de relógio do agente: estimativa ao criar, worklog ao fechar.
  - Toda tarefa nasce como Subtarefa dentro da História da sua user story. Nunca crie tarefa solta.
- Segredos: variável de ambiente em cada servidor, nunca no repositório, nunca no chat.
- LLM: ordem de provedores, em todas as equipes: Claude (conta de trabalho) → Cursor → Codex → Gemini → Claude (conta pessoal). Desça na lista só se o anterior estiver indisponível ou no limite.
- Merge, force-push e reescrita de histórico só com autorização explícita do responsável humano. Nenhum agente faz merge.
- Não mexer em `.codex/config.toml` nem `.mcp.json` do repositório.
- Onde uma skill antiga disser algo diferente destas regras, valem estas regras.
- Economia de tokens (vale sempre, sem precisar carregar skill): resposta mínima, sem preâmbulo e sem recapitular; não cole arquivo inteiro, aponte caminho + trecho; busque pelo grafo de código antes de varrer a árvore; leia só o trecho necessário (`rg`, `git diff --stat` antes do diff inteiro) e não releia o que já está na conversa; comando com saída longa vai filtrado.
