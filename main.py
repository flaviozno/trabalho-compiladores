from lexico.reader import read

my_str = "Olá, mundo!\nComo vai?\n"
char_to_check = "\n"

if char_to_check in my_str:
    print(f"'{char_to_check}' encontrado na string.")
else:
    print(f"'{char_to_check}' não encontrado na string.")
