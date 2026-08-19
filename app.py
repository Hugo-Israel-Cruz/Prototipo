from flask import Flask, request, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from config import *

app = Flask(__name__)
app.secret_key = SECRET_KEY

# ============================================================
# 📦 BASE DE DATOS EN MEMORIA (diccionario)
# ============================================================

# Diccionario para almacenar usuarios
# Estructura: { "email": { "nombre": "Juan", "password_hash": "hash", "id": 1 } }
usuarios_db = {}
contador_ids = 1  # Para asignar IDs automáticos


# ============================================================
# 📄 PÁGINAS PÚBLICAS
# ============================================================

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
                           COLOR_AZUL=COLOR_AZUL,
                           usuario_actual=session.get('usuario_id'))


@app.route('/consultas')
def consultas():
    return render_template('consultas.html',
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA,
                           usuario_actual=session.get('usuario_id'))


@app.route('/acerca')
def acerca():
    return render_template('acerca.html',
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA,
                           usuario_actual=session.get('usuario_id'))


# ============================================================
# 🔐 REGISTRO Y LOGIN (sin base de datos)
# ============================================================

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    global contador_ids

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmar = request.form.get('confirmar_password')

        # Validaciones
        if not nombre or not email or not password:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('registro'))

        if password != confirmar:
            flash('Las contraseñas no coinciden', 'error')
            return redirect(url_for('registro'))

        if len(password) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'error')
            return redirect(url_for('registro'))

        # Verificar si el email ya existe en el diccionario
        if email in usuarios_db:
            flash('El correo electrónico ya está registrado', 'error')
            return redirect(url_for('registro'))

        # Crear nuevo usuario en el diccionario
        usuarios_db[email] = {
            'id': contador_ids,
            'nombre': nombre,
            'email': email,
            'password_hash': generate_password_hash(password)
        }
        contador_ids += 1

        flash('¡Registro exitoso! Inicia sesión para continuar.', 'success')
        return redirect(url_for('login'))

    return render_template('registro.html',
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA,
                           usuario_actual=session.get('usuario_id'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('login'))

        # Buscar usuario en el diccionario
        usuario = usuarios_db.get(email)

        if not usuario:
            flash('Correo o contraseña incorrectos', 'error')
            return redirect(url_for('login'))

        # Verificar contraseña
        if not check_password_hash(usuario['password_hash'], password):
            flash('Correo o contraseña incorrectos', 'error')
            return redirect(url_for('login'))

        # Iniciar sesión
        session['usuario_id'] = usuario['id']
        session['usuario_nombre'] = usuario['nombre']
        session['usuario_email'] = usuario['email']
        flash(f'¡Bienvenido {usuario["nombre"]}!', 'success')
        return redirect(url_for('inicio'))

    return render_template('login.html',
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA,
                           usuario_actual=session.get('usuario_id'))


@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente', 'info')
    return redirect(url_for('inicio'))


# ============================================================
# 📝 RUTA PARA ENVIAR CONSULTA
# ============================================================
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
                           COLOR_AZUL=COLOR_AZUL,
                           usuario_actual=session.get('usuario_id'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


# ============================================================
# 📊 RUTAS PARA CATEGORÍAS Y BASES DE DATOS
# ============================================================

@app.route('/categoria/<nombre_categoria>')
def ver_categoria(nombre_categoria):
    """Muestra la página de detalle de una categoría"""
    categoria = INFORMACION_CATEGORIAS.get(nombre_categoria)
    if not categoria:
        flash('Categoría no encontrada', 'error')
        return redirect(url_for('inicio'))
    
    return render_template('categoria.html',
                           categoria=nombre_categoria,
                           info=categoria,
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA,
                           usuario_actual=session.get('usuario_id'))


@app.route('/base-datos/<nombre_categoria>')
def ver_base_datos(nombre_categoria):
    """Muestra la base de datos completa de una categoría"""
    categoria = INFORMACION_CATEGORIAS.get(nombre_categoria)
    if not categoria:
        flash('Categoría no encontrada', 'error')
        return redirect(url_for('inicio'))
    
    # Para la categoría "pensionados", usamos los datos del CSV
    if nombre_categoria == "pensionados":
        columnas = categoria.get('columnas', [])
        datos = categoria.get('datos', [])
    else:
        # Para otras categorías, usamos los datos genéricos
        columnas = ["id", "nombre", "descripcion", "nivel"] if "datos" in categoria and categoria["datos"] else []
        datos = categoria.get('datos', [])
    
    return render_template('base_datos.html',
                           categoria=nombre_categoria,
                           info=categoria,
                           columnas=columnas,
                           datos=datos,
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA,
                           usuario_actual=session.get('usuario_id'))