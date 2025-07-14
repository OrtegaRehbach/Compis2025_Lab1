import sys
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser

def main(argv):
    input_stream = FileStream(argv[1])      # Read src file as char stream
    lexer = MiniLangLexer(input_stream)     # Create a lexer for the char stream
    stream = CommonTokenStream(lexer)       # Lex the char stream into a token stream
    parser = MiniLangParser(stream)         # Create a parser for the token stream
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our MiniLang grammar, yay!

if __name__ == '__main__':
    main(sys.argv)