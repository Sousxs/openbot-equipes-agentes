---
name: busca-por-grafo
description: >-
  Use antes de buscar arquivos ou código no repositório: consultar o grafo de
  código (graphify, code-review-graph) em vez de varrer a árvore.
---
# Busca por grafo

## Quando usar
Antes de `find`/`rg` amplo ou de abrir dezenas de arquivos.

## Passos
1. Se o grafo estiver velho: `graphify update .` e `code-review-graph update --brief`.
2. Consultar `graphify-out/GRAPH_REPORT.md` e o brief do code-review-graph para achar símbolos e impacto.
3. Só então abrir os poucos arquivos apontados.
4. Sem as ferramentas no PATH: avisar o Orquestrador; não fingir busca semântica.
