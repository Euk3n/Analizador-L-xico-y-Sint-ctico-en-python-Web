import ply.yacc as yacc
from lexico import tokens

# Regla de producción para el ciclo while
def p_ciclo_while(p):
    '''ciclo_while : RESERVADA PARENTESIS_APERTURA RESERVADA MAYOR_QUE NUMERO PARENTESIS_CIERRE CORCHETE_APERTURA instrucciones CORCHETE_CIERRE'''
    p[0] = 'Ciclo While'

# Regla de producción para las instrucciones dentro del ciclo while
def p_instrucciones(p):
    '''instrucciones : RESERVADA PARENTESIS_APERTURA COMILLA IDENTIFICADOR COMILLA PARENTESIS_CIERRE PUNTO_Y_COMA'''
    p[0] = 'Instrucción dentro del ciclo While'


error_sintactico = None

# Regla de producción para manejar errores sintácticos
def p_error(p):
    global error_sintactico
    if p:
        error_sintactico = p.value
        print(f"Error sintáctico de tipo '{p.value}' en la línea {p.lineno}")

parser = yacc.yacc()


def analizar_codigo(codigo):
    global error_sintactico
    error_sintactico = None  # Reiniciar el error sintáctico
    resultado = parser.parse(codigo)
    if resultado is not None:
        return "Análisis sintáctico exitoso: Ciclo While"
    else:
        if error_sintactico:
            return f"Error sintáctico de tipo '{error_sintactico}'"
        else:
            return "Error sintáctico desconocido"
















