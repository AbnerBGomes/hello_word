import random

print("Bem Vindo ao Gerador de Senhas")

caracteres = "abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ!@#$%¨&*().,123456789"

numero = input("Quantidade de senhas geradas: ")
numero = int(numero)

comprimento = input("Insira o comprimento da sua senha: ")
comprimento = int(comprimento)

print("\Aqui esta sua senha: ")

for pwd in range(numero):
    senha = ''
    for c in range(comprimento):
        senha += random.choice(caracteres)
    print(senha)
