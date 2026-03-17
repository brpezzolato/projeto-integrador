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