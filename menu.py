def exibir_menu() -> str:
    """Exibe o menu principal e retorna a escolha do usuário."""
    while True:
        print("Menu Principal:")
        print("1 - Reproduzir a música inteira")
        print("2 - Reproduzir a parte 'Erguei as Mãos'")
        print("3 - Reproduzir a parte 'Deus disse a Noé...'")
        print("4 - Reproduzir a parte 'O Senhor tem Muitos Filhos'")
        print("5 - Sair")
        escolha = input("\nEscolha uma opção: ").strip()
        if escolha in {"1", "2", "3", "4", "5"}:
            return escolha
        print("Opção inválida. Tente novamente.")
