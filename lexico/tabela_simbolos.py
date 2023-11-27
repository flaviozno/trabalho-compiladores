from lexico.tabela_transicao import Token_type


class Tabela_simbolos:
    tabela = {}  # dicionário para armazenar informações sobre os símbolos encontrados durante a análise léxica

    def __init__(self):
        self.tabela = {}

    def inserir(self, token_tipo, lexema, valor, tipo_dado):
        self.tabela[lexema] = {
            "tipo_do_token": token_tipo,
            "lexema": lexema,
            "valor": valor,
            "tipo_do_dado": tipo_dado,
        }

    def buscar(self, lexema):  # recebe o lexema como parâmetro e retorna as informações associadas a esse lexema na tabela de símbolos. Se o lexema não estiver presente, retorna none
        return self.tabela.get(lexema, None)

    # retorna uma lista contendo todas as entradas da tabela de símbolos.
    def listar_todos(self):
        return list(self.tabela.values())
