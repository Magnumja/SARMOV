# Fase 0 · Fundação

| Estado | Bimestre sugerido | Atividades do cronograma | Depende de |
|---|---|---|---|
| Em andamento | B1 | — | — |

## Objetivo

Deixar o repositório pronto para receber código e dados de forma reprodutível, e apresentar a proposta de pesquisa a quem chega pelo GitHub.

## Entregas

- [x] README com resumo, método, metas e roteiro
- [x] Área de documentação em `docs/`, com um documento por fase
- [x] Marcos e tarefas de acompanhamento no GitHub
- [ ] Licença do código definida com o orientador
- [ ] `requirements.txt` com versões fixas
- [ ] Estrutura do pacote `sarmov/` criada conforme a [Arquitetura](../02-arquitetura.md#estrutura-de-código-planejada)
- [ ] Função única de fixação de sementes (`PYTHONHASHSEED`, `torch`, `numpy`)
- [ ] Data de início do projeto registrada no [Roteiro](../03-roteiro.md), convertendo os bimestres em datas

## Critérios de aceite

- Uma pessoa sem contato prévio com o projeto consegue criar o ambiente a partir do repositório e executar um comando de verificação sem erro.
- As versões instaladas coincidem com as registradas.

## Riscos

| Risco | Mitigação |
|---|---|
| Dados brutos ou pesos de modelo versionados por engano | `.gitignore` já exclui `data/`, pesos e saídas de treino |
| Dependências sem versão fixa quebram a reprodução meses depois | Fixar versões exatas e registrar a versão do Python |

## Contribuição para o artigo

Sustenta a afirmação de reprodutibilidade: ambiente documentado, sementes fixas e código público.

## Relatório de encerramento

_A preencher ao concluir a fase._
