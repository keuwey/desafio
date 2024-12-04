import time

import pygame


def reproducao(audio_file: str, start: float, end: float = 296.0):
    """Carrega e inicia a reprodução de um áudio a partir de um ponto específico."""
    if start >= end:
        raise ValueError("O ponto inicial deve ser menor que o ponto final.")
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_pos(start)
    time.sleep(end - start)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
