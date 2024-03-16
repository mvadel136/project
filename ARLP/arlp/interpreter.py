# interpreter.py

from arlp.parser1 import *

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, ast):
        for statement in ast:
            self.execute_statement(statement)

    def execute_statement(self, statement):
        if isinstance(statement, VariableDeclaration):
            self.variables[statement.identifier] = self.evaluate_expression(statement.value)
        elif isinstance(statement, PrintStatement):
            print(self.evaluate_expression(statement.expression))
        elif isinstance(statement, IfStatement):
            self.execute_if_statement(statement)
        elif isinstance(statement, WhileStatement):
            self.execute_while_statement(statement)

    def execute_while_statement(self, while_statement):
        while self.evaluate_expression(while_statement.condition):
            for stmt in while_statement.body:
                self.execute_statement(stmt)


    def evaluate_expression(self, expression):
        if isinstance(expression, Expression):
            left = self.evaluate_expression(expression.left)
            right = self.evaluate_expression(expression.right)
            if expression.operator in ['+', '-', '*', '/', '%', '>', '<', '!=', '==', '>=', '<=']:
                return eval(f"{left} {expression.operator} {right}")
        elif isinstance(expression, bool):
            return expression
        elif isinstance(expression, str):
            return self.variables.get(expression, expression)
        return expression


    def execute_if_statement(self, if_statement):
        if self.evaluate_expression(if_statement.condition):
            for statement in if_statement.body:
                self.execute_statement(statement)
        else:
            for elif_condition, elif_body in if_statement.elif_bodies:
                if self.evaluate_expression(elif_condition):
                    for statement in elif_body:
                        self.execute_statement(statement)
                    return
            if if_statement.else_body:
                for statement in if_statement.else_body:
                    self.execute_statement(statement)
    def execute_while_statement(self, while_statement):
        while self.evaluate_expression(while_statement.condition):
            for stmt in while_statement.body:
                self.execute_statement(stmt)

