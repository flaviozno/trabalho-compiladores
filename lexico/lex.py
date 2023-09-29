from tabela import tabela


def palavra():
    yield "c"
    yield "c"
    yield "c"
    yield "c"
    yield "d"


table = tabela()
estado = 1

for char in palavra():
    print(f"Estado = {estado}, char {char}")
    if estado == -1:
        print(f"Erro no char {char}")
        break
    for trans in table[estado].transicoes:
        if char in trans[0]:
            estado = trans[1]

    if table[estado].final:
        print("reconheci")
