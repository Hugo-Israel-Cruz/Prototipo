from flask import Flask, request

app = Flask(__name__)

# Página principal
@app.route('/')
def inicio():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ConsultaRápida - Sistema Profesional</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            /* ========================================
               RESET Y BASE
            ======================================== */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
                background: #f8f6f1;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 0;
                margin: 0;
                color: #1a2a3a;
            }

            /* ========================================
               BARRA SUPERIOR (header)
            ======================================== */
            .top-bar {
                width: 100%;
                background: #ffffff;
                border-bottom: 2px solid #f0ebe0;
                padding: 0 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                height: 72px;
                box-shadow: 0 2px 8px rgba(26, 42, 58, 0.04);
            }

            .logo {
                font-size: 1.4rem;
                font-weight: 700;
                letter-spacing: -0.5px;
                color: #1a3a5c;
            }

            .logo span {
                color: #c9a84c;
            }

            .nav {
                display: flex;
                gap: 32px;
                font-weight: 500;
                font-size: 0.95rem;
            }

            .nav a {
                color: #4a5a6a;
                text-decoration: none;
                transition: color 0.2s;
                padding: 4px 0;
                border-bottom: 2px solid transparent;
            }

            .nav a:hover,
            .nav a.active {
                color: #1a3a5c;
                border-bottom-color: #c9a84c;
            }

            /* ========================================
               CONTENEDOR PRINCIPAL
            ======================================== */
            .main-container {
                max-width: 1040px;
                width: 100%;
                padding: 48px 40px 40px;
                flex: 1;
            }

            /* ========================================
               TARJETA DE BIENVENIDA
            ======================================== */
            .welcome-card {
                background: #ffffff;
                border-radius: 16px;
                padding: 40px 48px 32px;
                margin-bottom: 32px;
                box-shadow: 0 4px 20px rgba(26, 42, 58, 0.06);
                border: 1px solid #f0ebe0;
            }

            .welcome-card h1 {
                font-size: 2rem;
                font-weight: 700;
                color: #1a3a5c;
                letter-spacing: -0.5px;
                margin-bottom: 6px;
            }

            .welcome-card h1 span {
                color: #c9a84c;
            }

            .welcome-card p {
                color: #6a7a8a;
                font-size: 1.05rem;
                font-weight: 400;
            }

            /* ========================================
               TARJETA DEL FORMULARIO
            ======================================== */
            .form-card {
                background: #ffffff;
                border-radius: 16px;
                padding: 36px 40px 40px;
                border: 1px solid #f0ebe0;
                box-shadow: 0 4px 20px rgba(26, 42, 58, 0.06);
            }

            .form-card h2 {
                font-size: 1.2rem;
                font-weight: 600;
                color: #1a3a5c;
                margin-bottom: 4px;
                letter-spacing: -0.3px;
            }

            .form-card .subtitle {
                color: #8a9aaa;
                font-size: 0.95rem;
                margin-bottom: 28px;
            }

            .form-row {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                margin-bottom: 20px;
            }

            .form-group {
                display: flex;
                flex-direction: column;
                gap: 6px;
            }

            .form-group.full {
                grid-column: 1 / -1;
            }

            .form-group label {
                font-weight: 500;
                font-size: 0.875rem;
                color: #1a3a5c;
                letter-spacing: 0.2px;
            }

            .form-group label .required {
                color: #c0392b;
                font-weight: 400;
            }

            .form-group input,
            .form-group select,
            .form-group textarea {
                padding: 12px 16px;
                border: 1.5px solid #e4ddd2;
                border-radius: 10px;
                font-family: 'Inter', sans-serif;
                font-size: 0.95rem;
                background: #fcfbf9;
                transition: border-color 0.25s, box-shadow 0.25s;
                color: #1a2a3a;
            }

            .form-group input:focus,
            .form-group select:focus,
            .form-group textarea:focus {
                outline: none;
                border-color: #c9a84c;
                box-shadow: 0 0 0 4px rgba(201, 168, 76, 0.12);
                background: #ffffff;
            }

            .form-group textarea {
                min-height: 110px;
                resize: vertical;
            }

            .btn-submit {
                background: #c9a84c;
                color: #ffffff;
                border: none;
                padding: 14px 32px;
                font-size: 1rem;
                font-weight: 600;
                border-radius: 10px;
                cursor: pointer;
                transition: background 0.25s, transform 0.15s;
                width: 100%;
                letter-spacing: 0.3px;
                margin-top: 6px;
                font-family: 'Inter', sans-serif;
            }

            .btn-submit:hover {
                background: #b8973a;
            }

            .btn-submit:active {
                transform: scale(0.98);
            }

            /* ========================================
               EJEMPLOS
            ======================================== */
            .examples-section {
                margin-top: 36px;
                padding-top: 28px;
                border-top: 1.5px solid #f0ebe0;
            }

            .examples-section h3 {
                font-size: 0.95rem;
                font-weight: 500;
                color: #4a5a6a;
                margin-bottom: 14px;
                letter-spacing: 0.2px;
            }

            .examples-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 12px;
            }

            .example-item {
                background: #f8f6f1;
                border: 1.5px solid #f0ebe0;
                border-radius: 10px;
                padding: 14px 16px;
                font-size: 0.9rem;
                color: #2a3a4a;
                cursor: pointer;
                transition: all 0.2s;
                text-align: center;
                font-weight: 450;
            }

            .example-item:hover {
                border-color: #c9a84c;
                background: #fcfbf9;
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(201, 168, 76, 0.15);
            }

            .example-item .category {
                display: block;
                font-size: 0.7rem;
                font-weight: 500;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                color: #c9a84c;
                margin-top: 4px;
            }

            /* ========================================
               PIE DE PÁGINA
            ======================================== */
            .footer {
                width: 100%;
                max-width: 1040px;
                padding: 24px 40px 32px;
                color: #9aaa9a;
                font-size: 0.85rem;
                border-top: 1.5px solid #f0ebe0;
                margin-top: 20px;
                text-align: center;
                letter-spacing: 0.2px;
            }

            .footer span {
                color: #c9a84c;
            }

            /* ========================================
               RESPONSIVE
            ======================================== */
            @media (max-width: 768px) {
                .top-bar {
                    padding: 0 20px;
                    height: 64px;
                }
                .nav {
                    gap: 20px;
                    font-size: 0.85rem;
                }
                .main-container {
                    padding: 24px 16px 20px;
                }
                .welcome-card {
                    padding: 28px 20px;
                }
                .welcome-card h1 {
                    font-size: 1.6rem;
                }
                .form-card {
                    padding: 24px 18px 28px;
                }
                .form-row {
                    grid-template-columns: 1fr;
                    gap: 16px;
                }
                .examples-grid {
                    grid-template-columns: 1fr 1fr;
                }
                .footer {
                    padding: 20px 20px 24px;
                }
            }

            @media (max-width: 480px) {
                .top-bar {
                    flex-direction: column;
                    height: auto;
                    padding: 12px 16px;
                    gap: 6px;
                }
                .nav {
                    gap: 14px;
                    font-size: 0.8rem;
                }
                .examples-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>
    <body>
        <!-- ===== BARRA SUPERIOR ===== -->
        <header class="top-bar">
            <div class="logo">Consulta<span>Rápida</span></div>
            <nav class="nav">
                <a href="/" class="active">Inicio</a>
                <a href="/consultas">Mis consultas</a>
                <a href="/acerca">Acerca de</a>
            </nav>
        </header>

        <!-- ===== CONTENIDO ===== -->
        <main class="main-container">
            <!-- Bienvenida -->
            <div class="welcome-card">
                <h1>Sistema de <span>consultas</span></h1>
                <p>Realice una consulta y obtenga información precisa de nuestra base de conocimiento.</p>
            </div>

            <!-- Formulario -->
            <div class="form-card">
                <h2>Nueva consulta</h2>
                <p class="subtitle">Complete los campos para realizar su pregunta.</p>

                <form action="/enviar-consulta" method="POST">
                    <div class="form-row">
                        <div class="form-group">
                            <label for="nombre">Nombre completo <span class="required">*</span></label>
                            <input type="text" id="nombre" name="nombre" placeholder="Ej. Hugo Cruz" required>
                        </div>
                        <div class="form-group">
                            <label for="categoria">Categoría</label>
                            <select id="categoria" name="categoria">
                                <option value="general">General</option>
                                <option value="tecnologia">Tecnología</option>
                                <option value="educacion">Educación</option>
                                <option value="salud">Salud</option>
                                <option value="negocios">Negocios</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group full">
                        <label for="pregunta">Pregunta <span class="required">*</span></label>
                        <textarea id="pregunta" name="pregunta" placeholder="Describa su consulta con claridad..." required></textarea>
                    </div>

                    <button type="submit" class="btn-submit">Enviar consulta</button>
                </form>

                <!-- Ejemplos -->
                <div class="examples-section">
                    <h3>Consultas de ejemplo</h3>
                    <div class="examples-grid">
                        <div class="example-item" onclick="document.getElementById('pregunta').value='¿Cuáles son los fundamentos de la programación orientada a objetos?'">
                            Fundamentos de programación
                            <span class="category">Tecnología</span>
                        </div>
                        <div class="example-item" onclick="document.getElementById('pregunta').value='¿Cómo puedo mejorar mi productividad en el trabajo?'">
                            Mejorar productividad
                            <span class="category">Negocios</span>
                        </div>
                        <div class="example-item" onclick="document.getElementById('pregunta').value='¿Qué beneficios tiene el aprendizaje continuo?'">
                            Beneficios del aprendizaje
                            <span class="category">Educación</span>
                        </div>
                        <div class="example-item" onclick="document.getElementById('pregunta').value='¿Cómo mantener una alimentación saludable?'">
                            Alimentación saludable
                            <span class="category">Salud</span>
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <!-- ===== PIE ===== -->
        <footer class="footer">
            &copy; 2026 <span>ConsultaRápida</span> &middot; Sistema profesional de gestión de consultas
        </footer>

        <script>
            // Pequeño detalle: al hacer clic en un ejemplo, enfoca el textarea
            document.querySelectorAll('.example-item').forEach(el => {
                el.addEventListener('click', function() {
                    const textarea = document.getElementById('pregunta');
                    textarea.focus();
                    textarea.scrollIntoView({ behavior: 'smooth', block: 'center' });
                });
            });
        </script>
    </body>
    </html>
    """
    return html


# Página "Mis consultas"
@app.route('/consultas')
def consultas():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mis consultas - ConsultaRápida</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Inter', -apple-system, sans-serif;
                background: #f8f6f1;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                color: #1a2a3a;
            }
            .top-bar {
                width: 100%;
                background: #ffffff;
                border-bottom: 2px solid #f0ebe0;
                padding: 0 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                height: 72px;
                box-shadow: 0 2px 8px rgba(26, 42, 58, 0.04);
            }
            .logo { font-size: 1.4rem; font-weight: 700; color: #1a3a5c; }
            .logo span { color: #c9a84c; }
            .nav { display: flex; gap: 32px; font-weight: 500; font-size: 0.95rem; }
            .nav a {
                color: #4a5a6a;
                text-decoration: none;
                padding: 4px 0;
                border-bottom: 2px solid transparent;
                transition: color 0.2s;
            }
            .nav a:hover, .nav a.active {
                color: #1a3a5c;
                border-bottom-color: #c9a84c;
            }
            .main-container {
                max-width: 1040px;
                width: 100%;
                padding: 48px 40px 40px;
                flex: 1;
            }
            .card {
                background: #ffffff;
                border-radius: 16px;
                padding: 40px 48px;
                border: 1px solid #f0ebe0;
                box-shadow: 0 4px 20px rgba(26, 42, 58, 0.06);
                text-align: center;
            }
            .card .icon { font-size: 3rem; color: #c9a84c; margin-bottom: 12px; display: block; }
            .card h2 { color: #1a3a5c; font-weight: 600; font-size: 1.4rem; margin-bottom: 6px; }
            .card p { color: #7a8a9a; font-size: 1rem; }
            .btn {
                display: inline-block;
                margin-top: 20px;
                background: #c9a84c;
                color: #ffffff;
                padding: 12px 32px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.95rem;
                transition: background 0.25s;
            }
            .btn:hover { background: #b8973a; }
            .footer {
                width: 100%;
                max-width: 1040px;
                padding: 24px 40px 32px;
                color: #9aaa9a;
                font-size: 0.85rem;
                border-top: 1.5px solid #f0ebe0;
                margin-top: 20px;
                text-align: center;
            }
            .footer span { color: #c9a84c; }
            @media (max-width: 768px) {
                .top-bar { padding: 0 20px; height: 64px; flex-wrap: wrap; }
                .nav { gap: 20px; font-size: 0.85rem; }
                .main-container { padding: 24px 16px 20px; }
                .card { padding: 28px 20px; }
            }
            @media (max-width: 480px) {
                .top-bar { flex-direction: column; height: auto; padding: 12px 16px; gap: 6px; }
                .nav { gap: 14px; font-size: 0.8rem; }
            }
        </style>
    </head>
    <body>
        <header class="top-bar">
            <div class="logo">Consulta<span>Rápida</span></div>
            <nav class="nav">
                <a href="/">Inicio</a>
                <a href="/consultas" class="active">Mis consultas</a>
                <a href="/acerca">Acerca de</a>
            </nav>
        </header>

        <main class="main-container">
            <div class="card">
                <span class="icon">📋</span>
                <h2>Aún no hay consultas</h2>
                <p>Realice su primera consulta desde la página de inicio.</p>
                <a href="/" class="btn">Ir al inicio</a>
            </div>
        </main>

        <footer class="footer">
            &copy; 2026 <span>ConsultaRápida</span> &middot; Sistema profesional de gestión de consultas
        </footer>
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
        <title>Acerca de - ConsultaRápida</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Inter', -apple-system, sans-serif;
                background: #f8f6f1;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                color: #1a2a3a;
            }
            .top-bar {
                width: 100%;
                background: #ffffff;
                border-bottom: 2px solid #f0ebe0;
                padding: 0 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                height: 72px;
                box-shadow: 0 2px 8px rgba(26, 42, 58, 0.04);
            }
            .logo { font-size: 1.4rem; font-weight: 700; color: #1a3a5c; }
            .logo span { color: #c9a84c; }
            .nav { display: flex; gap: 32px; font-weight: 500; font-size: 0.95rem; }
            .nav a {
                color: #4a5a6a;
                text-decoration: none;
                padding: 4px 0;
                border-bottom: 2px solid transparent;
                transition: color 0.2s;
            }
            .nav a:hover, .nav a.active {
                color: #1a3a5c;
                border-bottom-color: #c9a84c;
            }
            .main-container {
                max-width: 1040px;
                width: 100%;
                padding: 48px 40px 40px;
                flex: 1;
            }
            .card {
                background: #ffffff;
                border-radius: 16px;
                padding: 40px 48px;
                border: 1px solid #f0ebe0;
                box-shadow: 0 4px 20px rgba(26, 42, 58, 0.06);
            }
            .card h2 { color: #1a3a5c; font-weight: 600; font-size: 1.3rem; margin-bottom: 12px; }
            .card p { color: #4a5a6a; line-height: 1.7; margin-bottom: 12px; }
            .card ul { padding-left: 22px; color: #4a5a6a; line-height: 1.8; }
            .card ul li { margin-bottom: 4px; }
            .card .gold { color: #c9a84c; font-weight: 500; }
            .btn {
                display: inline-block;
                margin-top: 16px;
                background: #c9a84c;
                color: #ffffff;
                padding: 12px 32px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.95rem;
                transition: background 0.25s;
            }
            .btn:hover { background: #b8973a; }
            .footer {
                width: 100%;
                max-width: 1040px;
                padding: 24px 40px 32px;
                color: #9aaa9a;
                font-size: 0.85rem;
                border-top: 1.5px solid #f0ebe0;
                margin-top: 20px;
                text-align: center;
            }
            .footer span { color: #c9a84c; }
            @media (max-width: 768px) {
                .top-bar { padding: 0 20px; height: 64px; flex-wrap: wrap; }
                .nav { gap: 20px; font-size: 0.85rem; }
                .main-container { padding: 24px 16px 20px; }
                .card { padding: 28px 20px; }
            }
            @media (max-width: 480px) {
                .top-bar { flex-direction: column; height: auto; padding: 12px 16px; gap: 6px; }
                .nav { gap: 14px; font-size: 0.8rem; }
            }
        </style>
    </head>
    <body>
        <header class="top-bar">
            <div class="logo">Consulta<span>Rápida</span></div>
            <nav class="nav">
                <a href="/">Inicio</a>
                <a href="/consultas">Mis consultas</a>
                <a href="/acerca" class="active">Acerca de</a>
            </nav>
        </header>

        <main class="main-container">
            <div class="card">
                <h2>Acerca de ConsultaRápida</h2>
                <p>
                    <span class="gold">ConsultaRápida</span> es un sistema profesional de gestión de consultas 
                    diseñado para facilitar el acceso a información estructurada y precisa.
                </p>

                <h2 style="margin-top: 24px;">Características</h2>
                <ul>
                    <li>Formulario de consultas con categorización</li>
                    <li>Almacenamiento seguro en base de datos PostgreSQL</li>
                    <li>Interfaz limpia y profesional</li>
                    <li>Diseño responsive para todos los dispositivos</li>
                </ul>

                <h2 style="margin-top: 24px;">Tecnologías</h2>
                <ul>
                    <li>Python &middot; Flask &middot; PostgreSQL</li>
                    <li>HTML5 &middot; CSS3 &middot; Inter (tipografía)</li>
                    <li>Render (alojamiento en la nube)</li>
                </ul>

                <a href="/" class="btn">Volver al inicio</a>
            </div>
        </main>

        <footer class="footer">
            &copy; 2026 <span>ConsultaRápida</span> &middot; Sistema profesional de gestión de consultas
        </footer>
    </body>
    </html>
    """
    return html


# Ruta que recibe los datos del formulario
@app.route('/enviar-consulta', methods=['POST'])
def enviar_consulta():
    nombre = request.form.get('nombre')
    categoria = request.form.get('categoria')
    pregunta = request.form.get('pregunta')

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Consulta enviada - ConsultaRápida</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: 'Inter', -apple-system, sans-serif;
                background: #f8f6f1;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                color: #1a2a3a;
            }}
            .top-bar {{
                width: 100%;
                background: #ffffff;
                border-bottom: 2px solid #f0ebe0;
                padding: 0 40px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                height: 72px;
                box-shadow: 0 2px 8px rgba(26, 42, 58, 0.04);
            }}
            .logo {{ font-size: 1.4rem; font-weight: 700; color: #1a3a5c; }}
            .logo span {{ color: #c9a84c; }}
            .nav {{ display: flex; gap: 32px; font-weight: 500; font-size: 0.95rem; }}
            .nav a {{
                color: #4a5a6a;
                text-decoration: none;
                padding: 4px 0;
                border-bottom: 2px solid transparent;
                transition: color 0.2s;
            }}
            .nav a:hover {{ color: #1a3a5c; border-bottom-color: #c9a84c; }}
            .main-container {{
                max-width: 1040px;
                width: 100%;
                padding: 48px 40px 40px;
                flex: 1;
            }}
            .card {{
                background: #ffffff;
                border-radius: 16px;
                padding: 40px 48px;
                border: 1px solid #f0ebe0;
                box-shadow: 0 4px 20px rgba(26, 42, 58, 0.06);
            }}
            .card .check {{ color: #c9a84c; font-size: 2.8rem; display: block; margin-bottom: 8px; }}
            .card h2 {{ color: #1a3a5c; font-weight: 600; font-size: 1.5rem; margin-bottom: 4px; }}
            .card .sub {{ color: #7a8a9a; font-size: 1rem; margin-bottom: 20px; }}
            .detail-box {{
                background: #f8f6f1;
                border-radius: 12px;
                padding: 20px 24px;
                margin: 16px 0 20px;
                text-align: left;
            }}
            .detail-box p {{ margin: 6px 0; color: #2a3a4a; font-size: 0.95rem; }}
            .detail-box strong {{ color: #1a3a5c; font-weight: 600; }}
            .detail-box .gold-text {{ color: #c9a84c; font-weight: 500; }}
            .btn {{
                display: inline-block;
                background: #c9a84c;
                color: #ffffff;
                padding: 12px 32px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.95rem;
                transition: background 0.25s;
            }}
            .btn:hover {{ background: #b8973a; }}
            .footer {{
                width: 100%;
                max-width: 1040px;
                padding: 24px 40px 32px;
                color: #9aaa9a;
                font-size: 0.85rem;
                border-top: 1.5px solid #f0ebe0;
                margin-top: 20px;
                text-align: center;
            }}
            .footer span {{ color: #c9a84c; }}
            @media (max-width: 768px) {{
                .top-bar {{ padding: 0 20px; height: 64px; flex-wrap: wrap; }}
                .nav {{ gap: 20px; font-size: 0.85rem; }}
                .main-container {{ padding: 24px 16px 20px; }}
                .card {{ padding: 28px 20px; }}
                .detail-box {{ padding: 16px; }}
            }}
            @media (max-width: 480px) {{
                .top-bar {{ flex-direction: column; height: auto; padding: 12px 16px; gap: 6px; }}
                .nav {{ gap: 14px; font-size: 0.8rem; }}
            }}
        </style>
    </head>
    <body>
        <header class="top-bar">
            <div class="logo">Consulta<span>Rápida</span></div>
            <nav class="nav">
                <a href="/">Inicio</a>
                <a href="/consultas">Mis consultas</a>
                <a href="/acerca">Acerca de</a>
            </nav>
        </header>

        <main class="main-container">
            <div class="card">
                <span class="check">✓</span>
                <h2>Consulta enviada</h2>
                <p class="sub">Su consulta ha sido recibida correctamente.</p>

                <div class="detail-box">
                    <p><strong>Nombre:</strong> {nombre}</p>
                    <p><strong>Categoría:</strong> <span class="gold-text">{categoria}</span></p>
                    <p><strong>Pregunta:</strong> {pregunta}</p>
                </div>

                <p style="color: #7a8a9a; margin-bottom: 16px; font-size: 0.95rem;">
                    En breve recibirá una respuesta a su consulta.
                </p>
                <a href="/" class="btn">Realizar otra consulta</a>
            </div>
        </main>

        <footer class="footer">
            &copy; 2026 <span>ConsultaRápida</span> &middot; Sistema profesional de gestión de consultas
        </footer>
    </body>
    </html>
    """
    return html


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)