import processamento as funcao

print("Sistema automatico de acompanhamento academico")

dados = [
    ("Bruno Pezzolato", [1, 10, "10", ""]),
    ("Ana Lério", [9, 10, 8]),
    ("Pezzolato Bruno", [9, 10, 8]),
    ("São Marcos", [1, 10, "10", ""]),
    ("Bruno Pezzolato2", [10, 9, 8, 1, 2]),
    ("Bruno Pezzolato3", [10, 9, 7]),
]

dadosParaMedia, alunosRetirados = funcao.limpezaDosDados(dados)
dadosComMedia = funcao.calculoMedia(dadosParaMedia)
alunosComStatus = funcao.atribuirStatus(dadosComMedia)
alunosDeRecuperacao = funcao.alunosRecuperacao(alunosComStatus)
topStudent = funcao.topStudent(alunosComStatus)