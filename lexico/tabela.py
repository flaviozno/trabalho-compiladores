class Estado:
    def __init__(self, nome, final=False, transicoes=[], look_forward=False):
        self.nome = nome
        self.final = final
        self.transicoes = transicoes
        self.look_forward = look_forward

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
        Estado(nome=0, transicoes=[
               ("\\s" or "\\n" or "\\t", 1), ("{", 2), (letras, 4), (numeros, 6), ("'", 15), (":", 17), (";", 20), (",", 21), ("=", 22), ("<", 23), (">", 26), ("!", 29), ("^", 31), ("+", 32), ("-", 33), ("*", 34), ("/", 35), ("(", 36), (")", 37)]),
        Estado(nome=1, final=True),
        Estado(nome=2, transicoes=[("}", 3), (ascii_characters, 2)]),
        Estado(nome=3, final=True),
        Estado(
            nome=4,
            transicoes=[
                (letras + numeros, 4),
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
        Estado(nome=5, final=True, look_forward=True),
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
            ],
        ),
        Estado(nome=7, final=True, look_forward=True),
        Estado(nome=8, transicoes=[(numeros, 9)]),
        Estado(
            nome=9,
            transicoes=[
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
                ("".join(char for char in ascii_characters if char not in numeros), 13),
            ],
        ),
        Estado(nome=13, final=True, look_forward=True),
        Estado(nome=14, final=True, look_forward=True),
        Estado(nome=15, transicoes=[(".", 15), ("'", 16)]),
        Estado(nome=16, final=True),
        Estado(
            nome=17,
            transicoes=[
                ("=", 19),
                ("".join(char for char in ascii_characters if char not in "="), 18),
            ],
        ),
        Estado(nome=18, final=True, look_forward=True),
        Estado(nome=19, final=True),
        Estado(nome=20, final=True),
        Estado(nome=21, final=True),
        Estado(nome=22, final=True),
        Estado(
            nome=23,
            transicoes=[
                ("=", 24),
                ("".join(char for char in ascii_characters if char not in ">="), 25),
            ],
        ),
        Estado(nome=24, final=True),
        Estado(nome=25, final=True, look_forward=True),
        Estado(
            nome=26,
            transicoes=[
                ("=", 27),
                ("".join(char for char in ascii_characters if char not in "="), 28),
            ],
        ),
        Estado(nome=27, final=True),
        Estado(nome=28, final=True, look_forward=True),
        Estado(nome=29, transicoes=[("=", 30)]),
        Estado(nome=30, final=True),
        Estado(nome=31, final=True),
        Estado(nome=32, final=True),
        Estado(nome=33, final=True),
        Estado(nome=34, final=True),
        Estado(nome=35, final=True),
        Estado(nome=36, final=True),
        Estado(nome=37, final=True),
    ]

    return valida_tabela(tabela_transicao)


def valida_tabela(tabela):
    table = {}

    for elem in tabela:
        table[elem.nome] = elem

    for k, v in table.items():
        for trans in v.transicoes:
            if trans[1] not in table:
                raise Exception(
                    f"TRANSIÇÃO INVALIDA EM [{v}] NA TRANSICAO {trans}")

    return table
