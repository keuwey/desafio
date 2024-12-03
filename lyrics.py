import time


def parte_erguei_as_maos(repeticoes: int = 1) -> list[str]:
    """Retorna o trecho repetitivo da parte 'Erguei as mãos'."""
    trecho: list[str] = [
        "Erguei as mãos e dai glória a Deus",
        "Erguei as mãos e dai glória a Deus",
        "Erguei as mãos",
        "E cantai como os filhos do Senhor",
        "\n",
    ]
    return trecho * repeticoes


def parte_animaizinhos(repeticoes: int = 1) -> list[str]:
    """Retorna o trecho da parte 'Os animaizinhos subiram de dois em dois'."""
    base: list[str] = [
        "Os animaizinhos subiram de dois em dois",
        "Os animaizinhos subiram de dois em dois",
        "O elefante",
        "E os passarinhos, como os filhos do Senhor",
        "\n",
    ]
    return base * repeticoes


def parte_constroi_arca(repeticoes: int = 1):
    base: list[str] = [
        "Deus disse a Noé: Constrói uma arca",
        "Deus disse a Noé: Constrói uma arca",
        "Que seja feita",
        "De madeira para os filhos do Senhor",
        "\n",
    ]
    return base * repeticoes


def por_isso() -> list[str]:
    return ["Por isso...!"]


def separador() -> list[str]:
    return ["E atenção agora, porque"]


def parte_braços_movimentos(repeticoes: int = 1) -> list[str]:
    """Retorna o trecho da parte 'O Senhor tem muitos filhos'."""
    base: list[str] = [
        "O Senhor tem muitos filhos",
        "Muitos filhos ele tem",
        "Eu sou um deles, você também",
        "Louvemos ao Senhor",
        "\n",
    ]
    return base * repeticoes


def exibir_letra_com_delay(letra: list[str], delay: float | int) -> None:
    """
    Exibe cada linha da letra no terminal com um intervalo de tempo (delay).
    :param letra: Lista de strings representando a letra.
    :param delay: Tempo em segundos entre cada linha.
    """
    for linha in letra:
        print(linha)
        time.sleep(delay)
