def read(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            line_count = 0
            column_count = 0
            for linha in arquivo:
                line_count += 1
                for char in linha:
                    column_count += 1
                    yield {"char": char, "line": line_count, "column": column_count}
                column_count = 0
            line_count += 1
            yield {"char": "/n", "line": line_count, "column": column_count}
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
