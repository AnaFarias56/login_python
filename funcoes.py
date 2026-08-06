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


def validar_login(user, senha):
    usuarios = carregar_dados()

    if user in usuarios and usuarios[user] == senha:
        if len(senha.strip()) < 6:
            return False, "Aviso! Sua senha é muito curta e fora do novo padrão. Por favor, cadastre-se novamente com uma senha mais forte."
        return True, "Login bem-sucedido!"
    else:
        return False, "Erro: Usuário ou senha incorretos."
       
       


def registrar_usuario(user, senha):
    user = user.strip()
    if "@" not in user or "." not in user:
        return False, "Erro: O nome de usuário deve ser um e-mail válido."
    
    if len(senha.strip()) <6:
        return False, "Erro: A senha deve ter pelo menos 6 caracteres."
    
    usuarios = carregar_dados()

    if user in usuarios:
        return False, "Erro: Este email já está em uso."

    usuarios[user] = senha
    salvar_dados(usuarios)
    return True, "Usuário registrado com sucesso!"
        
def listar_usuarios():
    usuarios = carregar_dados()
    print("\n--- Lista de Usuários ---")
    for usuario in usuarios:
        print(f"- {usuario}")

def excluir(usuario_alvo):
    usuarios = carregar_dados()
    
    if usuario_alvo in usuarios:
        del usuarios[usuario_alvo]
        salvar_dados(usuarios)
        print(f"Usuário '{usuario_alvo}' excluído com sucesso.")
    else:
        print(f"Erro: O usuário '{usuario_alvo}' não foi encontrado.")



