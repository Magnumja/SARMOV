# 04 · Questões em aberto

Pontos do plano de trabalho que precisam de decisão ou verificação antes de virarem afirmações no artigo. Nenhum deles invalida a proposta; todos são perguntas que um revisor faria.

Cada questão traz a observação, a consequência e uma sugestão de encaminhamento. As decisões cabem ao autor e ao orientador.

| # | Questão | Impacto | Estado |
|---|---|---|---|
| [Q1](#q1--limiares-de-alerta-e-distância-de-frenagem) | Limiares de alerta e distância de frenagem | Alto | Aberta |
| [Q2](#q2--sensibilidade-ao-ângulo-de-inclinação) | Sensibilidade ao ângulo de inclinação | Alto | Aberta |
| [Q3](#q3--ponto-de-referência-da-classe-buraco) | Ponto de referência da classe Buraco | Médio | Aberta |
| [Q4](#q4--tamanho-do-dataset) | Tamanho do dataset | Alto | Aberta |
| [Q5](#q5--modo-de-captura-e-validade-da-calibração) | Modo de captura e validade da calibração | Alto | Aberta |
| [Q6](#q6--posicionamento-de-buracos-em-ambiente-controlado) | Posicionamento de buracos em ambiente controlado | Médio | Aberta |
| [Q7](#q7--hiperparâmetros-descritos-como-padrão) | Hiperparâmetros descritos como padrão | Baixo | Aberta |
| [Q8](#q8--referências-a-conferir) | Referências a conferir | Médio | Aberta |
| [Q9](#q9--privacidade-das-imagens-urbanas) | Privacidade das imagens urbanas | Médio | Aberta |
| [Q10](#q10--validação-estática-e-uso-em-movimento) | Validação estática e uso em movimento | Médio | Aberta |

---

## Q1 · Limiares de alerta e distância de frenagem

**Observação.** A equação de frenagem do plano resulta em cerca de 27 m a 40 km/h. O nível "Seguro" começa em 15 m, e a faixa de avaliação termina em 15 m. Pela mesma equação, 15 m só é distância suficiente para parar até cerca de 26 km/h.

**Consequência.** A 40 km/h, um objeto classificado como "Seguro" a 16 m já está dentro da distância de parada. O texto do plano justifica a faixa de 1 a 15 m pela análise de frenagem, mas os números não fecham.

**Encaminhamento sugerido.** Escolher uma das saídas e declará-la no artigo:

- delimitar o cenário de uso a baixas velocidades (até cerca de 25 km/h), em que 15 m é coerente; ou
- tornar o limiar função da velocidade, usando a equação de frenagem com a velocidade lida do GPS; ou
- manter limiares fixos e apresentá-los como níveis de proximidade, sem afirmar que derivam da frenagem a 40 km/h.

**Efeito na avaliação do alerta.** Das oito distâncias de coleta, 5 m e 15 m coincidem com os limiares, e 15 m é a única amostra do nível "Seguro". Um erro mínimo para menos a 15 m muda o nível para "Atenção". Para que a avaliação do alerta não dependa desse acaso, convém incluir ao menos uma distância acima de 15 m ou definir uma tolerância em torno dos limiares.

## Q2 · Sensibilidade ao ângulo de inclinação

**Observação.** O erro relativo de distância causado por um erro angular cresce com a distância (ver [Arquitetura](02-arquitetura.md#4-distância)). Com altura de câmera de 1,2 m, meio grau de erro, que é a precisão do inclinômetro prevista, produz cerca de 11 % de erro a 15 m.

**Consequência.** No extremo da faixa, a medição de `α` sozinha leva o erro para perto do limite de 15 %, antes de qualquer erro de detecção ou de calibração. Na média das oito distâncias, o efeito sobre o MAPE é de cerca de 5 %. O plano cita erros de 5 a 15 % para 1 a 2 graus; vale conferir em que altura e distância essa faixa foi obtida, porque a conta acima sugere valores maiores no extremo da faixa.

**Encaminhamento sugerido.**

- Estimar `α` a partir dos próprios dados: ajustar o ângulo que minimiza o erro em alguns pontos de distância conhecida, separados do conjunto de teste.
- Incluir no artigo a análise de sensibilidade, analítica e empírica. O plano prevê variação de ângulo de ±5° na coleta; se esse ângulo for a inclinação da câmera, o que precisa ser confirmado, a própria coleta fornece os dados.
- Reportar o erro por faixa de distância, não só o agregado.

## Q3 · Ponto de referência da classe Buraco

**Observação.** O plano usa a borda superior da caixa ($y_1$) para Buraco. Na imagem, a borda superior de um buraco no chão corresponde à sua borda mais distante.

**Consequência.** A distância estimada é até o fim do buraco, não até o começo. O alerta fica menos conservador exatamente na classe que motiva o projeto.

**Encaminhamento sugerido.** Tratar como experimento: comparar $y_1$, $y_2$ e o ponto médio para cada classe e adotar o que minimiza o erro em relação à medida de trena, deixando explícito a que ponto do objeto a trena se refere. A comparação rende uma tabela de ablação para o artigo.

## Q4 · Tamanho do dataset

**Observação.** São previstas cerca de 700 imagens para quatro classes, com 15 % para teste, o que dá aproximadamente 105 imagens de teste.

**Consequência.** Com esse volume, atingir mAP > 0,75 é incerto, e intervalos de confiança sobre 105 imagens divididas em quatro classes serão largos.

**Encaminhamento sugerido.**

- Declarar o uso de pesos pré-treinados, que o plano não menciona, e, se necessário, fazer um pré-treino em dataset público de danos em pavimento antes do ajuste fino no dataset próprio.
- Reportar o número de instâncias por classe, não só o de imagens.
- Considerar a fusão de classes pouco representadas.

## Q5 · Modo de captura e validade da calibração

**Observação.** O aparelho de prototipação tem sensor de 200 MP e, no uso comum, entrega imagens em resolução menor. O modo foto e o modo vídeo usam recortes diferentes do sensor; estabilização e foco automático alteram a geometria quadro a quadro.

**Consequência.** Parâmetros obtidos com fotos do xadrez não valem para quadros de vídeo a 1280×720. Usá-los introduz um erro sistemático de distância que não aparece no erro de reprojeção.

**Encaminhamento sugerido.** Fixar um único modo de captura para calibração, coleta e aplicativo, com estabilização desligada e foco travado. Registrar o modo no arquivo de calibração. Recalibrar se o modo mudar.

## Q6 · Posicionamento de buracos em ambiente controlado

**Observação.** O protocolo controlado posiciona elementos de risco a distâncias aferidas. Um buraco não pode ser movido.

**Encaminhamento sugerido.** Para Buraco e Irregularidade, mover a câmera em vez do objeto, medindo a distância até um defeito real fixo, ou usar um modelo físico que reproduza a aparência do defeito e declarar essa limitação.

## Q7 · Hiperparâmetros descritos como padrão

**Observação.** O plano justifica a taxa de aprendizado de 0,001 como "Padrão Ultralytics; cosine decay". Na configuração padrão atual da biblioteca, a taxa inicial para SGD é 0,01, o decaimento cosseno vem desligado e o otimizador é escolhido automaticamente, de modo que SGD precisa ser pedido de forma explícita. Rotação de ±10°, escala de 0,8 a 1,2 e paciência de 20 também não são os padrões.

**Encaminhamento sugerido.** Conferir a versão da biblioteca em uso e ajustar os valores ou a justificativa. As configurações do plano são defensáveis; o texto só precisa descrevê-las como escolhas e relatar o que foi de fato executado.

## Q8 · Referências a conferir

**Observação.** A referência [10], da qual saem a faixa de erro esperada e a escolha do ponto de referência, está sem volume, páginas e DOI. As referências [2], [6], [12], [14] e [21] estão com autoria abreviada.

**Encaminhamento sugerido.** Localizar a publicação original de [10] e completar os dados antes da submissão. Como ela sustenta as metas de erro do projeto, convém também confirmar que os valores citados constam do texto.

## Q9 · Privacidade das imagens urbanas

**Observação.** Vídeos em via pública registram rostos e placas de veículos.

**Encaminhamento sugerido.** Borrar rostos e placas antes de publicar qualquer amostra. Manter os dados brutos fora do repositório. Verificar com o orientador se a instituição exige algum registro para a coleta.

## Q10 · Validação estática e uso em movimento

**Observação.** A distância é validada com câmera estática em suporte rígido. Em um veículo, a suspensão e a frenagem alteram a inclinação da câmera a cada instante.

**Consequência.** Os erros medidos em bancada são um limite inferior do erro em uso real.

**Encaminhamento sugerido.** Declarar a limitação no artigo. Se houver tempo, incluir uma avaliação qualitativa em vídeo e registrar a leitura do sensor inercial do aparelho para quantificar a variação de inclinação.
