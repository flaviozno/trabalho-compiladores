from lexico.tabela_transicao import tabela, Token_type


def find_first_lexico(tabela_transicao):
    first_sets = {}

    for estado_nome, estado in tabela_transicao.items():
        first_set = set()

        for transicao in estado.transicoes:
            caracteres_transicao, proximo_estado_nome = transicao
            for char in caracteres_transicao:
                if char != Token_type.WS:
                    first_set.add(char)
                    break

            if not estado.look_forward:
                break

        first_sets[estado_nome] = first_set

    return first_sets


def find_follow_all(tabela_transicao):
    follow_sets = {estado_nome: set() for estado_nome in tabela_transicao}

    for _ in range(len(tabela_transicao)):
        for estado_nome, estado in tabela_transicao.items():
            for transicao in estado.transicoes:
                caracteres_transicao, proximo_estado_nome = transicao
                follow_sets[proximo_estado_nome].update(find_first_follow_all(
                    tabela_transicao[proximo_estado_nome], tabela_transicao, follow_sets))

    return follow_sets


def find_first_follow_all(estado, tabela_transicao, follow_sets):
    first_set = set()

    for transicao in estado.transicoes:
        caracteres_transicao, proximo_estado_nome = transicao
        for char in caracteres_transicao:
            if char != Token_type.WS:
                first_set.add(char)
                break

        if not estado.look_forward:
            break

    if estado.look_forward:
        first_set.update(follow_sets[estado.nome])

    return first_set