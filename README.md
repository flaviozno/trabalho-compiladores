# Trabalho Compiladores

Para ver o vídeo explicando como buildar e rodar o compilador acesse pelo seguinte link:
[Vídeo explicativo](https://ufubr-my.sharepoint.com/:v:/g/personal/daniel_dias_ufu_br/EfD9dQL1VxNNvxOAHpVTedkB1RmckZcTZimjixsuFJPgwQ?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0RpcmVjdCJ9fQ&e=rgjlM6) obs.: Precisa estar logado em uma conta do domínio UFU para acessar o vídeo

### Operating System
- Windows

### Language
- Python


## Creating the Virtual Environment

- Download and install Python:

    [Python 3.11.3](https://www.python.org/downloads/release/python-3113/) - Check ADD TO PATH if you're on a Windows machine

- Run the following command to create a virtual environment named venv:

      python -m venv venv

- Activate the virtual environment using the command:

      .\venv\Scripts\activate

## Installing Dependencies

- Install the dependencies listed in the `requirements.txt` file using the following command:

      pip install -r requirements.txt

## Compilling
- Compile the virtual environment and activate it by running the following command:

        ./compiler.sh $FILE_NAME
        