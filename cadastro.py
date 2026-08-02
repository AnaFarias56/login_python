import funcoes

novo_usuario = input("Digite o nome do novo usuário: ")
nova_senha = input("Digite a senha do novo usuário: ")

sucesso, mensagem = funcoes.registrar_usuario(novo_usuario, nova_senha)

print(mensagem)