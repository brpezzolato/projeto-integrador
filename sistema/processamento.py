def limpezaDosDados(dados):
    print("Limpando os dados...")

    alunosParaMedia = []
    alunosRetirados = []

    for cada in dados:
        for cadaNota in cada[1]:
            print(type(cadaNota))
            if type(cadaNota) != float or type(cadaNota) != int:
                alunosRetirados.append(cada)
                break
            else:
                alunosParaMedia.append(cada)

    return alunosParaMedia, alunosRetirados
