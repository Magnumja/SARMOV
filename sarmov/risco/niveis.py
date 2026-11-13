"""Distância de frenagem segura e classificação em níveis de risco.

Os limiares são os valores preliminares do plano de trabalho; a relação
deles com a distância de frenagem está em aberto (questão Q1).
"""

CRITICO = "critico"
ATENCAO = "atencao"
SEGURO = "seguro"

LIMIAR_CRITICO_M = 5.0
LIMIAR_ATENCAO_M = 15.0


def distancia_frenagem(
    velocidade_ms: float, tempo_reacao_s: float = 1.5, desaceleracao_ms2: float = 6.0
) -> float:
    """Distância de parada (m): percurso de reação mais percurso de frenagem."""
    return velocidade_ms * tempo_reacao_s + velocidade_ms**2 / (2 * desaceleracao_ms2)


def classificar(
    distancia_m: float,
    limiar_critico: float = LIMIAR_CRITICO_M,
    limiar_atencao: float = LIMIAR_ATENCAO_M,
) -> str:
    """Nível de risco para uma distância estimada."""
    if distancia_m < limiar_critico:
        return CRITICO
    if distancia_m < limiar_atencao:
        return ATENCAO
    return SEGURO
