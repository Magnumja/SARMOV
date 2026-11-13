"""Verifica o ambiente: versões instaladas, sementes e núcleo geométrico.

Uso, a partir da raiz do repositório:
    python -m scripts.verificar_ambiente
"""

import math
import platform
from importlib import metadata
from pathlib import Path

from sarmov.geometria import distancia
from sarmov.sementes import fixar_sementes

REQUISITOS = Path(__file__).resolve().parent.parent / "requirements.txt"
PRINCIPAIS = ("numpy", "torch", "ultralytics", "opencv-python")


def divergencias() -> list:
    """Pacotes de requirements.txt ausentes ou em versão diferente da registrada."""
    problemas = []
    for linha in REQUISITOS.read_text(encoding="utf-8").splitlines():
        if "==" not in linha or linha.startswith("#"):
            continue
        nome, registrada = linha.strip().split("==")
        try:
            instalada = metadata.version(nome)
        except metadata.PackageNotFoundError:
            instalada = "ausente"
        if instalada != registrada:
            problemas.append(f"{nome}: registrada {registrada}, instalada {instalada}")
    return problemas


def main() -> None:
    print(f"Python {platform.python_version()} ({platform.machine()})")
    for nome in PRINCIPAIS:
        try:
            print(f"  {nome} {metadata.version(nome)}")
        except metadata.PackageNotFoundError:
            print(f"  {nome} ausente")

    problemas = divergencias()
    if problemas:
        raise SystemExit("Versões diferentes de requirements.txt:\n  " + "\n  ".join(problemas))

    from sarmov.deteccao.treino import escolher_dispositivo

    print(f"  dispositivo de treino: {escolher_dispositivo()}")

    fixar_sementes()
    # Câmera a 1,2 m, apontada para um ponto a 10 m: o centro óptico deve dar 10 m.
    d = distancia(v=540, h=1.2, alfa=math.atan(1.2 / 10), fy=1000, v0=540)
    assert d is not None and abs(d - 10) < 1e-9, d

    print("Ambiente verificado: versões iguais às de requirements.txt.")


if __name__ == "__main__":
    main()
