from lexico.reader import read

arquivo = "teste.txt"

chars = read(arquivo)

for char in chars:
    print(char)
