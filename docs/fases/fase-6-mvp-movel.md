# Fase 6 · MVP móvel

| Estado | Bimestres sugeridos | Atividades do cronograma | Depende de |
|---|---|---|---|
| Planejada | B5–B6 | 6. Implementação do método (inferência no aparelho) | Etapa 4c |

## Objetivo

Levar o pipeline validado para o smartphone: um aplicativo que captura a câmera, detecta, estima a distância e alerta em tempo real.

O escopo, os requisitos e a arquitetura estão no [Plano do MVP](../mvp/plano-do-mvp.md). Este documento acompanha a execução.

## Entregas

- [ ] Plataforma confirmada com o orientador
- [ ] Captura de câmera no mesmo modo usado na calibração
- [ ] Inferência do modelo TFLite no aparelho
- [ ] Geometria e classificação de risco reimplementadas e conferidas contra o pipeline Python
- [ ] Alerta de cada nível conforme a tabela de risco do plano: som contínuo e vibração no Crítico; indicador luminoso e vibração leve no Atenção; apenas monitoramento no Seguro
- [ ] Tela de configuração: altura da câmera, inclinação e arquivo de calibração
- [ ] Registro de sessão exportável, com detecções, distâncias, níveis e tempo por quadro
- [ ] Medição de desempenho no aparelho (experimento E8)
- [ ] Vídeo de demonstração

## Critérios de aceite

- Taxa de quadros igual ou superior a 10 fps no aparelho de prototipação, medida em sessão contínua de 30 minutos.
- Para um mesmo conjunto de imagens, a distância calculada pelo aplicativo coincide com a do pipeline Python dentro de uma tolerância numérica definida.
- O nível e o alerta correspondente estão corretos em teste de bancada com objetos a distâncias conhecidas, afastadas dos limiares de 5 e 15 m.

## Riscos

| Risco | Mitigação |
|---|---|
| Queda de desempenho por aquecimento em sessões longas | Medir a taxa de quadros ao longo do tempo, não só no início |
| Aplicativo captura em modo diferente do calibrado | Fixar resolução e desligar estabilização por código; validar com o padrão xadrez |
| Divergência entre a geometria do aplicativo e a do Python | Conjunto de casos de teste compartilhado entre as duas implementações |
| Uso do aplicativo distrai o motorista | Alertas não exigem olhar para a tela; testes apenas em bancada ou com passageiro operando |

## Contribuição para o artigo

Medições de tempo por quadro e taxa de quadros, e a demonstração de que o sistema opera em tempo real em hardware de consumo.

## Relatório de encerramento

_A preencher ao concluir a fase._
