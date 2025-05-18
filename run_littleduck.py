import sys
from antlr4 import *
from LittleDuckLexer import LittleDuckLexer
from LittleDuckParser import LittleDuckParser
from LittleDuckParserVisitor import LittleDuckParserVisitor
from SemanticAnalizer import SemanticAnalyzer, SemanticError
from antlr4.error.ErrorListener import ErrorListener

# Custom Error Listener
class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.had_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error sintáctico en línea {line}, columna {column}: {msg}")
        self.had_error = True

# Lee archivo .ld y parsea
def main(file_path):
    # Abre el archivo fuente
    input_stream = FileStream(file_path)

    # Lexer: convierte texto a tokens
    lexer = LittleDuckLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Parser: analiza tokens y construye árbol sintáctico
    parser = LittleDuckParser(token_stream)

    # Agrega nuestro listener de errores sintácticos personalizados
    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Empieza desde la regla 'programa'
    tree = parser.programa()

    if error_listener.had_error:
        print("El programa tiene errores sintácticos.")
    else:
        print("El programa es sintácticamente válido.")

        # Análisis semántico
        analyzer = SemanticAnalyzer()
        try:
            analyzer.visit(tree)
            print("Análisis semántico completado sin errores.")
        except SemanticError as e:
            print(f"Error semántico: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python run_littleduck.py archivo.ld")
        sys.exit(1)

    main(sys.argv[1])