import time

import pygame

from lyrics import *
from menu import exibir_menu

pygame.mixer.init()

DELAY: float | int = 0.1
MOVIMENTOS: list[str] = [
    "Braço direito",
    "braço esquerdo",
    "Perna direita",
    "perna esquerda",
    "Balança a cabeça",
    "dá uma voltinha",
    "Dá um pulinho",
    "abraça o irmão",
]


# tamanho total da música em segundos: 296
def reproducao(audio_file: str, start: float, end: float = 296.0) -> None:
    """Carrega e inicia a reprodução de um áudio a partir de um ponto específico."""
    if start >= end:
        raise ValueError("O ponto inicial deve ser menor que o ponto final.")

    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_pos(start)
    duracao = end - start
    time.sleep(duracao)
    pygame.mixer.music.stop()


def reproduzir_letra(audio_file: str) -> None:
    """Reproduz o áudio e sincroniza com a exibição da letra no terminal"""

    animais = [
        ("O elefante", "os passarinhos"),
        ("A minhoquinha", "os pinguins"),
        ("O canguru", "o sapinho"),
    ]
    try:
        escolha = exibir_menu()
        if escolha == "1":
            exibir_letra_com_delay(parte_erguei_as_maos(), DELAY)
            for animal1, animal2 in animais:
                letra = parte_animaizinhos(animal1, animal2)
                exibir_letra_com_delay(letra, DELAY)
            # exibir_letra_com_delay(parte_animaizinhos(3), DELAY)
            exibir_letra_com_delay(parte_constroi_arca(), DELAY)
            exibir_letra_com_delay(por_isso(), DELAY)
            exibir_letra_com_delay(parte_erguei_as_maos(3), DELAY)
            exibir_letra_com_delay(separador(), DELAY)
            exibir_letra_com_delay(parte_braços_movimentos(), DELAY)
            print("%s\n" % MOVIMENTOS[0])
            exibir_letra_com_delay(parte_braços_movimentos(), DELAY)
            print("%s, %s\n" % (MOVIMENTOS[0], MOVIMENTOS[1]))
            exibir_letra_com_delay(parte_braços_movimentos(), DELAY)
            print("%s, %s\n%s\n" % (MOVIMENTOS[0], MOVIMENTOS[1], MOVIMENTOS[2]))
            exibir_letra_com_delay(parte_braços_movimentos(), DELAY)
            print("%s, %s\n%s, %s\n" % (MOVIMENTOS[0], MOVIMENTOS[1], MOVIMENTOS[2], MOVIMENTOS[3]))
            exibir_letra_com_delay(parte_braços_movimentos(), DELAY)
            print("%s, %s\n%s, %s\n" % (MOVIMENTOS[0], MOVIMENTOS[1], MOVIMENTOS[2], MOVIMENTOS[3]))
            print("%s" % MOVIMENTOS[4])
            exibir_letra_com_delay(parte_braços_movimentos(), DELAY)
            print("%s, %s\n%s, %s\n" % (MOVIMENTOS[0], MOVIMENTOS[1], MOVIMENTOS[2], MOVIMENTOS[3]))
            print("%s, %s" % (MOVIMENTOS[4], MOVIMENTOS[5]))
            exibir_letra_com_delay(parte_braços_movimentos(), DELAY)

            print(
                "%s, %s\n%s, %s\n%s, %s\n%s\n"
                % (
                    MOVIMENTOS[0],
                    MOVIMENTOS[1],
                    MOVIMENTOS[2],
                    MOVIMENTOS[3],
                    MOVIMENTOS[4],
                    MOVIMENTOS[5],
                    MOVIMENTOS[6],
                )
            )
            exibir_letra_com_delay(parte_braços_movimentos(), DELAY)

            print(
                "%s, %s\n%s, %s\n%s, %s\n%s e %s\n"
                % (
                    MOVIMENTOS[0],
                    MOVIMENTOS[1],
                    MOVIMENTOS[2],
                    MOVIMENTOS[3],
                    MOVIMENTOS[4],
                    MOVIMENTOS[5],
                    MOVIMENTOS[6],
                    MOVIMENTOS[7],
                )
            )

            reproducao(audio_file, start=0.0)
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        elif escolha == "2":
            exibir_letra_com_delay(parte_erguei_as_maos(), DELAY)
            reproducao(audio_file, start=21.7, end=37.0)
            pygame.mixer.music.unload()
        elif escolha == "3":
            exibir_letra_com_delay(parte_constroi_arca(), DELAY)
            reproducao(audio_file, start=80.0, end=94.0)

    except pygame.error as e:
        print(f"Erro ao carregar ou reproduzir o áudio: {e}")


reproduzir_letra("erguei_as_maos.mp3")
