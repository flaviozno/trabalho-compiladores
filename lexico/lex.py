from tabela import tabela

from reader import read


def lex(nome_arquivo):
    table = tabela()
    estado = 0
    lexema = ""
    for char in read(nome_arquivo):
        lexema, estado, found_transition = transiciona_estado(
            table, char, estado, lexema
        )

        if not found_transition:
            estado = -1

        if estado == -1:
            print(f"Erro no char {char} no lexema = {lexema}")
            break

        if table[estado].final:
            if table[estado].look_forward:
                yield lexema[:-1]
                lexema = ""
                estado = 0
                lexema, estado, found_transition = transiciona_estado(
                    table, char, estado, lexema
                )
            else:
                yield lexema
                lexema = ""
                estado = 0


def transiciona_estado(table, char, estado, lexema):
    lexema = lexema + char["char"]
    # print(f"Estado = {estado}, char = {char}, lexema = {lexema}")

    found_transition = False

    for trans in table[estado].transicoes:
        if char["char"] in trans[0]:
            estado = trans[1]
            found_transition = True

    return lexema, estado, found_transition


for lexema in lex("teste.txt"):
    print(lexema)
