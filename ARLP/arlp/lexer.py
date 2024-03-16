import re

TOKEN_TYPES = {
    'KEYWORD': r'(إذا|وإلا إذا|وإلا|مادام|لكل|في|توقف|تواصل|تمرر|ارجع|تعريف|فارغ|طباعة|ادراج)',
    'BOOLEAN': r'(صحيح|خطأ)',
    'IDENTIFIER': r'[ء-ي][ء-ي0-9_]*',  
    'NUMBER_INTEGER': r'\d+',
    'NUMBER_FLOAT': r'\d+\.\d+',
    'LIST': r'\[(.*?)\]',  
    'STRING': r'"(?:\\"|[^"])*"',  
    # 'OPERATOR': r'[+\-*/%=]|==|!=|>=|<=|>|<|و|أو|ليس|هو|ليس هو|في|ليس في',
    'OPERATOR': r'==|!=|>=|<=|و|أو|ليس|هو|ليس هو|في|ليس في|[+\-*/%=><]',

    'ASSIGNMENT': r'=',
    'PUNCTUATION': r'[(){}[\],.:;@`؛]',  
    'WHITESPACE': r'\s+'
}



TOKEN_REGEX = re.compile('|'.join('(?P<{}>{})'.format(token_type, pattern) for token_type, pattern in TOKEN_TYPES.items()), re.IGNORECASE)


def tokenize(code):
    tokens = []
    for match in TOKEN_REGEX.finditer(code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'WHITESPACE':
            tokens.append((token_type, token_value))
    return tokens

def tokenize_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
        return tokenize(code)


if __name__ == '__main__':
    file_path = '../test1.arpl'
    tokens = tokenize_file(file_path)
    for token in tokens:
        print(token)
