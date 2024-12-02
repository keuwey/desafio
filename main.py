import time

import pygame

from lyrics import *
from menu import exibir_menu

pygame.mixer.init()

DELAY: float | int = 1.6


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
    try:
        escolha = exibir_menu()
        if escolha == "1":
            reproducao(audio_file, start=0.0)
            time.sleep(21)
            while pygame.mixer.music.get_busy():
                exibir_letra_com_delay(parte_erguei_as_maos(), DELAY)
                # FIXME: Trocar dinamicamente o nome dos animais
                exibir_letra_com_delay(parte_animaizinhos(3), DELAY)
                exibir_letra_com_delay(parte_constroi_arca(), DELAY)
                exibir_letra_com_delay(parte_erguei_as_maos(3), DELAY)
                exibir_letra_com_delay(parte_braços_movimentos(3), DELAY)

            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        elif escolha == "2":
            # FIXME: Por causa do time.sleep(duracao) na linha 21,
            #       a letra só começa a tocar depois dessa duração
            exibir_letra_com_delay(parte_erguei_as_maos(), DELAY)
            reproducao(audio_file, start=21.7, end=37.0)
            pygame.mixer.music.unload()
        elif escolha == "3":
            exibir_letra_com_delay(parte_constroi_arca(), DELAY)
            reproducao(audio_file, start=80.0, end=93.0)

    except pygame.error as e:
        print(f"Erro ao carregar ou reproduzir o áudio: {e}")


reproduzir_letra("erguei_as_maos.mp3")
