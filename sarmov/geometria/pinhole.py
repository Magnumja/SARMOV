"""Ponto de referência e distância pelo modelo pinhole sobre o plano da via.

Este módulo não depende do detector: recebe caixas e devolve distâncias.
Ver docs/02-arquitetura.md, estágios 3 e 4.
"""

import math
from typing import Optional, Sequence

from sarmov.classes import BURACO, IRREGULARIDADE, OBJETO_NA_PISTA, OBSTACULO

# Estratégias de escolha da coordenada vertical dentro da caixa.
BORDA_SUPERIOR = "y1"
BORDA_INFERIOR = "y2"
PONTO_MEDIO = "meio"

# Escolha do plano de trabalho. A de Buraco e Irregularidade será verificada
# experimentalmente (questão Q3), por isso a estratégia pode ser sobreposta.
ESTRATEGIA_POR_CLASSE = {
    OBSTACULO: BORDA_INFERIOR,
    OBJETO_NA_PISTA: BORDA_INFERIOR,
    BURACO: BORDA_SUPERIOR,
    IRREGULARIDADE: PONTO_MEDIO,
}


def ponto_referencia(
    classe: str, caixa: Sequence[float], estrategia: Optional[str] = None
) -> float:
    """Coordenada vertical `v` (px) do ponto em que o objeto toca a via.

    `caixa` é `(x1, y1, x2, y2)` em pixels da imagem retificada.
    """
    _, y1, _, y2 = caixa
    estrategia = estrategia or ESTRATEGIA_POR_CLASSE[classe]
    if estrategia == BORDA_SUPERIOR:
        return y1
    if estrategia == BORDA_INFERIOR:
        return y2
    if estrategia == PONTO_MEDIO:
        return (y1 + y2) / 2
    raise ValueError(f"estratégia desconhecida: {estrategia!r}")


def distancia(v: float, h: float, alfa: float, fy: float, v0: float) -> Optional[float]:
    """Distância longitudinal (m) até o ponto da via projetado na linha `v`.

    h: altura da câmera sobre a via (m).
    alfa: inclinação da câmera para baixo (rad).
    fy: distância focal vertical (px).
    v0: coordenada vertical do centro óptico (px).

    Devolve `None` quando a equação não é definida: pontos no horizonte ou
    acima dele, e raios que passam da vertical (atrás da câmera).
    """
    teta = alfa + math.atan((v - v0) / fy)
    if teta <= 0 or teta >= math.pi / 2:
        return None
    return h / math.tan(teta)
