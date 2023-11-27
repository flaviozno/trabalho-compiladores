from lexico.lex import filtered_lex
from lexico.lex import Token_type
from lexico.tabela_simbolos import Tabela_simbolos
from sintatico.sintatica import find_first_lexico, find_follow_all
from lexico.tabela_transicao import tabela

tabela_simbolos = Tabela_simbolos()
tabela_transicao_lexico = tabela()
first_sets_lexico = find_first_lexico(tabela_transicao_lexico)
follow_sets_lexico = find_follow_all(tabela_transicao_lexico)

for lexema in filtered_lex("teste.txt", tabela_simbolos):
    pass

print("-----------------------------------------")
print("TABELA DE SÍMBOLOS: ")
print(f"{tabela_simbolos.listar_todos()}")
# print("-----------------------------------------")
# print("\n\nSINTÁTICA: ")
# print("Conjuntos First para o analisador léxico:")
# for estado_nome, first_set in first_sets_lexico.items():
#     estado = tabela_transicao_lexico[estado_nome]
#     if first_set:
#         print(f"Estado {estado}: {first_set}")
# print("\n\nConjuntos Follow para todos os estados:")
# for estado_nome, follow_set in follow_sets_lexico.items():
#     estado = tabela_transicao_lexico[estado_nome]
#     if follow_set:
#         print(f"Estado {estado}: {follow_set}")
