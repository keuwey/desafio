import time
from typing import List


def gerar_parte(base: List[str], repeticoes: int = 1) -> List[str]:
    """Gera uma parte repetitiva da música."""
    return base * repeticoes


def parte_erguei_as_maos(repeticoes: int = 1) -> List[str]:
    return gerar_parte(
        [
            "Erguei as mãos e dai glória a Deus",
            "Erguei as mãos e dai glória a Deus",
            "Erguei as mãos",
            "E cantai como os filhos do Senhor",
            "\n",
        ],
        repeticoes,
    )


def por_isso() -> list[str]:
    return ["Por isso...!"]


def separador() -> list[str]:
    return ["E atenção agora, porque", "\n"]


def parte_animaizinhos(animal1: str, animal2: str, repeticoes: int = 1) -> List[str]:
    return gerar_parte(
        [
            "Os animaizinhos subiram de dois em dois",
            "Os animaizinhos subiram de dois em dois",
            f"{animal1}",
            f"E {animal2}, como os filhos do Senhor",
            "\n",
        ],
        repeticoes,
    )


def parte_constroi_arca(repeticoes: int = 1) -> list[str]:
    """
    Retorna o trecho da parte 'Deus disse a Noé'.
    Parameters:
        repeticoes: Número de vezes que o verso irá se repetir
    """
    return gerar_parte(
        [
            "Deus disse a Noé: Constrói uma arca",
            "Deus disse a Noé: Constrói uma arca",
            "Que seja feita",
            "De madeira para os filhos do Senhor",
            "\n",
        ],
        repeticoes,
    )


def parte_braços_movimentos(repeticoes: int = 1) -> list[str]:
    """
    Retorna o trecho da parte 'O Senhor tem muitos filhos'.
    Parameters:
        repeticoes: Número de vezes que o verso irá se repetir
    """
    return gerar_parte(
        [
            "O Senhor tem muitos filhos",
            "Muitos filhos ele tem",
            "Eu sou um deles, você também",
            "Louvemos ao Senhor",
            "\n",
        ],
        repeticoes,
    )


def exibir_letra_com_delay(letra: List[str], delay: float | int) -> None:
    """
    Exibe cada linha da letra no terminal com um intervalo de tempo (delay).
    Parameters:
        letra: Lista de strings representando a letra.
        delay: Tempo em segundos entre cada linha.
    """
    for linha in letra:
        print(linha)
        time.sleep(delay)
