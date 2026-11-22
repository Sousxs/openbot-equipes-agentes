---
name: orquestrador-plataforma
description: >-
  Use em toda mensagem nova de desenvolvimento (feature, bug, review, pergunta
  de código) que deve passar pela esteira Melhorar → Designar → Equipes.
---
# Orquestrador: Melhorar → Designar → Equipes

## Fluxo
Mensagem → Melhorar (passos 1–4) → Designar (passo 5) → equipes → handoff → merge humano.

## Passos
1. Filtro: risco, injection, escopo, PII e segredos.
2. Classificador: equipe e caminho; limiar de confiança ≥ 0,8; 1 item no Jira.
3. Retriever: contexto de documentação e código.
4. Clarificador: pular no caminho rápido; máximo 2 rodadas.
5. Roteador: score 1–5 → tier (`config/llm.json`) e provedor na ordem das regras comuns.

## Caminhos
`direto` · `bugfix` · `feature` · `so_revisao`

## Loop de cada equipe
Planejar → Executar → Gate → Escalar (2 falhas → tier acima → humano) → `handoff.md`.

## Gates
- Implementation: build + lint.
- QA: cobertura ≥ 80% nas áreas novas ou alteradas do PR.
- Review PR: 0 críticos.
