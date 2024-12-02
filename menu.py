def exibir_menu() -> str:
    """
    Exibe o menu principal e retorna a escolha do usuário.
    """
    print("Menu Principal:")
    print("1 - Reproduzir a música inteira")
    print("2 - Reproduzir a parte 'Erguei as Mãos'")
    print("3 - Reproduzir a parte 'O Senhor tem Muitos Filhos'")
    print("4 - Sair")
    escolha: str = input("\nEscolha uma opção: ").strip()
    return escolha
