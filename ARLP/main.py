# main.py

import sys
from arlp.parser1 import Parser
from arlp.lexer import tokenize_file
from arlp.interpreter import Interpreter  

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_name>")
        return

    file_name = sys.argv[1]
    try:
        tokens = tokenize_file(file_name)
        print(tokens)
        parser = Parser(tokens)
        print("_________________________________")
        print(parser)
        ast = parser.parse()
        print("_________________________________")
        print(ast)
        interpreter = Interpreter()  
        interpreter.interpret(ast)   
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred 3adel run 2l files kamlin w dir vihm __main__ test la tensaaaaaah : {e}")

if __name__ == "__main__":
    main()
