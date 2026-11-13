import pytest

from sarmov.risco import ATENCAO, CRITICO, SEGURO, classificar, distancia_frenagem


def test_frenagem_a_40_kmh_do_plano():
    # 11,11 m/s * 1,5 s + 11,11² / (2 * 6) = 16,67 + 10,29
    assert distancia_frenagem(40 / 3.6) == pytest.approx(26.95, abs=0.01)


def test_frenagem_parado():
    assert distancia_frenagem(0.0) == 0.0


@pytest.mark.parametrize(
    "distancia_m, nivel",
    [(1.0, CRITICO), (4.99, CRITICO), (5.0, ATENCAO), (14.99, ATENCAO), (15.0, SEGURO), (30.0, SEGURO)],
)
def test_niveis_e_limiares(distancia_m, nivel):
    assert classificar(distancia_m) == nivel
