"""Treinamento e exportação do detector YOLOv8n a partir de um arquivo de configuração."""

from pathlib import Path

import yaml

from sarmov.sementes import fixar_sementes


def carregar_config(caminho: Path) -> dict:
    with open(caminho, encoding="utf-8") as arquivo:
        return yaml.safe_load(arquivo)


def escolher_dispositivo() -> str:
    """GPU disponível (CUDA ou a do Mac) ou, na falta dela, CPU.

    A biblioteca não escolhe a GPU do Mac sozinha; sem isto o treino roda em CPU.
    """
    import torch

    if torch.cuda.is_available():
        return "0"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def treinar(config: dict):
    """Treina o modelo descrito em `config` e devolve o caminho do melhor checkpoint."""
    from ultralytics import YOLO

    argumentos = dict(config["treino"])
    argumentos.setdefault("device", escolher_dispositivo())
    fixar_sementes(argumentos["seed"])

    modelo = YOLO(config["modelo"])
    modelo.train(data=config["dados"], **argumentos)
    return Path(modelo.trainer.best)


def exportar_tflite(pesos: Path, tamanho_imagem: int) -> Path:
    """Exporta um checkpoint para TFLite e devolve o caminho do arquivo gerado."""
    from ultralytics import YOLO

    return Path(YOLO(pesos).export(format="tflite", imgsz=tamanho_imagem))
