import sys
from antlr4 import *
from LittleDuckLexer import LittleDuckLexer
from LittleDuckParser import LittleDuckParser

# Lee archivo .ld y parsea

def main(file_path):
    # Abre el archivo fuente
    input_stream = FileStream(file_path)

    # Lexer: convierte texto a tokens
    lexer = LittleDuckLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Parser: analiza tokens y construye árbol sintáctico
    parser = LittleDuckParser(token_stream)

    # Empieza desde la regla 'programa' que es la raíz
    tree = parser.programa()

    print("El programa es sintácticamente válido.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python run_littleduck.py archivo.ld")
        sys.exit(1)

    main(sys.argv[1])
