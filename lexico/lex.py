from lexico.tabela_transicao import tabela
from lexico.tabela_transicao import Token_type
from lexico.tabela_simbolos import Tabela_simbolos

from lexico.reader import read

# Utiliza uma tabela de transição para determinar o tipo de token correspondente a cada lexema.
# Quando encontra um lexema completo, gera uma tupla contendo o lexema, o tipo de token e a posição inicial do lexema.
# Lida com casos de look-forward (quando é necessário retroceder um caractere ao encontrar um token final que se parece com o início de outro token).
# Se ocorrer um erro no reconhecimento do token, imprime uma mensagem e encerra o processo.


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
            print(
                f'Erro no char {char} no lexema = "{lexema}" len = {len(lexema)}')
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

# Atualiza o estado com base na tabela de transição e retorna um tupla contendo o lexama atualizado, novo estado e um indicador de se foir encontrada a transicao


def transiciona_estado(table, char, estado, lexema):
    lexema = lexema + char["char"]
    # print(f'Estado = {estado}, char = {char}, lexema = "{lexema}", len = {len(lexema)}')

    found_transition = False

    for trans in table[estado].transicoes:
        if char["char"] in trans[0]:
            estado = trans[1]
            found_transition = True
    return lexema, estado, found_transition

# Insere os lexemas na tabela de símbolos ignorando os ws


def filtered_lex(nome_arquivo, tabela_simbolo):

    palavras_reservadas = {
        'if': Token_type.IF,
        'else': Token_type.ELSE,
        'while': Token_type.WHILE,
        'for': Token_type.FOR,
        'int': Token_type.INT,
        'float': Token_type.FLOAT,
        'return': Token_type.RETURN,
        'programa': Token_type.PROGRAMA,
    }

    for lexema in lex(nome_arquivo):
        if not lexema[1] == Token_type.WS:
            if palavras_reservadas.get(lexema[0].lower()):
                novo_lexema = (lexema[0], palavras_reservadas.get(
                    lexema[0].lower())) + lexema[2:]
                yield insere_tabela(
                    lexema=novo_lexema, tabela=tabela_simbolo, is_reserved=True)
            else:
                insere_tabela(
                    lexema=lexema, tabela=tabela_simbolo, is_reserved=False)
                yield lexema

# Insere os lexemas na tabela de símbolos (tabela) com base em seu tipo de token


def insere_tabela(lexema, tabela: Tabela_simbolos, is_reserved):
    tipo = lexema[1]
    lex = lexema[0]
    
    if is_reserved:
        tabela.inserir(token_tipo=tipo, lexema=lex, tipo_dado=tipo, valor=None)

    if tipo in [Token_type.ID]:
        tabela.inserir(token_tipo=tipo, lexema=lex,
                       tipo_dado="ID", valor=None)

    if tipo in [
        Token_type.NUMERO_INT,
        Token_type.NUMERO_EXP,
        Token_type.NUMERO_FLOAT,
        Token_type.CHARS,
    ]:
        print("Numero adicionado na tabela de simbolos")
        tabela.inserir(token_tipo=tipo, lexema=lex, valor=None, tipo_dado=None)
