"""Fixação única das sementes aleatórias do projeto."""

import os
import random

SEMENTE_PADRAO = 42


def fixar_sementes(semente: int = SEMENTE_PADRAO) -> int:
    """Fixa as sementes de `random`, `numpy` e, se instalado, `torch`.

    `PYTHONHASHSEED` só afeta o interpretador atual se for definido antes de
    ele iniciar; aqui ele é definido para os subprocessos (por exemplo, os
    trabalhadores do carregador de dados).
    """
    os.environ["PYTHONHASHSEED"] = str(semente)
    random.seed(semente)

    import numpy as np

    np.random.seed(semente)

    try:
        import torch
    except ImportError:
        return semente

    torch.manual_seed(semente)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(semente)
    return semente
