from flask import Flask, request, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from config import *

app = Flask(__name__)
app.secret_key = SECRET_KEY

# ============================================================
# 📦 BASE DE DATOS EN MEMORIA (diccionario)
# ============================================================

usuarios_db = {}
contador_ids = 1

# ============================================================
# 👑 CREAR ADMINISTRADOR POR DEFECTO
# ============================================================

def crear_admin_por_defecto():
    global contador_ids
    if ADMIN_EMAIL not in usuarios_db:
        usuarios_db[ADMIN_EMAIL] = {
            'id': contador_ids,
            'nombre': ADMIN_NOMBRE,
            'email': ADMIN_EMAIL,
            'password_hash': generate_password_hash(ADMIN_PASSWORD),
            'rol': 'admin'
        }
        contador_ids += 1

crear_admin_por_defecto()


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
                           usuario_actual=session.get('usuario_id'),
                           es_admin=session.get('es_admin', False))


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
                           usuario_actual=session.get('usuario_id'),
                           es_admin=session.get('es_admin', False))


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
                           usuario_actual=session.get('usuario_id'),
                           es_admin=session.get('es_admin', False))


# ============================================================
# 🔐 REGISTRO Y LOGIN
# ============================================================

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    global contador_ids

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmar = request.form.get('confirmar_password')

        if not nombre or not email or not password:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('registro'))

        if password != confirmar:
            flash('Las contraseñas no coinciden', 'error')
            return redirect(url_for('registro'))

        if len(password) < 6:
            flash('La contraseña debe tener al menos 6 caracteres', 'error')
            return redirect(url_for('registro'))

        if email in usuarios_db:
            flash('El correo electrónico ya está registrado', 'error')
            return redirect(url_for('registro'))

        usuarios_db[email] = {
            'id': contador_ids,
            'nombre': nombre,
            'email': email,
            'password_hash': generate_password_hash(password),
            'rol': 'usuario'
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
                           usuario_actual=session.get('usuario_id'),
                           es_admin=session.get('es_admin', False))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('login'))

        usuario = usuarios_db.get(email)

        if not usuario:
            flash('Correo o contraseña incorrectos', 'error')
            return redirect(url_for('login'))

        if not check_password_hash(usuario['password_hash'], password):
            flash('Correo o contraseña incorrectos', 'error')
            return redirect(url_for('login'))

        session['usuario_id'] = usuario['id']
        session['usuario_nombre'] = usuario['nombre']
        session['usuario_email'] = usuario['email']
        session['es_admin'] = usuario.get('rol', 'usuario') == 'admin'
        
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
                           usuario_actual=session.get('usuario_id'),
                           es_admin=session.get('es_admin', False))


@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente', 'info')
    return redirect(url_for('inicio'))


# ============================================================
# 👑 PANEL DE ADMINISTRACIÓN
# ============================================================

@app.route('/admin')
def admin_panel():
    if not session.get('es_admin', False):
        flash('Acceso denegado. Se requieren permisos de administrador.', 'error')
        return redirect(url_for('inicio'))
    
    lista_usuarios = []
    for email, datos in usuarios_db.items():
        lista_usuarios.append({
            'id': datos['id'],
            'nombre': datos['nombre'],
            'email': email,
            'rol': datos.get('rol', 'usuario')
        })
    
    total_usuarios = len(usuarios_db)
    total_admins = sum(1 for u in usuarios_db.values() if u.get('rol') == 'admin')
    total_usuarios_normales = total_usuarios - total_admins
    
    return render_template('admin.html',
                           lista_usuarios=lista_usuarios,
                           total_usuarios=total_usuarios,
                           total_admins=total_admins,
                           total_usuarios_normales=total_usuarios_normales,
                           NOMBRE_SITIO=NOMBRE_SITIO,
                           TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                           TEXTO_FOOTER=TEXTO_FOOTER,
                           TEXTO_AÑO=TEXTO_AÑO,
                           NOMBRE_INICIO=NOMBRE_INICIO,
                           NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                           NOMBRE_ACERCA=NOMBRE_ACERCA,
                           usuario_actual=session.get('usuario_id'),
                           es_admin=session.get('es_admin', False))


@app.route('/admin/eliminar-usuario/<int:usuario_id>')
def eliminar_usuario(usuario_id):
    if not session.get('es_admin', False):
        flash('Acceso denegado', 'error')
        return redirect(url_for('inicio'))
    
    if usuario_id == session.get('usuario_id'):
        flash('No puedes eliminarte a ti mismo', 'error')
        return redirect(url_for('admin_panel'))
    
    for email, datos in list(usuarios_db.items()):
        if datos['id'] == usuario_id:
            del usuarios_db[email]
            flash('Usuario eliminado correctamente', 'success')
            break
    
    return redirect(url_for('admin_panel'))


@app.route('/admin/hacer-admin/<int:usuario_id>')
def hacer_admin(usuario_id):
    if not session.get('es_admin', False):
        flash('Acceso denegado', 'error')
        return redirect(url_for('inicio'))
    
    for email, datos in usuarios_db.items():
        if datos['id'] == usuario_id:
            datos['rol'] = 'admin'
            flash(f'Usuario {datos["nombre"]} ahora es administrador', 'success')
            break
    
    return redirect(url_for('admin_panel'))


@app.route('/admin/quitar-admin/<int:usuario_id>')
def quitar_admin(usuario_id):
    if not session.get('es_admin', False):
        flash('Acceso denegado', 'error')
        return redirect(url_for('inicio'))
    
    if usuario_id == session.get('usuario_id'):
        flash('No puedes quitarte permisos a ti mismo', 'error')
        return redirect(url_for('admin_panel'))
    
    for email, datos in usuarios_db.items():
        if datos['id'] == usuario_id:
            datos['rol'] = 'usuario'
            flash(f'Usuario {datos["nombre"]} ya no es administrador', 'success')
            break
    
    return redirect(url_for('admin_panel'))


# ============================================================
# 📊 RUTAS PARA CATEGORÍAS Y BASES DE DATOS
# ============================================================

@app.route('/categoria/<nombre_categoria>')
def ver_categoria(nombre_categoria):
    categoria = INFORMACION_CATEGORIAS.get(nombre_categoria)
    if not categoria:
        flash('Categoría no encontrada', 'error')
        return redirect(url_for('inicio'))
    
    # Si es la categoría de divorcios, usar la plantilla especial
    if nombre_categoria == 'divorcios':
        return render_template('divorcios.html',
                               datos=DATOS_DIVORCIOS,
                               NOMBRE_SITIO=NOMBRE_SITIO,
                               TEXTO_BIENVENIDA=TEXTO_BIENVENIDA,
                               TEXTO_FOOTER=TEXTO_FOOTER,
                               TEXTO_AÑO=TEXTO_AÑO,
                               NOMBRE_INICIO=NOMBRE_INICIO,
                               NOMBRE_CONSULTAS=NOMBRE_CONSULTAS,
                               NOMBRE_ACERCA=NOMBRE_ACERCA,
                               COLOR_AZUL=COLOR_AZUL,
                               usuario_actual=session.get('usuario_id'),
                               es_admin=session.get('es_admin', False))
    
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
                           COLOR_AZUL=COLOR_AZUL,
                           usuario_actual=session.get('usuario_id'),
                           es_admin=session.get('es_admin', False))


@app.route('/base-datos/<nombre_categoria>')
def ver_base_datos(nombre_categoria):
    categoria = INFORMACION_CATEGORIAS.get(nombre_categoria)
    if not categoria:
        flash('Categoría no encontrada', 'error')
        return redirect(url_for('inicio'))
    
    if nombre_categoria == "pensionados":
        columnas = categoria.get('columnas', [])
        datos = categoria.get('datos', [])
    else:
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
                           COLOR_AZUL=COLOR_AZUL,
                           usuario_actual=session.get('usuario_id'),
                           es_admin=session.get('es_admin', False))


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
                           usuario_actual=session.get('usuario_id'),
                           es_admin=session.get('es_admin', False))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)