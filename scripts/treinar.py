"""Treina o detector a partir de um arquivo de configuração.

Uso, a partir da raiz do repositório:
    python -m scripts.treinar configs/treino_referencia.yaml
    python -m scripts.treinar configs/treino_referencia.yaml --epocas 1 --exportar
"""

import argparse
from pathlib import Path

from sarmov.deteccao.treino import carregar_config, exportar_tflite, treinar


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("config", type=Path)
    parser.add_argument("--epocas", type=int, help="sobrepõe o número de épocas (teste rápido)")
    parser.add_argument("--dispositivo", help="cpu, mps ou índice da GPU; padrão: GPU, se houver")
    parser.add_argument("--exportar", action="store_true", help="exporta o melhor checkpoint para TFLite")
    args = parser.parse_args()

    config = carregar_config(args.config)
    if not Path(config["dados"]).exists():
        raise SystemExit(f"Dataset não encontrado: {config['dados']}. Veja data/README.md.")
    if args.epocas:
        config["treino"]["epochs"] = args.epocas
    if args.dispositivo:
        config["treino"]["device"] = args.dispositivo

    melhor = treinar(config)
    print(f"Melhor checkpoint: {melhor}")
    if args.exportar:
        print(f"TFLite: {exportar_tflite(melhor, config['treino']['imgsz'])}")


if __name__ == "__main__":
    main()
