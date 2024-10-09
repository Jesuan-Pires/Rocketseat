def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return


def vizualizar_tarefas(tarefas):
    print("Lista de tarefas: ")
    for i, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{i + 1}. [{status}] {nome_tarefa}")


def atualizar_tarefas(tarefas, indice, novo_nome_tarefa):
    if indice >= 0 and indice < len(tarefas):
        tarefas[indice]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice + 1} atualizada para {novo_nome_tarefa}")
    else:
        indice = indice + 1
        print(f"A tarefa {indice} não existe!")
    return


def completar_tarefa(tarefas, indice):
    indice_tarefa_ajustado = int(indice) - 1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice} marcado como ajustado.")


def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"] == True:
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas!")
    return


tarefas = []
while True:
    print("\nMenu Genrenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "6":
        print("Programa Finalizado!")
        break
    elif escolha == "1":
        nome_tarefa = input(
            "Entre com o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        vizualizar_tarefas(tarefas)
    elif escolha == "3":
        print("Qual tarefa deseja atualizar? ")
        vizualizar_tarefas(tarefas)
        indice = int(input("Escolha o numero referente a tarefa: "))
        indice -= 1
        novo_nome_tarefa = input("Entre com o novo nome da tarefa: ")
        atualizar_tarefas(tarefas, indice, novo_nome_tarefa)
    elif escolha == "4":
        vizualizar_tarefas(tarefas)
        indice = input("Qual tarefa deseja marcar como completa? ")
        completar_tarefa(tarefas, indice)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        vizualizar_tarefas(tarefas)
    else:
        break
