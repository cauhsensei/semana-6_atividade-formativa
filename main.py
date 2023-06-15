estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []


def apresentar_menu_principal():
    print('\n###############')
    print("\nMenu Principal:")
    print('\n###############\n')
    print("1. Gerenciar estudantes")
    print("2. Gerenciar professores")
    print("3. Gerenciar disciplinas")
    print("4. Gerenciar turmas")
    print("5. Gerenciar matrículas")
    print("6. Sair")


def apresentar_menu_operacoes(tipo_dado):
    print('\n#################################')
    print("\nMenu de Operações para {}:".format(tipo_dado))
    print('\n#################################\n')
    print("1. Incluir")
    print("2. Listar")
    print("3. Editar")
    print("4. Excluir")
    print("5. Voltar ao menu principal")


def incluir_dado(dados, tipo_dado, campos):
    novo_dado = {}
    for campo, tipo in campos.items():
        valor = input("Digite {}: ".format(campo))
        if tipo == int:
            valor = int(valor)
        novo_dado[campo] = valor

    if tipo_dado == "Turmas" and verificar_codigo_existente(turmas, novo_dado["Código da turma"]):
        print("Já existe uma turma com esse código. Inclusão cancelada.")
        return

    if tipo_dado == "Matrículas" and verificar_codigo_existente(matriculas, novo_dado["Código da turma"]):
        print("Já existe uma matrícula com esse código. Inclusão cancelada.")
        return

    dados.append(novo_dado)
    print("\n{} adicionado com sucesso!".format(tipo_dado))


def listar_dados(dados, tipo_dado):
    if len(dados) == 0:
        print("Não há {} cadastrados.".format(tipo_dado))
    else:
        print("\n{} cadastrados:".format(tipo_dado))
        for dado in dados:
            print("- Código: {}".format(dado["Código"]))
            for campo, valor in dado.items():
                if campo != "Código":
                    print("  {}: {}".format(campo.capitalize(), valor))
            print("")
        input("Aperte Enter para voltar")


def excluir_dado(dados, tipo_dado):
    codigo = int(input("Digite o código do {} a ser excluído: ".format(tipo_dado)))
    for dado in dados:
        if dado["Código"] == codigo:
            dados.remove(dado)
            print("{} excluído com sucesso!".format(tipo_dado))
            break
    else:
        print("{} não encontrado.".format(tipo_dado))


def editar_dado(dados, tipo_dado, campos):
    codigo = int(input("Digite o código do {} a ser editado: ".format(tipo_dado)))
    for dado in dados:
        if dado["Código"] == codigo:
            for campo, tipo in campos.items():
                novo_valor = input("Digite novo valor para {}: ".format(campo))
                if tipo == int:
                    novo_valor = int(novo_valor)
                dado[campo] = novo_valor
            print("{} editado com sucesso!".format(tipo_dado))
            break
    else:
        print("{} não encontrado.".format(tipo_dado))


def verificar_codigo_existente(dados, codigo):
    for dado in dados:
        if dado["Código"] == codigo:
            return True
    return False


def gerenciar_dados(dados, tipo_dado, campos):
    while True:
        apresentar_menu_operacoes(tipo_dado)
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            incluir_dado(dados, tipo_dado, campos)
        elif opcao == "2":
            listar_dados(dados, tipo_dado)
        elif opcao == "3":
            editar_dado(dados, tipo_dado, campos)
        elif opcao == "4":
            excluir_dado(dados, tipo_dado)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")


def gerenciar_estudantes():
    gerenciar_dados(estudantes, "Estudantes", {"Código": int, "Nome": str, "CPF": str})


def gerenciar_professores():
    gerenciar_dados(professores, "Professores", {"Código": int, "Nome": str, "CPF": str})


def gerenciar_disciplinas():
    gerenciar_dados(disciplinas, "Disciplinas", {"Código": int, "Nome": str})


def gerenciar_turmas():
    gerenciar_dados(turmas, "Turmas", {"Código": int, "Código do professor": int, "Código da disciplina": int})


def gerenciar_matriculas():
    gerenciar_dados(matriculas, "Matrículas", {"Código da turma": int, "Código do estudante": int})


def menu_principal():
    while True:
        apresentar_menu_principal()
        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            gerenciar_estudantes()
        elif opcao == "2":
            gerenciar_professores()
        elif opcao == "3":
            gerenciar_disciplinas()
        elif opcao == "4":
            gerenciar_turmas()
        elif opcao == "5":
            gerenciar_matriculas()
        elif opcao == "6":
            print("Encerrando aplicação")
            break
        else:
            print("Opção inválida. Por favor, selecione uma opção válida.")


menu_principal()
