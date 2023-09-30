from enum import Enum


class Token_type(Enum):
    WS = 1
    ID = 2
    NUMERO_INT = 3
    NUMERO_EXP = 4
    NUMERO_FLOAT = 5
    CHARS = 6
    DOIS_PONTOS = 7
    ATRIBUICAO = 8
    PONTO_E_VIRGULA = 9
    VIRGULA = 10
    RELOP_EQ = 11
    RELOP_NE = 12
    RELOP_GE = 13
    RELOP_GT = 14
    RELOP_LE = 15
    RELOP_LT = 16
    ARIOP_SUM = 17
    ARIOP_SUB = 18
    ARIOP_MUL = 19
    ARIOP_DIV = 20
    ARIOP_EXP = 21
    ABRE_PARENTESES = 22
    FECHA_PARENTESES = 23


class Estado:
    def __init__(
        self, nome, final=False, transicoes=[], look_forward=False, retorno=None
    ):
        self.nome = nome
        self.final = final
        self.transicoes = transicoes
        self.look_forward = look_forward
        self.retorno = retorno

    def adicionar_transicao(self, caractere, proximo_estado):
        self.transicoes.append((caractere, proximo_estado))

    def __str__(self):
        estado_final = "Final" if self.final else "Não Final"
        transicoes_str = ", ".join(
            [f"({char}, {estado})" for char, estado in self.transicoes]
        )
        return f"Nome: {self.nome}, {estado_final}, Transições: [{transicoes_str}]"


def tabela():
    ascii_characters = "".join(chr(i) for i in range(32, 127))
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
    numeros = "0123456789"

    tabela_transicao = [
        Estado(
            nome=0,
            transicoes=[
                (" " + "\n", 1),
                ("{", 2),
                (letras, 4),
                (numeros, 6),
                ("'", 15),
                (":", 17),
                (";", 20),
                (",", 21),
                ("=", 22),
                ("<", 23),
                (">", 26),
                ("!", 29),
                ("^", 31),
                ("+", 32),
                ("-", 33),
                ("*", 34),
                ("/", 35),
                ("(", 36),
                (")", 37),
            ],
        ),
        Estado(nome=1, final=True, retorno=Token_type.WS),
        Estado(
            nome=2,
            transicoes=[
                ("}", 3),
                ("".join(char for char in ascii_characters if char not in ("}")), 2),
                ("\n", 2),
            ],
        ),
        Estado(nome=3, final=True, retorno=Token_type.WS),
        Estado(
            nome=4,
            transicoes=[
                (letras + numeros, 4),
                ("\n", 5),
                (
                    "".join(
                        char
                        for char in ascii_characters
                        if char not in (letras + numeros)
                    ),
                    5,
                ),
            ],
        ),
        Estado(nome=5, final=True, look_forward=True, retorno=Token_type.ID),
        Estado(
            nome=6,
            transicoes=[
                (numeros, 6),
                (".", 8),
                (
                    "".join(
                        char for char in ascii_characters if char not in (numeros + ".")
                    ),
                    7,
                ),
                ("\n", 7),
            ],
        ),
        Estado(nome=7, final=True, look_forward=True, retorno=Token_type.NUMERO_INT),
        Estado(nome=8, transicoes=[(numeros, 9)]),
        Estado(
            nome=9,
            transicoes=[
                ("\n", 14),
                (numeros, 9),
                ("E", 10),
                (
                    "".join(
                        char for char in ascii_characters if char not in (numeros + "E")
                    ),
                    14,
                ),
            ],
        ),
        Estado(nome=10, transicoes=[("-", 11), (numeros, 12)]),
        Estado(nome=11, transicoes=[(numeros, 12)]),
        Estado(
            nome=12,
            transicoes=[
                (numeros, 12),
                (
                    "".join(
                        char for char in ascii_characters if char not in (numeros + ".")
                    ),
                    13,
                ),
                ("\n", 13),
            ],
        ),
        Estado(nome=13, final=True, look_forward=True, retorno=Token_type.NUMERO_EXP),
        Estado(nome=14, final=True, look_forward=True, retorno=Token_type.NUMERO_FLOAT),
        Estado(
            nome=15,
            transicoes=[
                ("\n", 15),
                ("'", 16),
                ("".join(char for char in ascii_characters if char not in "'"), 15),
            ],
        ),
        Estado(nome=16, final=True, retorno=Token_type.CHARS),
        Estado(
            nome=17,
            transicoes=[
                ("\n", 18),
                ("=", 19),
                ("".join(char for char in ascii_characters if char not in "="), 18),
            ],
        ),
        Estado(nome=18, final=True, look_forward=True, retorno=Token_type.DOIS_PONTOS),
        Estado(nome=19, final=True, retorno=Token_type.ATRIBUICAO),
        Estado(nome=20, final=True, retorno=Token_type.PONTO_E_VIRGULA),
        Estado(nome=21, final=True, retorno=Token_type.VIRGULA),
        Estado(nome=22, final=True, retorno=Token_type.RELOP_EQ),
        Estado(
            nome=23,
            transicoes=[
                ("\n", 25),
                ("=", 24),
                ("".join(char for char in ascii_characters if char not in ">="), 25),
            ],
        ),
        Estado(nome=24, final=True, retorno=Token_type.RELOP_LE),
        Estado(nome=25, final=True, look_forward=True, retorno=Token_type.RELOP_LT),
        Estado(
            nome=26,
            transicoes=[
                ("\n", 28),
                ("=", 27),
                ("".join(char for char in ascii_characters if char not in "="), 28),
            ],
        ),
        Estado(nome=27, final=True, retorno=Token_type.RELOP_GE),
        Estado(nome=28, final=True, look_forward=True, retorno=Token_type.RELOP_GT),
        Estado(nome=29, transicoes=[("=", 30)]),
        Estado(nome=30, final=True, retorno=Token_type.RELOP_NE),
        Estado(nome=31, final=True, retorno=Token_type.ARIOP_EXP),
        Estado(nome=32, final=True, retorno=Token_type.ARIOP_SUM),
        Estado(nome=33, final=True, retorno=Token_type.ARIOP_SUB),
        Estado(nome=34, final=True, retorno=Token_type.ARIOP_MUL),
        Estado(nome=35, final=True, retorno=Token_type.ARIOP_DIV),
        Estado(nome=36, final=True, retorno=Token_type.ABRE_PARENTESES),
        Estado(nome=37, final=True, retorno=Token_type.FECHA_PARENTESES),
    ]

    return valida_tabela(tabela_transicao)


def valida_tabela(tabela):
    table = {}

    for elem in tabela:
        table[elem.nome] = elem

    for k, v in table.items():
        for trans in v.transicoes:
            if trans[1] not in table:
                raise Exception(f"TRANSIÇÃO INVALIDA EM [{v}] NA TRANSICAO {trans}")

    return table
