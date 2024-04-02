import ply.lex as lex

# Definición de tokens
tokens = (
    'RESERVADA',
    'NUMERO',
    'PUNTO_Y_COMA',
    'MAYOR_QUE',
    'PARENTESIS_APERTURA',
    'PARENTESIS_CIERRE',
    'CORCHETE_APERTURA',
    'CORCHETE_CIERRE',
    'COMILLA',
    'IDENTIFICADOR',
)

# Expresiones regulares para tokens simples
t_PUNTO_Y_COMA = r';'
t_PARENTESIS_APERTURA = r'\('
t_PARENTESIS_CIERRE = r'\)'
t_CORCHETE_APERTURA = r'{'
t_CORCHETE_CIERRE = r'}'
t_MAYOR_QUE = r'>'
t_COMILLA = r'"'
t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
# Expresión regular para números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_RESERVADA(t):
    r'\b(While|print|a)\b'
    t.type = 'RESERVADA'
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \t'

# Contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regla para manejar errores
def t_error(t):
    print(f"Token no válido '{t.value}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba del lexer
def analizar_codigo(codigo):
    lexer.lineno = 1  # Reiniciar el contador de líneas a 1
    lexer.input(codigo)
    tokens = []  # Lista para almacenar los tokens
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)  # Agregar el token a la lista
    return tokens  # Devolver la lista de tokens







