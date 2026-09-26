from cadastro import listar_usuarios, cadastro, remover_usuario, buscar_usuario, atualizar_usuario

while True:
    print("\n=== Menu ===")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário")
    print("4. Remover usuário")
    print("5. Atualizar usuário")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastro()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        usuario_id = int(input("Digite o ID do usuário a ser buscado: "))
        buscar_usuario(usuario_id)
    elif opcao == "4":
        usuario_id = int(input("Digite o ID do usuário a ser removido: "))
        remover_usuario(usuario_id)
    elif opcao == "5":
        usuario_id = int(input("Digite o ID do usuário a ser atualizado: "))
        nome = input("Digite o novo nome do usuário: ")
        idade = int(input("Digite a nova idade do usuário: "))
        atualizar_usuario(usuario_id, nome, idade)
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")
