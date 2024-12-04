import pygame

from audio import reproducao
from lyrics import (
    exibir_letra_com_delay,
    parte_animaizinhos,
    parte_braços_movimentos,
    parte_constroi_arca,
    parte_erguei_as_maos,
    por_isso,
    separador,
)
from menu import exibir_menu

pygame.mixer.init()

DELAY: float | int = 0.1
MOVIMENTOS: list[str] = [
    "Braço direito",
    "braço esquerdo\n",
    "Perna direita",
    "perna esquerda\n",
    "Balança a cabeça",
    "dá uma voltinha\n",
    "Dá um pulinho",
    "abraça o irmão\n",
]


def exibir_movimentos(movimentos: list[str]) -> None:
    """Exibe os movimentos de forma dinâmica."""
    for i in range(1, len(movimentos) + 1):
        exibir_letra_com_delay(parte_braços_movimentos(), DELAY)
        print("\n".join(movimentos[:i]), end="\n")


def reproduzir_letra(audio_file: str) -> None:
    """Reproduz o áudio e sincroniza com a exibição da letra no terminal."""
    animais = [
        ("O elefante", "os passarinhos"),
        ("A minhoquinha", "os pinguins"),
        ("O canguru", "o sapinho"),
    ]

    escolha = exibir_menu()
    partes = {
        "1": lambda: (
            exibir_letra_com_delay(parte_erguei_as_maos(), DELAY),
            [exibir_letra_com_delay(parte_animaizinhos(a1, a2), DELAY) for a1, a2 in animais],
            exibir_letra_com_delay(parte_constroi_arca(), DELAY),
            exibir_letra_com_delay(por_isso(), DELAY),
            exibir_letra_com_delay(parte_erguei_as_maos(3), DELAY),
            exibir_letra_com_delay(separador(), DELAY),
            exibir_movimentos(MOVIMENTOS),
            reproducao(audio_file, start=0.0),
        ),
        "2": lambda: (
            exibir_letra_com_delay(parte_erguei_as_maos(), DELAY),
            reproducao(audio_file, start=21.7, end=37.0),
        ),
        "3": lambda: (
            exibir_letra_com_delay(parte_constroi_arca(), DELAY),
            reproducao(audio_file, start=80.0, end=93.3),
        ),
        "4": lambda: (
            exibir_letra_com_delay(parte_braços_movimentos(), DELAY),
            reproducao(audio_file, start=140.7, end=153.7),
        ),
    }
    if escolha in partes:
        partes[escolha]()
    elif escolha == "5":
        print("Saindo...")
    else:
        print("Opção inválida.")


reproduzir_letra("erguei_as_maos.mp3")
