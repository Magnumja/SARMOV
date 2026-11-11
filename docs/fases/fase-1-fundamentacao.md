# Fase 1 · Fundamentação

| Estado | Bimestres sugeridos | Atividades do cronograma | Depende de |
|---|---|---|---|
| Planejada | B1–B2, com continuidade em B3 | 1. Revisão bibliográfica; 2. Estudo de YOLO | Fase 0 |

## Objetivo

Consolidar a base teórica do projeto e adquirir prática com o YOLOv8 antes de haver dataset próprio.

## Entregas

- [ ] Fichamento das referências do plano, organizado nas três frentes: ADAS preventivo, detecção de risco viário e estimativa monocular de distância
- [ ] Busca complementar por trabalhos que combinem detecção de defeitos viários com estimativa de distância em smartphone, para delimitar a lacuna
- [ ] Referência [10] localizada e conferida ([Q8](../04-questoes-em-aberto.md#q8--referências-a-conferir))
- [ ] Tabela comparativa de trabalhos correlatos: sensor, método de distância, faixa avaliada, erro reportado, plataforma
- [ ] Treino de referência do YOLOv8n em um dataset público, do início à exportação em TFLite
- [ ] Hiperparâmetros padrão da versão instalada conferidos ([Q7](../04-questoes-em-aberto.md#q7--hiperparâmetros-descritos-como-padrão))
- [ ] Rascunho da seção de trabalhos correlatos

## Critérios de aceite

- A tabela comparativa mostra, com números, onde o SARMOV se posiciona em relação aos trabalhos mais próximos.
- O treino de referência roda de ponta a ponta e o modelo exportado executa inferência no smartphone.

## Riscos

| Risco | Mitigação |
|---|---|
| Existir trabalho que já integra as três frentes em smartphone | Descobrir cedo e reposicionar a contribuição para a validação experimental e a análise de erro |
| Metas de erro apoiadas em uma referência não localizada | Substituir por fonte verificável ou derivar a meta da análise de sensibilidade |

## Contribuição para o artigo

Introdução, trabalhos correlatos e a tabela comparativa. O treino de referência fornece também a medição preliminar de desempenho no aparelho.

## Relatório de encerramento

_A preencher ao concluir a fase._
