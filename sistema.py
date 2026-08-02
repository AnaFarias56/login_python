import funcoes

print(" -- Tela de Login -- ")
usuario_login = input("Digite seu usuario: ")
senha_login = input("Digite sua senha: ")

if funcoes.validar_login(usuario_login, senha_login):
    print("Login feito com sucesso! Bem-vindo(a)!")
else:
    print("Usuário ou senha incorretos. Acesso negado.")