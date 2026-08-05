import funcoes

while True:
    print("\n--- MENU ---")
    print("1. Login | 2. Cadastro | 3. Listar Usuários | 4. Excluir | 5. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        user = input("Usuário: ")
        senha = input("Senha: ")
        sucesso, mensagem = funcoes.validar_login(user, senha)
        print(mensagem)
            
    elif opcao == "2":
        user = input("Novo Usuário: ")
        senha = input("Senha: ")
        sucesso, mensagem = funcoes.registrar_usuario(user, senha)
        print(mensagem)
        
    elif opcao == "3":
        funcoes.listar_usuarios()   

    elif opcao == "4":
        usuario_alvo = input("Digite o nome do usuário que deseja excluir: ")
        funcoes.excluir(usuario_alvo)

    elif opcao == "5":
        print("Saindo do sistema...")
        break  