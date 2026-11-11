# 01 · Visão geral

Compilado do plano de trabalho do PIBIC. Este documento resume o que o projeto se propõe a fazer; os detalhes de construção estão em [Arquitetura](02-arquitetura.md). Os trechos marcados com † são formulações desta documentação, não texto do plano.

## Problema

Segundo a Organização Mundial da Saúde, cerca de 1,3 milhão de pessoas morrem por ano em acidentes viários [20]. Buracos, objetos sobre a pista e irregularidades no pavimento oferecem risco ao condutor quando surgem a uma distância insuficiente para uma manobra segura.

Os sistemas ADAS que alertam o condutor dependem, em sua maioria, de radar, LiDAR ou câmeras estéreo [23, 9]. O custo desses sensores limita a adoção em veículos populares. Um smartphone fixado no painel tem câmera, processador e alto-falante: o que falta é saber se uma única câmera, bem calibrada, entrega distâncias confiáveis.

## Pergunta de pesquisa †

O plano não enuncia uma pergunta de pesquisa. A formulação abaixo foi montada a partir do objetivo geral e das metas.

> Um pipeline que combina detecção por YOLOv8n, calibração de Zhang e geometria *pinhole*, executado em um smartphone, estima a distância até riscos viários com erro suficientemente baixo (MAE < 1,5 m e MAPE < 15 % entre 1 e 15 m) para sustentar um alerta preventivo em tempo real (≥ 10 fps)?

## Objetivos

**Geral.** Desenvolver e avaliar um sistema móvel de baixo custo, baseado em visão monocular, que estime a distância entre a câmera de um smartphone e elementos de risco em vias urbanas e acione alertas preventivos ao motorista.

**Específicos.**

| # | Objetivo | Fase |
|---|---|---|
| O1 | Construir banco de imagens e vídeos capturados por smartphone, com protocolo de coleta estruturado | 2, 3 |
| O2 | Detectar elementos de risco (obstáculos, buracos, irregularidades) com YOLOv8 | 4 |
| O3 | Extrair informações geométricas das caixas delimitadoras para o cálculo de distância | 4 |
| O4 | Aplicar o modelo *pinhole* para estimar a distância longitudinal | 4 |
| O5 | Definir limiares de segurança com base em frenagem segura | 4 |
| O6 | Avaliar o desempenho por métricas de erro (MAE, RMSE, MAPE) e de detecção (precisão, revocação, mAP) | 5 |

## Método em resumo

| Etapa | O que é feito | Parâmetros do plano |
|---|---|---|
| Coleta controlada | Smartphone em suporte rígido; objetos a distâncias aferidas com trena | 1, 2, 3, 5, 7, 10, 12 e 15 m; ≥ 10 imagens por distância; ≥ 500 imagens |
| Coleta urbana | Vídeos em vias de Campo Grande, MS | Av. Afonso Pena e Rua Aracy; 7h, 12h, 17h e 20h; 30 fps; ≥ 1280×720; ≥ 200 imagens |
| Anotação | Caixas delimitadoras em formato YOLO, com revisão dupla | Classes: Buraco, Obstáculo, Objeto na Pista, Irregularidade |
| Divisão | Treino, validação e teste, estratificados por faixa de distância | 70 : 15 : 15 |
| Calibração | Método de Zhang com OpenCV | Xadrez 8×6, quadrados de 2 cm, ≥ 15 imagens, RMS < 0,5 px |
| Detecção | YOLOv8n treinado e exportado para TFLite | 100 épocas, lote 16, SGD, parada antecipada com paciência 20 |
| Distância | Modelo *pinhole* sobre o plano da via | Altura `h` e inclinação `α` medidas em três repetições |
| Alerta | Três níveis por limiar de distância | Crítico < 5 m; Atenção 5–15 m; Seguro ≥ 15 m |
| Avaliação | Erro de distância, qualidade da detecção, matriz de confusão do alerta, desempenho no aparelho | IC de 95 % nas métricas principais |

## Ambiente técnico

| Componente | Uso | Versão |
|---|---|---|
| Python | Linguagem do pipeline de pesquisa | 3.9+ |
| PyTorch | Treinamento | 2.0.0+ |
| Ultralytics | YOLOv8 | 8.0.0+ |
| OpenCV | Calibração e processamento de imagem | 4.8.0+ |
| NumPy | Álgebra linear | 1.24+ |
| TensorFlow Lite | Inferência no smartphone | estável |
| Smartphone | Samsung Galaxy S23 Ultra (prototipação) | — |

As dependências serão fixadas em `requirements.txt`. As sementes aleatórias são fixadas em 42 (`PYTHONHASHSEED`, `torch`, `numpy`).

## Contribuições esperadas

1. **Científica.** Um pipeline unificado de detecção, calibração e geometria projetiva para smartphone, com validação experimental.
2. **Prática.** Uma alternativa de baixo custo para assistência preventiva em veículos sem sensores dedicados.

O plano prevê ainda, entre os resultados esperados, a disponibilização do código-fonte, dos parâmetros de calibração e, quando possível, de amostras anonimizadas do dataset em repositório público.

## Limitações previstas

- O modelo *pinhole* supõe via plana; a precisão degrada em pavimento irregular.
- Sombras, reflexos e variações de iluminação afetam o desempenho.
- O campo de visão fixo limita a cobertura lateral.
- † A validação quantitativa de distância ocorre em ambiente controlado, com câmera estática; aclives e declives também violam a hipótese de via plana.

A discussão detalhada dessas e de outras fragilidades está em [Questões em aberto](04-questoes-em-aberto.md).

## Trabalhos futuros

Estimativa de profundidade por aprendizado profundo (MiDaS [15]), fusão com sensores inerciais do smartphone, avaliação em vídeo contínuo e testes com outros aparelhos.

---

Os números entre colchetes remetem a [Referências](referencias.md).
