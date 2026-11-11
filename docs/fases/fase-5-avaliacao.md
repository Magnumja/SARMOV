# Fase 5 · Avaliação

| Estado | Bimestres sugeridos | Atividades do cronograma | Depende de |
|---|---|---|---|
| Planejada | B4–B6 | 7. Avaliação da detecção; 8. Avaliação da distância; 9. Avaliação dos alertas | Fase 4; fase 6 para o desempenho no aparelho |

## Objetivo

Medir o desempenho do sistema nas três dimensões do plano, com intervalos de confiança, e analisar onde e por que ele falha.

## Experimentos

O detalhamento de cada experimento, com a figura ou tabela que ele gera, está no [Plano do artigo](../artigo/plano-do-artigo.md#experimentos).

- [ ] **E1 · Calibração.** Erro de reprojeção RMS e parâmetros obtidos
- [ ] **E2 · Detecção.** Precisão, revocação, F1, IoU e mAP, por classe e no total
- [ ] **E3 · Distância com caixas manuais.** MAE, RMSE e MAPE por distância, isolando o erro geométrico
- [ ] **E4 · Distância de ponta a ponta.** As mesmas métricas com as caixas do detector
- [ ] **E5 · Ponto de referência.** Comparação entre borda superior, borda inferior e ponto médio, por classe
- [ ] **E6 · Sensibilidade.** Erro em função da variação de `α` e de `h`, analítico e medido
- [ ] **E7 · Alerta.** Matriz de confusão do alerta (verdadeiro e falso positivo, verdadeiro e falso negativo), como define o plano; taxas de verdadeiros e falsos positivos
- [ ] **E8 · Desempenho no aparelho.** Tempo por quadro e taxa de quadros
- [ ] **E9 · Falhas.** Casos de baixa iluminação, sombra e oclusão

## Resultados

Preencher conforme os experimentos forem executados. Os valores só entram no README depois de registrados aqui.

| Métrica | Meta | Obtido | IC 95 % | Experimento |
|---|---|---|---|---|
| Erro de reprojeção RMS | < 0,5 px | — | — | E1 |
| Precisão | > 80 % | — | — | E2 |
| Revocação | > 80 % | — | — | E2 |
| mAP | > 0,75 | — | — | E2 |
| MAE de distância | < 1,5 m | — | — | E4 |
| MAPE de distância | < 15 % | — | — | E4 |
| Verdadeiros positivos do alerta | > 85 % | — | — | E7 |
| Falsos positivos do alerta | < 15 % | — | — | E7 |
| Taxa de quadros | ≥ 10 fps | — | — | E8 |

## Critérios de aceite

- Toda tabela e toda figura do artigo é gerada por um script, a partir do dataset e dos parâmetros versionados.
- As métricas principais têm intervalo de confiança de 95 %.
- O erro de distância é reportado por faixa, não apenas agregado.
- Metas não atingidas são reportadas como tal, com análise da causa.

## Riscos

| Risco | Mitigação |
|---|---|
| mAP abaixo da meta | Ponto de controle PC3: pré-treino em dataset público ou redução de classes |
| Conjunto de teste pequeno gera intervalos largos | Reportar os intervalos como estão; usar reamostragem para calculá-los |
| Tentação de ajustar limiares olhando o conjunto de teste | Qualquer ajuste é feito na validação; o teste é usado uma vez |

## Contribuição para o artigo

Toda a seção de resultados e a discussão de limitações.

## Relatório de encerramento

_A preencher ao concluir a fase._
