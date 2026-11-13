# Dados

Esta pasta fica fora do versionamento, exceto este arquivo e `amostras/`. Dados brutos e datasets públicos nunca são enviados ao repositório.

## Organização

```text
data/
├── raw/
│   ├── publico/<dataset>/     # datasets públicos, como foram baixados
│   ├── controlado/<sessao>/   # coleta controlada, com a planilha de distância real
│   └── urbano/<sessao>/       # quadros extraídos dos vídeos urbanos
├── yolo/
│   ├── referencia/            # dataset público do treino de referência (fase 1)
│   └── sarmov/                # dataset próprio, dividido 70/15/15 por sessão (fase 3)
└── amostras/                  # amostras anonimizadas, versionadas
```

Cada pasta em `yolo/` contém um `data.yaml` no formato da Ultralytics, com os caminhos de treino, validação e teste e os nomes das classes.

## Treino de referência

O arquivo `configs/treino_referencia.yaml` espera um dataset em formato YOLO em `data/yolo/referencia/`, com `data.yaml` na raiz. Qualquer dataset público de buracos nesse formato serve. O sugerido é o de detecção de buracos do Roboflow Universe, citado na Tabela 1 de Safyari et al. (2024):

<https://universe.roboflow.com/intel-unnati-training-program/pothole-detection-bqu6s/dataset/9>

Baixe no formato "YOLOv8" e extraia o conteúdo em `data/yolo/referencia/`. Confira os caminhos dentro do `data.yaml` baixado e a licença do dataset antes de publicar pesos treinados com ele.

## Regra do conjunto de teste

O conjunto de teste do artigo contém apenas imagens próprias. Dados públicos entram somente no treino e na validação.
