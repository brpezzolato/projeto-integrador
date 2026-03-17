def limpezaDosDados(dados):
    print("\nLimpando os dados...")

    alunosParaMedia = []
    alunosRetirados = []

    for cada in dados:
        dadosValidos = True

        if len(cada[1]) == 0:
            dadosValidos = False

        for cadaNota in cada[1]:
            if type(cadaNota) != float and type(cadaNota) != int:
                dadosValidos = False

        if dadosValidos == True:
            alunosParaMedia.append(cada)
        else:
            alunosRetirados.append(cada)

    return alunosParaMedia, alunosRetirados


def calculoMedia(dados):
    print("Calculando média dos alunos...")

    dadosComMedia = []

    for cada in dados:
        soma = 0

        for cadaNota in cada[1]:
            soma += cadaNota

        media = soma / len(cada[1])
        novoObjto = (cada[0], cada[1], media)
        dadosComMedia.append(novoObjto)

    return dadosComMedia


def atribuirStatus(dados):
    print("Atribuindo status dos alunos...")

    alunosComStatus = []
    medias = []

    for cada in dados:
        medias.append(cada[2])

    maior = max(medias)

    for cada in dados:
        if cada[2] == maior:
            novoObjto = (cada[0], cada[1], cada[2], "Top Student")
            alunosComStatus.append(novoObjto)
        elif cada[2] < 7.0:
            novoObjto = (cada[0], cada[1], cada[2], "Recuperação")
            alunosComStatus.append(novoObjto)
        else:
            novoObjto = (cada[0], cada[1], cada[2], "Situação Normal")
            alunosComStatus.append(novoObjto)

    return alunosComStatus


def alunosRecuperacao(dados):
    print("Filtrando alunos de recuperação...")

    alunosEmRecuperacao = []

    for cada in dados:
        if cada[2] < 7.0:
            alunosEmRecuperacao.append(cada)

    return alunosEmRecuperacao


def definirTopStudent(dados):
    print("Definindo o Top Student...")

    topStudent = []

    for cada in dados:
        if cada[3] == "Top Student":
            topStudent.append(cada)

    return topStudent


def gerarRelatorio(alunosRetirados, alunosComStatus, alunosDeRecuperacao, topStudent):
    print("Gerando relatório...")

    with open("sistema/relatorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(
            "Relatório de desempenho acadêmico do SENAI\n\n" + "-" * 100 + "\n\n"
        )

        arquivo.write(f"- Alunos que estão de recuperação (Média < 7.0): \n")
        for cada in alunosDeRecuperacao:
            arquivo.write(
                f"    Nome do aluno: {cada[0]} - Notas: {cada[1]} - Média: {cada[2]} - Situação: {cada[3]}\n"
            )
        arquivo.write(f"\n* Quantidade de alunos({len(alunosDeRecuperacao)}) *\n")

        arquivo.write("\n" + "-" * 100 + "\n\n")

        arquivo.write("- Alunos que estão de situação normal (Média >= 7.0): \n")
        count = 0
        for cada in alunosComStatus:
            if cada[3] == "Situação Normal":
                arquivo.write(
                    f"    Nome do aluno: {cada[0]} - Média: {cada[2]} - Situação: {cada[3]}\n"
                )
                count += 1
        arquivo.write(f"\n* Quantidade de alunos({count}) *\n")

        arquivo.write("\n" + "-" * 100 + "\n\n")

        arquivo.write("- Top Student (Maior média registrada): \n")
        for cada in topStudent:
            arquivo.write(
                f"    Nome do aluno: {cada[0]} - Média: {cada[2]} - Situação: {cada[3]}\n"
            )
        arquivo.write(f"\n* Quantidade de alunos({len(topStudent)}) *\n")

        arquivo.write("\n" + "-" * 100 + "\n\n")

        arquivo.write(
            "- Alunos que precisam de revisão de nota (sao aceitos valores inteiros ou decimais): \n"
        )
        for cada in alunosRetirados:
            arquivo.write(f"    Nome do aluno: {cada[0]} - Notas: {cada[1]}\n")
        arquivo.write(f"\n* Quantidade de alunos({len(alunosRetirados)}) *\n")
