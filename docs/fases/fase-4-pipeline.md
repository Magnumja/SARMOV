# Fase 4 · Pipeline

| Estado | Bimestres sugeridos | Atividades do cronograma | Depende de |
|---|---|---|---|
| Planejada | B3–B5 | 6. Implementação do método | Fase 2 (etapa 4a); fase 3 (etapa 4b) |

## Objetivo

Implementar o método proposto: detecção, ponto de referência, estimativa de distância e classificação de risco, integrados em um pipeline que processa imagens e vídeos.

A fase é dividida em três etapas. A primeira não depende do detector e deve começar assim que a calibração estiver aceita.

## Etapa 4a · Geometria

- [ ] Retificação de imagem a partir do arquivo de calibração
- [ ] Seleção do ponto de referência por classe
- [ ] Função de distância pelo modelo *pinhole*, com tratamento de pontos acima do horizonte
- [ ] Testes unitários com casos calculados à mão
- [ ] Validação com caixas anotadas manualmente nas imagens controladas
- [ ] Estimativa de `α` por ajuste em pontos de distância conhecida, comparada à medição por inclinômetro ([Q2](../04-questoes-em-aberto.md#q2--sensibilidade-ao-ângulo-de-inclinação))

**Aceite.** Erro de distância com caixas manuais dentro da meta em toda a faixa de 1 a 15 m (ponto de controle PC2).

## Etapa 4b · Detector

- [ ] Treinamento do YOLOv8n com o protocolo do plano e sementes fixas
- [ ] Registro de cada execução: configuração, versão do código, curvas de treino
- [ ] Seleção do melhor *checkpoint* por mAP de validação
- [ ] Exportação para TFLite e verificação de que o modelo exportado reproduz as detecções do original

**Aceite.** Treino reprodutível a partir de um arquivo de configuração; modelo exportado validado.

## Etapa 4c · Risco e integração

- [ ] Cálculo da distância de frenagem segura e classificação em três níveis
- [ ] Decisão sobre os limiares registrada ([Q1](../04-questoes-em-aberto.md#q1--limiares-de-alerta-e-distância-de-frenagem))
- [ ] Pipeline de ponta a ponta: imagem ou vídeo na entrada; detecções, distâncias e níveis de risco na saída, em arquivo tabular
- [ ] Vídeo anotado com caixas, distâncias e nível de risco, para inspeção visual
- [ ] Suavização temporal do alerta em vídeo, para evitar disparos por detecções isoladas

**Aceite.** O pipeline processa todo o conjunto de teste sem intervenção manual e gera a tabela de saída usada pela fase 5.

## Riscos

| Risco | Mitigação |
|---|---|
| Erro geométrico acima da meta nas maiores distâncias | Antecipar a etapa 4a; estimar `α` pelos dados; restringir a faixa declarada |
| Diferença entre o modelo exportado e o original | Comparar as saídas em um conjunto fixo de imagens |
| Caixas do detector menos justas que as manuais deslocam o ponto de referência | Medir a distância com caixas manuais e com caixas detectadas, separadamente |

## Contribuição para o artigo

Seção de método. A separação entre 4a e 4b permite reportar o erro geométrico isolado do erro de detecção.

## Contribuição para o MVP

O vídeo anotado da etapa 4c é a primeira versão demonstrável do sistema. As funções de geometria e risco são a especificação do que o aplicativo precisa reproduzir.

## Relatório de encerramento

_A preencher ao concluir a fase._
