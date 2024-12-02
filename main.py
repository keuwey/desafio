import time

import pygame

from lyrics import exibir_letra_com_delay, parte_animaizinhos, parte_erguei_as_maos
from menu import exibir_menu

pygame.mixer.init()


def reproducao(audio_file: str, start: float = 0.0) -> None:
    """Carrega e inicia a reprodução de um áudio a partir de um ponto específico."""
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_pos(start)


def reproduzir_letra(audio_file: str) -> None:
    """Reproduz o áudio e sincroniza com a exibição da letra no terminal"""
    try:
        escolha = exibir_menu()
        if escolha == "1":
            reproducao(audio_file, start=0)
            time.sleep(21)
            exibir_letra_com_delay(parte_erguei_as_maos(1), delay=1.6)
            parte_animaizinhos()
        elif escolha == "2":
            reproducao(audio_file, start=21)
            exibir_letra_com_delay(parte_erguei_as_maos(1), delay=1.6)

    except pygame.error as e:
        print(f"Erro ao carregar ou reproduzir o áudio: {e}")


reproduzir_letra("erguei_as_maos.mp3")
