class Estado:
    def __init__(self, nome, final=False, transicoes=[]):
        self.nome = nome
        self.final = final
        self.transicoes = transicoes

    def adicionar_transicao(self, caractere, proximo_estado):
        self.transicoes.append((caractere, proximo_estado))

    def __str__(self):
        estado_final = "Final" if self.final else "Não Final"
        transicoes_str = ", ".join(
            [f"({char}, {estado})" for char, estado in self.transicoes]
        )
        return f"Nome: {self.nome}, {estado_final}, Transições: [{transicoes_str}]"


def tabela():
    tabela_transicao = [
        Estado(nome=1, transicoes=[("cb", 2), ("d", 3)]),
        Estado(nome=2, transicoes=[("c", 3)]),
        Estado(nome=3, transicoes=[("c", 4)]),
        Estado(nome=4, transicoes=[("c", 5)]),
        Estado(nome=5, transicoes=[("c", 1), ("d", 6)]),
        Estado(nome=6, final=True, transicoes=[("c", 5)]),
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
