from lexico.reader import read

ascii_characters = "".join(chr(i) for i in range(32, 127))
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"
res = "".join(char for char in ascii_characters if char not in letras)
print(res)
