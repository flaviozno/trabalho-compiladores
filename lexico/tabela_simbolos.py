from lexico.tabela_transicao import Token_type


class Tabela_simbolos:
    tabela = {}

    def init(self):
        self.tabela = {}

    def inserir(self, token_tipo, lexema, valor, tipo_dado):
        self.tabela[lexema] = {
            "tipo_do_token": token_tipo,
            "lexema": lexema,
            "valor": valor,
            "tipo_do_dado": tipo_dado,
        }

    def buscar(self, lexema):
        return self.tabela.get(lexema, None)

    def listar_todos(self):
        return list(self.tabela.values())
