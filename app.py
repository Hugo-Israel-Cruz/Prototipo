from flask import Flask, request, render_template_string

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    # HTML de la página principal
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Sistema de Consultas</title>
        <style>
            /* ============ ESTILOS GENERALES ============ */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            /* ============ TARJETA PRINCIPAL ============ */
            .container {
                background: white;
                max-width: 900px;
                width: 100%;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            
            /* ============ ENCABEZADO ============ */
            .header {
                text-align: center;
                margin-bottom: 30px;
            }
            
            .header h1 {
                font-size: 2.5em;
                color: #2c3e50;
                margin-bottom: 10px;
            }
            
            .header h1 span {
                color: #764ba2;
            }
            
            .header p {
                color: #7f8c8d;
                font-size: 1.1em;
            }
            
            /* ============ MENÚ DE NAVEGACIÓN ============ */
            .menu {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin: 25px 0 30px 0;
                flex-wrap: wrap;
            }
            
            .menu a {
                color: #2c3e50;
                text-decoration: none;
                font-weight: 600;
                padding: 8px 20px;
                border-radius: 25px;
                transition: all 0.3s ease;
                border: 2px solid transparent;
            }
            
            .menu a:hover {
                background: #667eea;
                color: white;
                border-color: #667eea;
            }
            
            .menu a.activo {
                background: #667eea;
                color: white;
            }
            
            /* ============ FORMULARIO ============ */
            .seccion {
                background: #f8f9fa;
                padding: 25px;
                border-radius: 15px;
                margin-bottom: 25px;
            }
            
            .seccion h2 {
                color: #2c3e50;
                margin-bottom: 15px;
                font-size: 1.4em;
            }
            
            .seccion h2 span {
                color: #764ba2;
            }
            
            .campo {
                margin-bottom: 15px;
            }
            
            .campo label {
                display: block;
                font-weight: 600;
                margin-bottom: 5px;
                color: #2c3e50;
            }
            
            .campo input,
            .campo textarea,
            .campo select {
                width: 100%;
                padding: 12px 15px;
                border: 2px solid #ddd;
                border-radius: 10px;
                font-size: 1em;
                transition: border-color 0.3s ease;
                font-family: inherit;
            }
            
            .campo input:focus,
            .campo textarea:focus,
            .campo select:focus {
                outline: none;
                border-color: #667eea;
            }
            
            .campo textarea {
                min-height: 100px;
                resize: vertical;
            }
            
            /* ============ BOTONES ============ */
            .btn {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 14px 35px;
                font-size: 1.1em;
                font-weight: 600;
                border-radius: 10px;
                cursor: pointer;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                width: 100%;
            }
            
            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
            }
            
            .btn:active {
                transform: translateY(0);
            }
            
            /* ============ SECCIÓN DE EJEMPLOS ============ */
            .ejemplos {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin-top: 15px;
            }
            
            .ejemplo-item {
                background: white;
                padding: 15px;
                border-radius: 10px;
                border: 2px solid #e9ecef;
                text-align: center;
                transition: all 0.3s ease;
                cursor: pointer;
            }
            
            .ejemplo-item:hover {
                border-color: #667eea;
                transform: translateY(-3px);
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            
            .ejemplo-item .icono {
                font-size: 2em;
                display: block;
                margin-bottom: 5px;
            }
            
            .ejemplo-item .texto {
                color: #2c3e50;
                font-size: 0.9em;
            }
            
            /* ============ PIE DE PÁGINA ============ */
            .footer {
                text-align: center;
                margin-top: 25px;
                color: #bdc3c7;
                font-size: 0.9em;
                border-top: 2px solid #ecf0f1;
                padding-top: 20px;
            }
            
            /* ============ RESPONSIVE ============ */
            @media (max-width: 600px) {
                .container {
                    padding: 20px;
                }
                
                .header h1 {
                    font-size: 1.8em;
                }
                
                .menu {
                    gap: 10px;
                }
                
                .menu a {
                    font-size: 0.9em;
                    padding: 6px 15px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- ===== ENCABEZADO ===== -->
            <div class="header">
                <h1>🔍 <span>Consulta</span>Rápida</h1>
                <p>Haz preguntas y obtén respuestas basadas en nuestra base de conocimiento</p>
            </div>
            
            <!-- ===== MENÚ ===== -->
            <div class="menu">
                <a href="/" class="activo">🏠 Inicio</a>
                <a href="/consultas">📋 Mis Consultas</a>
                <a href="/acerca">ℹ️ Acerca de</a>
            </div>
            
            <!-- ===== FORMULARIO DE CONSULTA ===== -->
            <div class="seccion">
                <h2>📝 <span>Nueva</span> Consulta</h2>
                <form action="/enviar-consulta" method="POST">
                    <div class="campo">
                        <label for="nombre">Tu nombre</label>
                        <input type="text" id="nombre" name="nombre" placeholder="Ej: Hugo" required>
                    </div>
                    
                    <div class="campo">
                        <label for="categoria">Categoría</label>
                        <select id="categoria" name="categoria">
                            <option value="general">General</option>
                            <option value="tecnologia">Tecnología</option>
                            <option value="educacion">Educación</option>
                            <option value="salud">Salud</option>
                            <option value="negocios">Negocios</option>
                        </select>
                    </div>
                    
                    <div class="campo">
                        <label for="pregunta">Tu pregunta</label>
                        <textarea id="pregunta" name="pregunta" placeholder="Escribe tu consulta aquí..." required></textarea>
                    </div>
                    
                    <button type="submit" class="btn">🚀 Enviar Consulta</button>
                </form>
            </div>
            
            <!-- ===== EJEMPLOS DE CONSULTAS ===== -->
            <div class="seccion">
                <h2>💡 <span>Ejemplos</span> de Consultas</h2>
                <p style="color: #7f8c8d; margin-bottom: 15px; font-size: 0.95em;">
                    Haz clic en un ejemplo para probar
                </p>
                <div class="ejemplos">
                    <div class="ejemplo-item" onclick="document.getElementById('pregunta').value='¿Qué es Python?'">
                        <span class="icono">🐍</span>
                        <span class="texto">¿Qué es Python?</span>
                    </div>
                    <div class="ejemplo-item" onclick="document.getElementById('pregunta').value='¿Cómo funciona el aprendizaje automático?'">
                        <span class="icono">🤖</span>
                        <span class="texto">¿Cómo funciona el machine learning?</span>
                    </div>
                    <div class="ejemplo-item" onclick="document.getElementById('pregunta').value='¿Cuáles son los mejores lenguajes para programar?'">
                        <span class="icono">💻</span>
                        <span class="texto">Mejores lenguajes de programación</span>
                    </div>
                    <div class="ejemplo-item" onclick="document.getElementById('pregunta').value='¿Cómo empezar a aprender programación?'">
                        <span class="icono">📚</span>
                        <span class="texto">¿Cómo empezar a programar?</span>
                    </div>
                </div>
            </div>
            
            <!-- ===== PIE DE PÁGINA ===== -->
            <div class="footer">
                <p>© 2026 - Mi Sistema de Consultas | Todos los derechos reservados</p>
            </div>
        </div>
        
        <!-- ===== JAVASCRIPT PARA DEMOSTRACIÓN ===== -->
        <script>
            // Esto es para que los ejemplos funcionen (ya están en el onclick)
            console.log('¡Bienvenido a ConsultaRápida!');
        </script>
    </body>
    </html>
    """
    return html

# Página "Consultas" (lista de consultas)
@app.route('/consultas')
def consultas():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mis Consultas</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            .container {
                background: white;
                max-width: 900px;
                width: 100%;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { font-size: 2.5em; color: #2c3e50; }
            .header h1 span { color: #764ba2; }
            .menu {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin: 25px 0 30px 0;
                flex-wrap: wrap;
            }
            .menu a {
                color: #2c3e50;
                text-decoration: none;
                font-weight: 600;
                padding: 8px 20px;
                border-radius: 25px;
                transition: all 0.3s ease;
                border: 2px solid transparent;
            }
            .menu a:hover, .menu a.activo {
                background: #667eea;
                color: white;
                border-color: #667eea;
            }
            .mensaje {
                background: #f8f9fa;
                padding: 40px;
                border-radius: 15px;
                text-align: center;
            }
            .mensaje h2 { color: #2c3e50; margin-bottom: 10px; }
            .mensaje p { color: #7f8c8d; font-size: 1.1em; }
            .btn-volver {
                display: inline-block;
                margin-top: 20px;
                background: #667eea;
                color: white;
                padding: 12px 30px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
            }
            .btn-volver:hover {
                background: #764ba2;
            }
            .footer {
                text-align: center;
                margin-top: 25px;
                color: #bdc3c7;
                font-size: 0.9em;
                border-top: 2px solid #ecf0f1;
                padding-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📋 <span>Mis</span> Consultas</h1>
                <p>Aquí verás todas tus consultas guardadas</p>
            </div>
            
            <div class="menu">
                <a href="/">🏠 Inicio</a>
                <a href="/consultas" class="activo">📋 Mis Consultas</a>
                <a href="/acerca">ℹ️ Acerca de</a>
            </div>
            
            <div class="mensaje">
                <h2>📭 Sin consultas aún</h2>
                <p>¡Realiza tu primera consulta desde la página de inicio!</p>
                <a href="/" class="btn-volver">⬅ Volver al inicio</a>
            </div>
            
            <div class="footer">
                <p>© 2026 - Mi Sistema de Consultas</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

# Página "Acerca de"
@app.route('/acerca')
def acerca():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Acerca de</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            .container {
                background: white;
                max-width: 900px;
                width: 100%;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { font-size: 2.5em; color: #2c3e50; }
            .header h1 span { color: #764ba2; }
            .menu {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin: 25px 0 30px 0;
                flex-wrap: wrap;
            }
            .menu a {
                color: #2c3e50;
                text-decoration: none;
                font-weight: 600;
                padding: 8px 20px;
                border-radius: 25px;
                transition: all 0.3s ease;
                border: 2px solid transparent;
            }
            .menu a:hover, .menu a.activo {
                background: #667eea;
                color: white;
                border-color: #667eea;
            }
            .contenido {
                background: #f8f9fa;
                padding: 30px;
                border-radius: 15px;
                line-height: 1.8;
            }
            .contenido h2 { color: #2c3e50; margin-bottom: 15px; }
            .contenido p { color: #34495e; margin-bottom: 10px; }
            .contenido ul { padding-left: 25px; color: #34495e; }
            .contenido ul li { margin-bottom: 8px; }
            .btn-volver {
                display: inline-block;
                margin-top: 20px;
                background: #667eea;
                color: white;
                padding: 12px 30px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
            }
            .btn-volver:hover { background: #764ba2; }
            .footer {
                text-align: center;
                margin-top: 25px;
                color: #bdc3c7;
                font-size: 0.9em;
                border-top: 2px solid #ecf0f1;
                padding-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>ℹ️ <span>Acerca</span> de</h1>
                <p>Conoce más sobre este proyecto</p>
            </div>
            
            <div class="menu">
                <a href="/">🏠 Inicio</a>
                <a href="/consultas">📋 Mis Consultas</a>
                <a href="/acerca" class="activo">ℹ️ Acerca de</a>
            </div>
            
            <div class="contenido">
                <h2>📖 ¿Qué es ConsultaRápida?</h2>
                <p>Es un sistema de consultas que permite a los usuarios hacer preguntas y recibir respuestas basadas en información almacenada.</p>
                
                <h2>🎯 Características</h2>
                <ul>
                    <li>✅ Formulario para realizar consultas</li>
                    <li>✅ Almacenamiento de preguntas y respuestas</li>
                    <li>✅ Búsqueda de información por categorías</li>
                    <li>✅ Interfaz fácil y moderna</li>
                </ul>
                
                <h2>🛠️ Tecnologías utilizadas</h2>
                <ul>
                    <li>🐍 Python con Flask</li>
                    <li>🗄️ PostgreSQL (base de datos)</li>
                    <li>☁️ Render (alojamiento)</li>
                </ul>
                
                <a href="/" class="btn-volver">⬅ Volver al inicio</a>
            </div>
            
            <div class="footer">
                <p>© 2026 - Mi Sistema de Consultas</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)