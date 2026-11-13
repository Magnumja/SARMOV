import math

import pytest

from sarmov.classes import BURACO, CLASSES, IRREGULARIDADE, OBJETO_NA_PISTA, OBSTACULO
from sarmov.geometria import distancia, ponto_referencia
from sarmov.geometria.pinhole import BORDA_INFERIOR, ESTRATEGIA_POR_CLASSE

CAIXA = (100, 200, 300, 400)


def test_ponto_referencia_segue_a_tabela_do_plano():
    assert ponto_referencia(OBSTACULO, CAIXA) == 400
    assert ponto_referencia(OBJETO_NA_PISTA, CAIXA) == 400
    assert ponto_referencia(BURACO, CAIXA) == 200
    assert ponto_referencia(IRREGULARIDADE, CAIXA) == 300


def test_toda_classe_tem_estrategia():
    assert set(ESTRATEGIA_POR_CLASSE) == set(CLASSES)


def test_estrategia_pode_ser_sobreposta():
    assert ponto_referencia(BURACO, CAIXA, estrategia=BORDA_INFERIOR) == 400


def test_estrategia_desconhecida():
    with pytest.raises(ValueError):
        ponto_referencia(BURACO, CAIXA, estrategia="canto")


def test_camera_nivelada_a_45_graus():
    # alfa = 0 e (v - v0) = fy dão um raio a 45° para baixo: d = h.
    assert distancia(v=1540, h=1.2, alfa=0.0, fy=1000, v0=540) == pytest.approx(1.2)


def test_centro_optico_aponta_para_a_distancia_da_inclinacao():
    alfa = math.atan(1.2 / 10)
    assert distancia(v=540, h=1.2, alfa=alfa, fy=1000, v0=540) == pytest.approx(10.0)


def test_linha_mais_baixa_na_imagem_esta_mais_perto():
    alfa = math.radians(5)
    perto = distancia(v=900, h=1.2, alfa=alfa, fy=1000, v0=540)
    longe = distancia(v=600, h=1.2, alfa=alfa, fy=1000, v0=540)
    assert perto < longe


def test_raio_alem_da_vertical_nao_tem_distancia():
    # Câmera a 60° para baixo e ponto 45° abaixo do eixo óptico: 105° no total.
    assert distancia(v=1540, h=1.2, alfa=math.radians(60), fy=1000, v0=540) is None


def test_horizonte_e_acima_nao_tem_distancia():
    assert distancia(v=540, h=1.2, alfa=0.0, fy=1000, v0=540) is None
    assert distancia(v=100, h=1.2, alfa=math.radians(5), fy=1000, v0=540) is None
