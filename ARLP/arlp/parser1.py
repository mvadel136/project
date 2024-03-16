class WhileStatement:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class IfStatement:
    def __init__(self, condition, body, elif_bodies=None, else_body=None):
        self.condition = condition
        self.body = body
        self.elif_bodies = elif_bodies if elif_bodies is not None else []
        self.else_body = else_body

class ElifStatement:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class VariableDeclaration:
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class PrintStatement:
    def __init__(self, expression):
        self.expression = expression

class Expression:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def current_token(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None, None

    def parse(self):
        statements = []
        while self.current_token_index < len(self.tokens):
            statement = self.parse_statement()
            if statement:
                statements.append(statement)
        return statements

    def parse_statement(self):
        token_type, token_value = self.current_token()

        if token_type == 'IDENTIFIER':
            next_token = self.tokens[self.current_token_index + 1] if self.current_token_index + 1 < len(self.tokens) else (None, None)
            if token_value == 'طباعة':
                return self.parse_print_statement()
            elif next_token[0] == 'OPERATOR' and next_token[1] == '=':  
                return self.parse_variable_declaration()
        elif token_type == 'KEYWORD' and token_value == 'طباعة':
            return self.parse_print_statement()
        elif token_type == 'KEYWORD' and token_value == 'إذا':
            return self.parse_if_statement()
        elif token_type == 'KEYWORD' and token_value == 'مادام':
            return self.parse_while_statement()

        self.current_token_index += 1  
        return None  

    def parse_variable_declaration(self):
        identifier = self.consume_token('IDENTIFIER')
        self.consume_token('OPERATOR', '=')
        expression = self.parse_expression()
        self.consume_token('PUNCTUATION', ';')
        return VariableDeclaration(identifier, expression)

    def parse_print_statement(self):
        self.consume_token('KEYWORD', 'طباعة')
        self.consume_token('PUNCTUATION', '(')
        expression = self.parse_expression()
        self.consume_token('PUNCTUATION', ')')
        self.consume_token('PUNCTUATION', ';')
        return PrintStatement(expression)

    def consume_token(self, expected_type, expected_value=None):
        token_type, token_value = self.current_token()
        if token_type != expected_type or (expected_value is not None and token_value != expected_value):
            raise SyntaxError(f"Expected {expected_type}{' with value ' + expected_value if expected_value else ''}, but got {token_type} with value {token_value}")
        self.current_token_index += 1
        return token_value

    def parse_expression(self):
        left = self.parse_primary()
        while self.current_token() and self.current_token()[0] == 'OPERATOR':
            operator = self.consume_token('OPERATOR')
            right = self.parse_primary()
            left = Expression(left, operator, right)
        return left

    def parse_primary(self):
        token_type, token_value = self.current_token()

        if token_type in ['NUMBER_INTEGER', 'NUMBER_FLOAT', 'STRING']:
            self.current_token_index += 1
            return token_value
        elif token_type == 'IDENTIFIER':
            self.current_token_index += 1
            return token_value
        elif token_type == 'PUNCTUATION' and token_value == '(':
            self.current_token_index += 1
            expr = self.parse_expression()
            self.consume_token('PUNCTUATION', ')')
            return expr
        elif token_type == 'BOOLEAN':  
            self.current_token_index += 1
            return token_value == 'صحيح'
        else:
            raise SyntaxError(f"Expected a primary expression, got {token_type} with value '{token_value}'")
        

    def parse_if_statement(self):
        self.consume_token('KEYWORD', 'إذا')
        self.consume_token('PUNCTUATION', '(')
        condition = self.parse_expression()
        self.consume_token('PUNCTUATION', ')')
        
        self.consume_token('PUNCTUATION', '{')
        if_body = self.parse_block()
        
        elif_bodies = []
        else_body = None
        while self.current_token()[1] in ['وإلا إذا', 'وإلا']:
            if self.current_token()[1] == 'وإلا إذا':
                self.consume_token('KEYWORD', 'وإلا إذا')
                self.consume_token('PUNCTUATION', '(')
                elif_condition = self.parse_expression()
                self.consume_token('PUNCTUATION', ')')
                self.consume_token('PUNCTUATION', '{')
                elif_body = self.parse_block()
                elif_bodies.append((elif_condition, elif_body))
            elif self.current_token()[1] == 'وإلا':
                self.consume_token('KEYWORD', 'وإلا')
                self.consume_token('PUNCTUATION', '{')
                else_body = self.parse_block()
                break

        return IfStatement(condition, if_body, elif_bodies, else_body)

    def parse_block(self):
        statements = []
        while not self.current_token() == ('PUNCTUATION', '}'):
            statements.append(self.parse_statement())
        self.consume_token('PUNCTUATION', '}')
        return statements
    
    def parse_while_statement(self):
        self.consume_token('KEYWORD', 'مادام')
        self.consume_token('PUNCTUATION', '(')
        condition = self.parse_expression()
        self.consume_token('PUNCTUATION', ')')
        
        self.consume_token('PUNCTUATION', '{')
        body = self.parse_block()
        
        return WhileStatement(condition, body)

