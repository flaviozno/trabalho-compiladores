from tabela import tabela

from reader import read


def lex(nome_arquivo):
    table = tabela()
    estado = 1
    lexema = ""
    for char in read(nome_arquivo):
        lexema = lexema + char["char"]

        print(f"Estado = {estado}, char = {char}, lexema = {lexema}")

        found_transition = False

        for trans in table[estado].transicoes:
            if char["char"] in trans[0]:
                estado = trans[1]
                found_transition = True

        if not found_transition:
            estado = -1

        if estado == -1:
            print(f"Erro no char {char}")
            break

        if table[estado].final:
            print(f"reconheci lexema = {lexema} ")
            lexema = ""
            estado = 1


lex("teste.txt")
