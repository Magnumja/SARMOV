# Plano do artigo

Como o plano de trabalho do PIBIC se torna um artigo científico: o que o artigo afirma, que evidência sustenta cada afirmação e quais experimentos a produzem.

## Do plano ao artigo

O plano de trabalho já tem o esqueleto de um artigo. O que muda é o tempo verbal e o peso de cada parte.

| Seção do plano | Vira, no artigo | O que falta |
|---|---|---|
| Introdução | Introdução | Enunciar a lacuna e as contribuições em lista explícita |
| Objetivos | Último parágrafo da introdução | Reescrever como pergunta de pesquisa |
| Trabalhos correlatos | Trabalhos correlatos | Tabela comparativa com números |
| Materiais e métodos | Método e configuração experimental | Trocar "será" por "foi"; registrar o que mudou |
| Resultados esperados | Resultados | Substituir metas por medições, com intervalos de confiança |
| Impactos e limitações | Discussão e ameaças à validade | Aprofundar com a análise de falhas |
| Cronograma | — | Não entra |

## Tese central

> Com calibração cuidadosa, a geometria *pinhole* sobre detecções de um YOLOv8n estima a distância até riscos viários, em smartphone e em tempo real, com erro caracterizado por faixa de distância entre 1 e 15 m.

O plano declara que o trabalho é de integração e validação, não de novos algoritmos. Isso define o que o artigo precisa entregar para ter valor: **a caracterização do erro**. Um revisor não espera um método novo; espera saber quanto o método erra, onde, e por quê.

## Contribuições a declarar

1. Um pipeline integrado de detecção e estimativa monocular de distância para riscos viários, executável em smartphone.
2. Um protocolo de coleta com distâncias aferidas, que permite medir o erro de distância por faixa.
3. Uma decomposição do erro: quanto vem da geometria, quanto da detecção e quanto da medição da pose da câmera.
4. Código, parâmetros de calibração e amostra do dataset públicos.

A terceira contribuição é a que diferencia o artigo de um relato de implementação.

## Afirmações e evidências

| Afirmação | Evidência necessária | Experimento |
|---|---|---|
| A câmera foi calibrada com qualidade suficiente | Erro de reprojeção RMS < 0,5 px | E1 |
| O detector identifica os riscos | Precisão, revocação e mAP por classe | E2 |
| A geometria estima a distância com erro baixo | MAE, RMSE e MAPE por distância, com caixas manuais | E3 |
| O sistema completo mantém esse erro | As mesmas métricas com caixas detectadas | E4 |
| A escolha do ponto de referência é adequada | Comparação entre alternativas, por classe | E5 |
| O erro é explicado pela incerteza na pose da câmera | Curva de erro prevista contra erro medido | E6 |
| O alerta é confiável | Matriz de confusão dos níveis | E7 |
| O sistema opera em tempo real | Tempo por quadro e taxa de quadros no aparelho | E8 |
| As limitações são conhecidas | Casos de falha documentados | E9 |

## Experimentos

| # | Experimento | Dados | Saída |
|---|---|---|---|
| E1 | Calibração | Imagens do padrão xadrez | Tabela de parâmetros e RMS |
| E2 | Detecção | Conjunto de teste completo | Tabela por classe; curva precisão-revocação |
| E3 | Distância, geometria isolada | Imagens controladas com caixas manuais | Tabela e gráfico de erro por distância |
| E4 | Distância, ponta a ponta | Imagens controladas com caixas detectadas | Mesma tabela, lado a lado com E3 |
| E5 | Ablação do ponto de referência | Imagens controladas | Tabela: classe × ponto × MAE |
| E6 | Sensibilidade a `α` e `h` | Capturas com ângulo nominal e ±5°, se o ângulo variado na coleta for a inclinação; a variação de `h` exige capturas adicionais | Curva analítica sobreposta aos pontos medidos |
| E7 | Alerta | Imagens controladas com nível real conhecido | Matriz de confusão do alerta, como define o plano |

Para E7, é preciso definir o que conta como positivo. A proposta é considerar positivo o caso em que o nível real é Crítico ou Atenção. Uma matriz 3×3 por nível pode complementar a análise, mas as metas do plano (verdadeiros positivos acima de 85 %, falsos positivos abaixo de 15 %) se referem à matriz binária.
| E8 | Desempenho | Sessão no aparelho | Tempo por quadro, taxa de quadros |
| E9 | Falhas | Imagens noturnas, com sombra e com oclusão | Figura com exemplos comentados |

Comparar E3 com E4 mostra quanto do erro final vem do detector. Comparar a curva analítica de E6 com os pontos medidos mostra se o modelo de erro explica o que se observa. Esses dois contrastes são o centro da seção de resultados.

### Comparação com outros métodos

O plano não prevê comparação com outro método de estimativa de distância, e um revisor pode pedi-la. Duas opções de custo baixo, a decidir com o orientador:

- estimativa pela altura aparente de um objeto de tamanho conhecido;
- um modelo de profundidade monocular pré-treinado, como o MiDaS, que o plano já cita como trabalho futuro.

## Figuras e tabelas previstas

| Item | Conteúdo | Origem |
|---|---|---|
| Figura 1 | Diagrama do pipeline | [Arquitetura](../02-arquitetura.md) |
| Figura 2 | Geometria da câmera: `h`, `α`, ponto de referência e distância | A desenhar |
| Figura 3 | Arranjo experimental do ambiente controlado | Foto da coleta |
| Figura 4 | Erro de distância por faixa, com caixas manuais e detectadas | E3, E4 |
| Figura 5 | Sensibilidade: curva prevista e pontos medidos | E6 |
| Figura 6 | Exemplos de detecção com distância, e casos de falha | E9 |
| Tabela 1 | Comparação com trabalhos correlatos | Fase 1 |
| Tabela 2 | Composição do dataset | Fase 3 |
| Tabela 3 | Parâmetros de calibração | E1 |
| Tabela 4 | Métricas de detecção por classe | E2 |
| Tabela 5 | Métricas de distância por faixa | E3, E4 |
| Tabela 6 | Ablação do ponto de referência | E5 |
| Tabela 7 | Matriz de confusão do alerta | E7 |
| Tabela 8 | Desempenho no aparelho | E8 |

## Ameaças à validade

A seção deve tratar, no mínimo, dos pontos abaixo. Cada um está detalhado em [Questões em aberto](../04-questoes-em-aberto.md).

| Ameaça | Tipo | Questão |
|---|---|---|
| Hipótese de via plana | Construção | — |
| Validação com câmera estática | Externa | Q10 |
| Um único aparelho | Externa | — |
| Dataset pequeno, de uma única cidade | Externa | Q4 |
| Limiares de alerta fixos, independentes da velocidade | Construção | Q1 |
| Medição manual de `h` e `α` | Interna | Q2 |
| Definição do ponto medido com a trena em cada classe | Interna | Q3 |

## Estatística

- Intervalos de confiança de 95 % por reamostragem (*bootstrap*) sobre as imagens de teste.
- Erro reportado por distância, com média e dispersão, além do agregado.
- Gráfico de concordância entre distância real e estimada, para expor viés sistemático.
- O conjunto de teste é usado uma única vez; ajustes são feitos na validação.

## Veículo de publicação

A escolha cabe ao orientador. Vale levantar, no início da fase 7:

- o seminário de iniciação científica da instituição, se o edital do programa o previr;
- trilhas de iniciação científica e de trabalhos de graduação em eventos brasileiros de computação e de visão computacional;
- o modelo de formatação e o limite de páginas, que definem quantas das figuras e tabelas acima cabem.

## Lista de verificação antes da submissão

- [ ] Toda afirmação quantitativa aponta para uma tabela ou figura
- [ ] O método descrito é o que foi executado
- [ ] Hiperparâmetros conferem com os arquivos de configuração
- [ ] Referências completas e conferidas
- [ ] Metas não atingidas estão reportadas e discutidas
- [ ] Repositório público citado, com a versão exata usada nos experimentos
- [ ] Imagens publicadas estão anonimizadas
