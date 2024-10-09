def saudacao(nome):
    print(f"Olá, {nome}!")


print("\n Chamando a função saudação: ")
saudacao("Alice")
saudacao("Bob")


def quadrado(numero):
    resultado = numero ** 2
    return resultado


print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado: ", resultado_quadrado)


def soma(n1, n2):
    resultado = n1 + n2
    return resultado


print("Chamando a função Soma: ")
numero1 = 10
numero2 = 40

soma_n1_n2 = soma(numero1, numero2)
print("Resultado de %s + %s = %s", numero1, numero2, soma_n1_n2)
