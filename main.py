lista = []

while True:
    menu = input("1 - Cadastrar usuário\n"
                 "2 - Lista de usuários\n"
                 "3 - Buscar usuário\n"
                 "4 - Sair\n"
                 "Escolha: ")

    if menu == "1":
        nome = input("Nome do usuário: ").lower()

        if nome in lista:
            print("Usuário já cadastrado!")
        else:
            lista.append(nome)
            print("Usuário cadastrado com sucesso!")

    elif menu == "2":
        if not lista:
            print("Nenhum usuário cadastrado.")
        else:
            for i, usuario in enumerate(lista):
                print(f"{i+1} - {usuario}")

    elif menu == "3":
        busca = input("Insira o nome do usuário: ").lower()

        if busca in lista:
            print(f"Usuário {busca} encontrado!")
        else:
            print("Usuário não encontrado!")

    elif menu == "4":
        print("Encerrando o programa...")
        break
