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
