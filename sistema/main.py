import processamento as funcao

print("Sistema automatico de acompanhamento academico")

dados = [
    ("Bruno Pezzolato", [1, 10, "10", ""]),
    ("Ana Lério", [9, 10, 8]),
    ("São Marcos", [1, 10, "10", ""]),
    ("Bruno Pezzolato2", [9, 10, 8, None, 8]),
]

dadosParaMedia, alunosRetirados = funcao.limpezaDosDados(dados)