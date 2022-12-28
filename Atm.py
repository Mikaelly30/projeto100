def registrar(dados):
    cadastro = input("\n\nCartão: ")
    if cadastro in dados:
        print("Já existe um cartão com esse nome!")
        return
    senha = input("\n\nSenha: ")
    print("Cadastro realizado com suceso!")
    dados[cadastro] = senha

dadosls = {}
answer = input("Você é um usuário novo ou não? ")
if answer == "Sim" or answer == "sim":
    print("Vamos cadastrar")
    registrar(dadosls)
usuario = input("Entre com seu nome: ")
senha2 = input("Digite sua senha: ")
if usuario in dadosls:
    if dadosls[usuario] == senha2:
        print("Login efetuado!")
    else:
        print("Login não efetuado")
else:
    print("Não existe cadatro para esse cartão")