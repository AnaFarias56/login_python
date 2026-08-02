import funcoes

while True:
    print("\n--- MENU ---")
    print("1. Login | 2. Cadastro | 3. Excluir | 4. Listar Usuários | 5. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        user = input("Usuário: ")
        senha = input("Senha: ")
        if funcoes.validar_login(user, senha):
            print("Login feito com sucesso!")
        else:
            print("Dados incorretos.")
            
    elif opcao == "2":
        user = input("Novo Usuário: ")
        senha = input("Senha: ")
        sucesso, mensagem = funcoes.registrar_usuario(user, senha)
        print(mensagem)
        
    elif opcao == "3":
        user = input("Digite o nome do usuário que deseja excluir: ")
        funcoes.excluir(user)

    elif opcao == "4":
        funcoes.listar_usuarios()   

    elif opcao == "5":
        print("Saindo do sistema...")
        break   