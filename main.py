from lexico.lex import filtered_lex
from lexico.lex import Token_type
from lexico.tabela_simbolos import Tabela_simbolos

tabela_simbolos = Tabela_simbolos()

for lexema in filtered_lex("teste.txt", tabela_simbolos):
    print(lexema)

print("----------------------------")
print(f"{tabela_simbolos.listar_todos()}")
