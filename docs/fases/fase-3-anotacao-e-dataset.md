# Fase 3 · Anotação e dataset

| Estado | Bimestres sugeridos | Atividades do cronograma | Depende de |
|---|---|---|---|
| Planejada | B3–B4 | 5. Anotação de imagens | Fase 2 |

## Objetivo

Transformar as imagens brutas em um dataset anotado, revisado e dividido, pronto para treinar e avaliar o detector.

## Entregas

- [ ] Guia de anotação: definição de cada classe, com exemplos e casos-limite
- [ ] Ferramenta de anotação (Python, Tkinter, OpenCV) funcional e documentada
- [ ] Caixas delimitadoras em formato YOLO para as classes Buraco, Obstáculo, Objeto na Pista e Irregularidade
- [ ] Revisão dupla, pelo autor e pelo orientador, com registro das divergências
- [ ] Divisão treino, validação e teste em 70 : 15 : 15, estratificada por faixa de distância
- [ ] Ficha do dataset: número de imagens e de instâncias por classe, por ambiente, por iluminação e por faixa de distância
- [ ] Amostra anonimizada separada para publicação

## Critérios de aceite

- Todas as imagens do dataset passaram pela revisão dupla.
- A divisão é reprodutível a partir de uma semente fixa.
- Imagens da mesma sessão de coleta e quadros do mesmo trecho de vídeo ficam no mesmo subconjunto, para que o teste não contenha imagens quase idênticas às do treino.

## Riscos

| Risco | Mitigação |
|---|---|
| Fronteira ambígua entre Obstáculo e Objeto na Pista, ou entre Buraco e Irregularidade | Resolver no guia de anotação antes de começar; considerar fusão de classes |
| Classes com poucas instâncias | Verificar a ficha do dataset antes de treinar ([Q4](../04-questoes-em-aberto.md#q4--tamanho-do-dataset)) |
| Vazamento entre treino e teste por quadros consecutivos | Dividir por sessão e por trecho de vídeo, não por imagem |

## Contribuição para o artigo

Tabela de composição do dataset e descrição do protocolo de anotação. A amostra anonimizada apoia a afirmação de reprodutibilidade.

## Relatório de encerramento

_A preencher ao concluir a fase._
