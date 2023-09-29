from lexico.reader import read

arquivo = "teste.txt"

chars = read(arquivo)

for char in chars:
    if char == "\n":
        print("\\n")
    elif char == "\t":
        print("\\t")
    elif char == " ":
        print("\\s")
    else:
        print(char)
