import json

def carregar_dados():
    try:
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

    
def salvar_dados(dados):
    with open("usuarios.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


def validar_login(usuario, senha):
    usuarios = carregar_dados()
    return usuario in usuarios and usuarios[usuario] == senha


def registrar_usuario(usuario, senha):
    usuarios = carregar_dados()
    if usuario in usuarios:
        return False, "Erro: Usuário já existe."
    else:
        usuarios[usuario] = senha
        salvar_dados(usuarios)
        return True, "Usuário registrado com sucesso!"

def cadastrar():
    usuarios = carregar_dados()
    user = input("Digite o nome do usuário: ")
    if user in usuarios:
        print("Erro: Usuário já existe.")
    else:
        senha = input("Digite sua senha: ")
        usuarios[user] = senha
        salvar_dados(usuarios)
        print("Usuário salvo com sucesso!")

def excluir():
    usuarios = carregar_dados()
    user = input("DIgite o nome do usuário que deseja excluir: ")
    if user in usuarios:
        del usuarios[user]
        salvar_dados(usuarios)
        print(f"Usuário {user} excluído com sucesso!")
    else:
        print(f"Erro: Usuário não encontrado. ")

def listar_usuarios():
    usuarios = carregar_dados()
    print("\n--- Lista de Usuários ---")
    for usuario in usuarios:
        print(f"- {usuario}")


