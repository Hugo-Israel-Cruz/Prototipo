from flask import Flask, request, render_template
from config import *

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html',
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FORMULARIO=TEXTO_FORMULARIO,
                           TEXTO_SUBFORMULARIO=TEXTO_SUBFORMULARIO,
                           TEXTO_BOTON=TEXTO_BOTON,
                           TEXTO_EJEMPLOS=TEXTO_EJEMPLOS,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA,
                           CATEGORIAS=CATEGORIAS,
                           EJEMPLOS_CONSULTAS=EJEMPLOS_CONSULTAS,
                           COLOR_AZUL=COLOR_AZUL)


@app.route('/consultas')
def consultas():
    return render_template('consultas.html',
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA)


@app.route('/acerca')
def acerca():
    return render_template('acerca.html',
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA)


@app.route('/enviar-consulta', methods=['POST'])
def enviar_consulta():
    nombre = request.form.get('nombre')
    categoria = request.form.get('categoria')
    pregunta = request.form.get('pregunta')

    nombre_categoria = categoria
    for cat in CATEGORIAS:
        if cat["valor"] == categoria:
            nombre_categoria = cat["texto"]
            break

    return render_template('exito.html',
                           nombre=nombre,
                           nombre_categoria=nombre_categoria,
                           pregunta=pregunta,
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA,
                           COLOR_AZUL=COLOR_AZUL)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)