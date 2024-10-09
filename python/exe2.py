lista1 = []
nome = input("Seu nome? ")
altura = float(input("Sua altura? "))
peso = float(input("Peso? "))
imc = (altura * altura) / peso


dict1 = {"nome":nome, "altura":altura, "peso":peso, "imc":imc}
lista1.append(dict1)
lista1.append(dict1)

print("Nome: ", lista1[0]["nome"],"\n", "IMC", lista1[0]["imc"])