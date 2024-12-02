import time

import pygame

from lyrics import exibir_letra_com_delay, parte_animaizinhos, parte_erguei_as_maos
from menu import exibir_menu

pygame.mixer.init()


def reproduzir_letra(audio_file: str) -> None:
    """Reproduz o áudio e sincroniza com a exibição da letra no terminal"""
    escolha = exibir_menu()
    if escolha == "1":
        parte_erguei_as_maos()
        parte_animaizinhos()
        parte_animaizinhos()

    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        time.sleep(20)

        exibir_letra_com_delay(parte_erguei_as_maos(1), delay=1.6)
        pygame.mixer.music.stop()
    except pygame.error as e:
        print(f"Erro ao carregar ou reproduzir o áudio: {e}")


# if __name__ == "__main__":
#     while True:
#         opcao = exibir_menu()
#         if opcao == "4":
#             break
reproduzir_letra("erguei_as_maos.mp3")
