usuarios = []

def cadastro():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))

    if verificar_maior_idade(idade):
        id = len(usuarios) + 1
        
        cadastrar_usuario(id, nome, idade)

        print("Usuário cadastrado com sucesso!")
    else:
        print("Usuário não pode ser cadastrado. É menor de idade.")

def cadastrar_usuario(id, nome, idade):
    usuario = {
        "id": id,
        "nome": nome,
        "idade": idade
    }
    usuarios.append(usuario)
  
def verificar_maior_idade(idade):
    if idade >= 18:
        return True
    return False

def listar_usuarios():
        for u in usuarios:
            print(f"ID: {u['id']} | Nome: {u['nome']} | Idade: {u['idade']}")

def buscar_usuario(id):
    for u in usuarios:
        if u['id'] == id:
            print(f"ID: {u['id']} | Nome: {u['nome']} | Idade: {u['idade']}")
            return        
    print("Usuário não encontrado.")

def remover_usuario(id):
    for u in usuarios:
        if u['id'] == id:
            usuarios.remove(u)
            print("Usuário removido com sucesso!")
            return        
    print("Usuário não encontrado.")

def atualizar_usuario(id, nome, idade):
    for u in usuarios:
        if u['id'] == id:
            u['nome'] = nome
            u['idade'] = idade
            print("Usuário atualizado com sucesso!")
            return        
    print("Usuário não encontrado.")