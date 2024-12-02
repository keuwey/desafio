import time

import pygame

from lyrics import exibir_letra_com_delay, parte_animaizinhos, parte_erguei_as_maos
from menu import exibir_menu

pygame.mixer.init()


def reproduzir_letra(audio_file: str) -> None:
    """Reproduz o áudio e sincroniza com a exibição da letra no terminal"""
    try:
        escolha = exibir_menu()
        if escolha == "1":
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            time.sleep(21)
            exibir_letra_com_delay(parte_erguei_as_maos(1), delay=1.6)
            parte_animaizinhos()
        elif escolha == "2":
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play(start=21)
            exibir_letra_com_delay(parte_erguei_as_maos(1), delay=1.6)

    except pygame.error as e:
        print(f"Erro ao carregar ou reproduzir o áudio: {e}")


reproduzir_letra("erguei_as_maos.mp3")
