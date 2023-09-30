from lexico.tabela_transicao import tabela
from lexico.tabela_transicao import Token_type

from lexico.reader import read


def lex(nome_arquivo):
    table = tabela()
    estado = 0
    lexema = ""
    leitor = read(nome_arquivo)

    inicio_lexema = (0, 0)
    for char in leitor:
        # print(f"LEU CHAR : {char}")

        if len(lexema) == 0:
            inicio_lexema = (char["line"], char["column"])

        if table[estado].final:
            if table[estado].look_forward:
                yield (lexema[:-1], table[estado].retorno, inicio_lexema)
                lexema = ""
                estado = 0
                inicio_lexema = (char["line"], char["column"])
            else:
                yield (lexema, table[estado].retorno, inicio_lexema)
                lexema = ""
                estado = 0
                inicio_lexema = (char["line"], char["column"])

        if not table[estado].final:
            lexema, estado, found_transition = transiciona_estado(
                table, char, estado, lexema
            )

        if not found_transition and not (table[estado].final):
            estado = -1

        if estado == -1:
            print(f'Erro no char {char} no lexema = "{lexema}" len = {len(lexema)}')
            break

        if table[estado].final:
            if table[estado].look_forward:
                yield (lexema[:-1], table[estado].retorno, inicio_lexema)
                lexema = ""
                estado = 0
                inicio_lexema = (char["line"], char["column"])
                lexema, estado, found_transition = transiciona_estado(
                    table, char, estado, lexema
                )
            else:
                yield (lexema, table[estado].retorno, inicio_lexema)
                lexema = ""
                estado = 0
                inicio_lexema = (char["line"], char["column"])


def transiciona_estado(table, char, estado, lexema):
    lexema = lexema + char["char"]
    # print(f'Estado = {estado}, char = {char}, lexema = "{lexema}", len = {len(lexema)}')

    found_transition = False

    for trans in table[estado].transicoes:
        if char["char"] in trans[0]:
            estado = trans[1]
            found_transition = True
    return lexema, estado, found_transition


def filtered_lex(nome_arquivo):
    for lexema in lex(nome_arquivo):
        if not lexema[1] == Token_type.WS:
            yield lexema
