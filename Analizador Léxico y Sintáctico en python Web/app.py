from flask import Flask, render_template, request
import Sintactico
import lexico

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado_sintactico="", resultado_lexico="", datos="")

@app.route('/analizar', methods=['POST'])
def analizar():
    codigo = request.form['datos']
    accion = request.form.get('accion', '')

    if accion == 'sintactico':
        resultado_sintactico = Sintactico.analizar_codigo(codigo)
        resultado_lexico = request.form.get('resultado_lexico', '')
        return render_template('index.html', resultado_lexico=resultado_lexico, resultado_sintactico=resultado_sintactico, datos=codigo)
    else:
        tokens = lexico.analizar_codigo(codigo)
        resultado_lexico = ""
        for token in tokens:
            resultado_lexico += f"LINEA->{token.lineno} ------- |{token.type.upper().replace('_', ' ')}| ----- <SIMBOLO>{token.value}\n"
        return render_template('index.html', resultado_lexico=resultado_lexico, resultado_sintactico="", datos=codigo)

if __name__ == '__main__':
    app.run(debug=True)






