from flask import Flask, request

app = Flask(__name__)

# ============================================================
# 🎨 ZONA DE PERSONALIZACIÓN - EDITA AQUÍ LOS COLORES Y TEXTOS
# ============================================================

# ---------- COLORES PRINCIPALES ----------
COLOR_DORADO = "#C9A84C"        # Cambia este color dorado
COLOR_DORADO_OSCURO = "#B8943A"  # Dorado más oscuro para hover
COLOR_DORADO_BORDE = "#A07D2E"   # Borde de elementos
COLOR_DORADO_CLARO = "#D4C08A"   # Dorado claro para bordes suaves
COLOR_FONDO_DORADO = "#F8F2E6"   # Fondo dorado muy claro

COLOR_AZUL = "#1A3A5C"          # Cambia este color azul
COLOR_AZUL_CLARO = "#2C5F8A"     # Azul más claro
COLOR_AZUL_OSCURO = "#0F1B33"    # Azul muy oscuro

COLOR_BLANCO = "#FFFFFF"        # Blanco para fondos
COLOR_GRIS = "#F5F3F0"          # Gris suave para fondos secundarios
COLOR_GRIS_BORDE = "#E8DFC8"    # Gris para bordes

# ---------- TEXTOS EDITABLES ----------
NOMBRE_SITIO = "ConsultaRápida"     # Cambia el nombre de tu sitio
TEXTO_BIENVENIDA = "Sistema de consultas"  # Título de bienvenida
TEXTO_SUBTITULO = "Realice una consulta y obtenga información precisa de nuestra base de conocimiento."
TEXTO_FORMULARIO = "Nueva consulta"
TEXTO_SUBFORMULARIO = "Complete los campos para realizar su pregunta."
TEXTO_BOTON = "Enviar consulta"
TEXTO_EJEMPLOS = "Consultas de ejemplo"
TEXTO_FOOTER = "Sistema profesional de gestión de consultas"
TEXTO_AÑO = "2026"

# ---------- NOMBRES DE PÁGINAS (Menú) ----------
NOMBRE_INICIO = "Inicio"
NOMBRE_CONSULTAS = "Mis consultas"
NOMBRE_ACERCA = "Acerca de"

# ---------- CATEGORÍAS (edita o agrega más) ----------
CATEGORIAS = [
    {"valor": "general", "texto": "General"},
    {"valor": "tecnologia", "texto": "Tecnología"},
    {"valor": "educacion", "texto": "Educación"},
    {"valor": "salud", "texto": "Salud"},
    {"valor": "negocios", "texto": "Negocios"},
]

# ---------- EJEMPLOS DE CONSULTAS (edita o agrega más) ----------
EJEMPLOS_CONSULTAS = [
    {"texto": "Fundamentos de programación orientada a objetos", "categoria": "Tecnología"},
    {"texto": "Cómo mejorar la productividad en el trabajo", "categoria": "Negocios"},
    {"texto": "Beneficios del aprendizaje continuo", "categoria": "Educación"},
    {"texto": "Cómo mantener una alimentación saludable", "categoria": "Salud"},
]

# ============================================================
# FIN ZONA DE PERSONALIZACIÓN
# ============================================================


# ============================================================
# FUNCIÓN PARA GENERAR ESTILOS CSS (usa las variables de arriba)
# ============================================================
def generar_estilos():
    return f"""
    <style>
        /* ========================================
           RESET Y BASE
        ======================================== */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: {COLOR_DORADO};
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 0;
            margin: 0;
            color: {COLOR_AZUL};
        }}

        /* ========================================
           BARRA SUPERIOR (fondo dorado)
        ======================================== */
        .top-bar {{
            width: 100%;
            background: {COLOR_DORADO_OSCURO};
            padding: 0 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 72px;
            border-bottom: 2px solid {COLOR_DORADO_BORDE};
        }}

        .logo {{
            font-size: 1.4rem;
            font-weight: 700;
            letter-spacing: -0.5px;
            color: {COLOR_BLANCO};
        }}

        .logo span {{
            color: {COLOR_AZUL};
        }}

        .nav {{
            display: flex;
            gap: 32px;
            font-weight: 500;
            font-size: 0.95rem;
        }}

        .nav a {{
            color: {COLOR_BLANCO};
            text-decoration: none;
            transition: all 0.2s;
            padding: 4px 0;
            border-bottom: 2px solid transparent;
        }}

        .nav a:hover,
        .nav a.active {{
            border-bottom-color: {COLOR_AZUL};
            color: {COLOR_AZUL};
        }}

        /* ========================================
           CONTENEDOR PRINCIPAL
        ======================================== */
        .main-container {{
            max-width: 1200px;
            width: 100%;
            padding: 30px 40px 30px;
            flex: 1;
            display: flex;
            gap: 28px;
        }}

        /* ========================================
           BARRA LATERAL (AZUL)
        ======================================== */
        .sidebar {{
            width: 240px;
            min-width: 200px;
            background: {COLOR_AZUL};
            border-radius: 16px;
            padding: 28px 20px;
            border: 1px solid {COLOR_DORADO_CLARO};
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.10);
            height: fit-content;
        }}

        .sidebar h3 {{
            color: {COLOR_DORADO};
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
            margin-bottom: 18px;
            padding-bottom: 10px;
            border-bottom: 1.5px solid rgba(201, 168, 76, 0.3);
        }}

        .sidebar .menu-item {{
            display: block;
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
            padding: 10px 14px;
            border-radius: 10px;
            font-size: 0.9rem;
            font-weight: 450;
            transition: all 0.2s;
            margin-bottom: 4px;
        }}

        .sidebar .menu-item:hover {{
            background: rgba(201, 168, 76, 0.15);
            color: {COLOR_DORADO};
        }}

        .sidebar .menu-item.active {{
            background: {COLOR_DORADO};
            color: {COLOR_AZUL};
            font-weight: 600;
        }}

        .sidebar .menu-item .icon {{
            margin-right: 10px;
            font-size: 1.1rem;
        }}

        /* ========================================
           CONTENIDO PRINCIPAL
        ======================================== */
        .content {{
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}

        /* ========================================
           BARRA DE BÚSQUEDA
        ======================================== */
        .search-bar {{
            background: {COLOR_BLANCO};
            border-radius: 12px;
            padding: 8px 16px;
            border: 1px solid {COLOR_DORADO_CLARO};
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .search-bar input {{
            flex: 1;
            border: none;
            padding: 12px 0;
            font-size: 0.95rem;
            font-family: 'Inter', sans-serif;
            color: {COLOR_AZUL};
            background: transparent;
            outline: none;
        }}

        .search-bar input::placeholder {{
            color: #9a9a9a;
        }}

        .search-bar .btn-search {{
            background: {COLOR_DORADO};
            color: {COLOR_BLANCO};
            border: none;
            padding: 10px 24px;
            border-radius: 10px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.25s;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
        }}

        .search-bar .btn-search:hover {{
            background: {COLOR_DORADO_OSCURO};
        }}

        /* ========================================
           TARJETA DE ESTADÍSTICAS
        ======================================== */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 16px;
        }}

        .stat-card {{
            background: {COLOR_BLANCO};
            border-radius: 14px;
            padding: 20px 18px;
            text-align: center;
            border: 1px solid {COLOR_DORADO_CLARO};
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
            transition: transform 0.2s;
        }}

        .stat-card:hover {{
            transform: translateY(-3px);
        }}

        .stat-card .numero {{
            font-size: 2rem;
            font-weight: 700;
            color: {COLOR_DORADO};
            display: block;
        }}

        .stat-card .label {{
            font-size: 0.8rem;
            color: {COLOR_AZUL};
            font-weight: 500;
            margin-top: 4px;
        }}

        /* ========================================
           TARJETA DE CONTENIDO PRINCIPAL
        ======================================== */
        .content-card {{
            background: {COLOR_BLANCO};
            border-radius: 16px;
            padding: 28px 32px 32px;
            border: 1px solid {COLOR_DORADO_CLARO};
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        }}

        .content-card h2 {{
            font-size: 1.2rem;
            font-weight: 600;
            color: {COLOR_AZUL};
            margin-bottom: 4px;
            letter-spacing: -0.3px;
        }}

        .content-card .sub {{
            color: #5a7a8a;
            font-size: 0.95rem;
            margin-bottom: 20px;
        }}

        /* ========================================
           FORMULARIO
        ======================================== */
        .form-row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 18px;
            margin-bottom: 16px;
        }}

        .form-group {{
            display: flex;
            flex-direction: column;
            gap: 5px;
        }}

        .form-group.full {{
            grid-column: 1 / -1;
        }}

        .form-group label {{
            font-weight: 500;
            font-size: 0.85rem;
            color: {COLOR_AZUL};
        }}

        .form-group label .required {{
            color: #c0392b;
            font-weight: 400;
        }}

        .form-group input,
        .form-group select,
        .form-group textarea {{
            padding: 11px 15px;
            border: 1.5px solid {COLOR_DORADO_CLARO};
            border-radius: 10px;
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            background: {COLOR_GRIS};
            transition: border-color 0.25s, box-shadow 0.25s;
            color: {COLOR_AZUL};
        }}

        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {{
            outline: none;
            border-color: {COLOR_DORADO};
            box-shadow: 0 0 0 4px rgba(201, 168, 76, 0.12);
            background: {COLOR_BLANCO};
        }}

        .form-group textarea {{
            min-height: 90px;
            resize: vertical;
        }}

        .btn-submit {{
            background: {COLOR_DORADO};
            color: {COLOR_BLANCO};
            border: none;
            padding: 13px 28px;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 10px;
            cursor: pointer;
            transition: background 0.25s, transform 0.15s;
            width: 100%;
            font-family: 'Inter', sans-serif;
        }}

        .btn-submit:hover {{
            background: {COLOR_DORADO_OSCURO};
        }}

        /* ========================================
           EJEMPLOS
        ======================================== */
        .examples-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 10px;
            margin-top: 12px;
        }}

        .example-item {{
            background: {COLOR_GRIS};
            border: 1.5px solid {COLOR_DORADO_CLARO};
            border-radius: 10px;
            padding: 12px 14px;
            font-size: 0.85rem;
            color: {COLOR_AZUL};
            cursor: pointer;
            transition: all 0.2s;
            text-align: center;
            font-weight: 450;
        }}

        .example-item:hover {{
            border-color: {COLOR_DORADO};
            background: {COLOR_FONDO_DORADO};
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(201, 168, 76, 0.2);
        }}

        .example-item .cat {{
            display: block;
            font-size: 0.65rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: {COLOR_DORADO};
            margin-top: 4px;
        }}

        /* ========================================
           PIE DE PÁGINA
        ======================================== */
        .footer {{
            width: 100%;
            max-width: 1200px;
            padding: 20px 40px 24px;
            color: {COLOR_BLANCO};
            font-size: 0.85rem;
            border-top: 2px solid {COLOR_DORADO_BORDE};
            margin-top: 10px;
            text-align: center;
            background: {COLOR_DORADO_OSCURO};
            border-radius: 0 0 16px 16px;
        }}

        .footer span {{
            color: {COLOR_AZUL};
            font-weight: 600;
        }}

        /* ========================================
           RESPONSIVE
        ======================================== */
        @media (max-width: 900px) {{
            .main-container {{
                flex-direction: column;
                padding: 20px 16px 20px;
            }}
            .sidebar {{
                width: 100%;
                min-width: unset;
                display: flex;
                flex-wrap: wrap;
                gap: 4px;
                padding: 16px 18px;
            }}
            .sidebar h3 {{
                width: 100%;
                margin-bottom: 8px;
            }}
            .sidebar .menu-item {{
                padding: 8px 14px;
                font-size: 0.85rem;
                margin-bottom: 0;
            }}
        }}

        @media (max-width: 640px) {{
            .top-bar {{
                flex-direction: column;
                height: auto;
                padding: 14px 16px;
                gap: 8px;
            }}
            .nav {{
                gap: 18px;
                font-size: 0.85rem;
                flex-wrap: wrap;
                justify-content: center;
            }}
            .form-row {{
                grid-template-columns: 1fr;
                gap: 14px;
            }}
            .stats-grid {{
                grid-template-columns: 1fr 1fr;
            }}
            .content-card {{
                padding: 20px 16px 22px;
            }}
            .footer {{
                padding: 16px 20px 20px;
            }}
            .search-bar {{
                flex-wrap: wrap;
                padding: 12px 16px;
            }}
            .search-bar .btn-search {{
                width: 100%;
            }}
        }}
    </style>
    """

# ============================================================


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================
@app.route('/')
def inicio():
    # Generar opciones de categorías para el select
    opciones_categorias = ""
    for cat in CATEGORIAS:
        opciones_categorias += f'<option value="{cat["valor"]}">{cat["texto"]}</option>'

    # Generar ejemplos
    ejemplos_html = ""
    for ej in EJEMPLOS_CONSULTAS:
        ejemplos_html += f'''
        <div class="example-item" onclick="document.getElementById('pregunta').value='{ej["texto"]}'">
            {ej["texto"]}
            <span class="cat">{ej["categoria"]}</span>
        </div>
        '''

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{NOMBRE_SITIO} - Sistema Profesional</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        {generar_estilos()}
    </head>
    <body>
        <!-- ===== BARRA SUPERIOR ===== -->
        <header class="top-bar">
            <div class="logo">{NOMBRE_SITIO} <span>|</span> {TEXTO_BIENVENIDA}</div>
            <nav class="nav">
                <a href="/" class="active">{NOMBRE_INICIO}</a>
                <a href="/consultas">{NOMBRE_CONSULTAS}</a>
                <a href="/acerca">{NOMBRE_ACERCA}</a>
            </nav>
        </header>

        <!-- ===== CONTENIDO PRINCIPAL ===== -->
        <main class="main-container">
            <!-- BARRA LATERAL -->
            <aside class="sidebar">
                <h3>Menú</h3>
                <a href="/" class="menu-item active"><span class="icon">🏠</span> {NOMBRE_INICIO}</a>
                <a href="/consultas" class="menu-item"><span class="icon">📋</span> {NOMBRE_CONSULTAS}</a>
                <a href="/acerca" class="menu-item"><span class="icon">ℹ️</span> {NOMBRE_ACERCA}</a>
                <a href="/" class="menu-item"><span class="icon">➕</span> Nueva consulta</a>
                <a href="/" class="menu-item"><span class="icon">📊</span> Estadísticas</a>
                <a href="/" class="menu-item"><span class="icon">⚙️</span> Configuración</a>
            </aside>

            <!-- CONTENIDO -->
            <div class="content">
                <!-- BARRA DE BÚSQUEDA -->
                <div class="search-bar">
                    <input type="text" placeholder="Buscar consultas, temas o palabras clave..." id="buscar">
                    <button class="btn-search" onclick="alert('Función de búsqueda en desarrollo')">Buscar</button>
                </div>

                <!-- ESTADÍSTICAS -->
                <div class="stats-grid">
                    <div class="stat-card">
                        <span class="numero">0</span>
                        <span class="label">Total consultas</span>
                    </div>
                    <div class="stat-card">
                        <span class="numero">0</span>
                        <span class="label">Consultas respondidas</span>
                    </div>
                    <div class="stat-card">
                        <span class="numero">0</span>
                        <span class="label">Categorías activas</span>
                    </div>
                    <div class="stat-card">
                        <span class="numero">0</span>
                        <span class="label">Usuarios</span>
                    </div>
                </div>

                <!-- FORMULARIO -->
                <div class="content-card">
                    <h2>{TEXTO_FORMULARIO}</h2>
                    <p class="sub">{TEXTO_SUBFORMULARIO}</p>

                    <form action="/enviar-consulta" method="POST">
                        <div class="form-row">
                            <div class="form-group">
                                <label for="nombre">Nombre completo <span class="required">*</span></label>
                                <input type="text" id="nombre" name="nombre" placeholder="Ej. Hugo Cruz" required>
                            </div>
                            <div class="form-group">
                                <label for="categoria">Categoría</label>
                                <select id="categoria" name="categoria">
                                    {opciones_categorias}
                                </select>
                            </div>
                        </div>

                        <div class="form-group full">
                            <label for="pregunta">Pregunta <span class="required">*</span></label>
                            <textarea id="pregunta" name="pregunta" placeholder="Describa su consulta con claridad..." required></textarea>
                        </div>

                        <button type="submit" class="btn-submit">{TEXTO_BOTON}</button>
                    </form>

                    <!-- EJEMPLOS -->
                    <div style="margin-top: 28px; padding-top: 20px; border-top: 1.5px solid {COLOR_GRIS_BORDE};">
                        <h3 style="font-size:0.9rem; font-weight:500; color:{COLOR_AZUL}; margin-bottom:10px;">{TEXTO_EJEMPLOS}</h3>
                        <div class="examples-grid">
                            {ejemplos_html}
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <!-- ===== PIE DE PÁGINA ===== -->
        <footer class="footer">
            &copy; {TEXTO_AÑO} <span>{NOMBRE_SITIO}</span> &middot; {TEXTO_FOOTER}
        </footer>

        <script>
            document.querySelectorAll('.example-item').forEach(el => {{
                el.addEventListener('click', function() {{
                    const textarea = document.getElementById('pregunta');
                    textarea.focus();
                    textarea.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                }});
            }});
        </script>
    </body>
    </html>
    """
    return html


# ============================================================
# PÁGINA "MIS CONSULTAS"
# ============================================================
@app.route('/consultas')
def consultas():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{NOMBRE_CONSULTAS} - {NOMBRE_SITIO}</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        {generar_estilos()}
        <style>
            .empty-state {{
                text-align: center;
                padding: 40px 20px;
            }}
            .empty-state .icon {{ font-size: 3rem; color: {COLOR_DORADO}; display: block; margin-bottom: 12px; }}
            .empty-state h2 {{ color: {COLOR_AZUL}; font-weight: 600; font-size: 1.4rem; margin-bottom: 6px; }}
            .empty-state p {{ color: #4a6a7a; font-size: 1rem; }}
            .btn {{
                display: inline-block;
                margin-top: 18px;
                background: {COLOR_DORADO};
                color: {COLOR_BLANCO};
                padding: 12px 32px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.95rem;
                transition: background 0.25s;
            }}
            .btn:hover {{ background: {COLOR_DORADO_OSCURO}; }}
        </style>
    </head>
    <body>
        <header class="top-bar">
            <div class="logo">{NOMBRE_SITIO} <span>|</span> {TEXTO_BIENVENIDA}</div>
            <nav class="nav">
                <a href="/">{NOMBRE_INICIO}</a>
                <a href="/consultas" class="active">{NOMBRE_CONSULTAS}</a>
                <a href="/acerca">{NOMBRE_ACERCA}</a>
            </nav>
        </header>

        <main class="main-container">
            <aside class="sidebar">
                <h3>Menú</h3>
                <a href="/" class="menu-item"><span class="icon">🏠</span> {NOMBRE_INICIO}</a>
                <a href="/consultas" class="menu-item active"><span class="icon">📋</span> {NOMBRE_CONSULTAS}</a>
                <a href="/acerca" class="menu-item"><span class="icon">ℹ️</span> {NOMBRE_ACERCA}</a>
                <a href="/" class="menu-item"><span class="icon">➕</span> Nueva consulta</a>
                <a href="/" class="menu-item"><span class="icon">📊</span> Estadísticas</a>
                <a href="/" class="menu-item"><span class="icon">⚙️</span> Configuración</a>
            </aside>

            <div class="content">
                <div class="content-card empty-state">
                    <span class="icon">📋</span>
                    <h2>Aún no hay consultas</h2>
                    <p>Realice su primera consulta desde la página de inicio.</p>
                    <a href="/" class="btn">Ir al inicio</a>
                </div>
            </div>
        </main>

        <footer class="footer">
            &copy; {TEXTO_AÑO} <span>{NOMBRE_SITIO}</span> &middot; {TEXTO_FOOTER}
        </footer>
    </body>
    </html>
    """
    return html


# ============================================================
# PÁGINA "ACERCA DE"
# ============================================================
@app.route('/acerca')
def acerca():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{NOMBRE_ACERCA} - {NOMBRE_SITIO}</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        {generar_estilos()}
        <style>
            .about-content h2 {{ color: {COLOR_AZUL}; font-weight: 600; font-size: 1.3rem; margin-bottom: 10px; margin-top: 18px; }}
            .about-content p {{ color: #4a6a7a; line-height: 1.7; margin-bottom: 10px; }}
            .about-content ul {{ padding-left: 22px; color: #4a6a7a; line-height: 1.8; }}
            .about-content ul li {{ margin-bottom: 4px; }}
            .about-content .gold {{ color: {COLOR_DORADO}; font-weight: 600; }}
            .btn {{
                display: inline-block;
                margin-top: 12px;
                background: {COLOR_DORADO};
                color: {COLOR_BLANCO};
                padding: 12px 32px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.95rem;
                transition: background 0.25s;
            }}
            .btn:hover {{ background: {COLOR_DORADO_OSCURO}; }}
        </style>
    </head>
    <body>
        <header class="top-bar">
            <div class="logo">{NOMBRE_SITIO} <span>|</span> {TEXTO_BIENVENIDA}</div>
            <nav class="nav">
                <a href="/">{NOMBRE_INICIO}</a>
                <a href="/consultas">{NOMBRE_CONSULTAS}</a>
                <a href="/acerca" class="active">{NOMBRE_ACERCA}</a>
            </nav>
        </header>

        <main class="main-container">
            <aside class="sidebar">
                <h3>Menú</h3>
                <a href="/" class="menu-item"><span class="icon">🏠</span> {NOMBRE_INICIO}</a>
                <a href="/consultas" class="menu-item"><span class="icon">📋</span> {NOMBRE_CONSULTAS}</a>
                <a href="/acerca" class="menu-item active"><span class="icon">ℹ️</span> {NOMBRE_ACERCA}</a>
                <a href="/" class="menu-item"><span class="icon">➕</span> Nueva consulta</a>
                <a href="/" class="menu-item"><span class="icon">📊</span> Estadísticas</a>
                <a href="/" class="menu-item"><span class="icon">⚙️</span> Configuración</a>
            </aside>

            <div class="content">
                <div class="content-card about-content">
                    <h2>Acerca de <span class="gold">{NOMBRE_SITIO}</span></h2>
                    <p>
                        <span class="gold">{NOMBRE_SITIO}</span> es un sistema profesional de gestión de consultas 
                        diseñado para facilitar el acceso a información estructurada y precisa.
                    </p>

                    <h2>Características</h2>
                    <ul>
                        <li>Formulario de consultas con categorización</li>
                        <li>Almacenamiento seguro en base de datos PostgreSQL</li>
                        <li>Interfaz limpia y profesional</li>
                        <li>Diseño responsive para todos los dispositivos</li>
                    </ul>

                    <h2>Tecnologías</h2>
                    <ul>
                        <li>Python &middot; Flask &middot; PostgreSQL</li>
                        <li>HTML5 &middot; CSS3 &middot; Inter (tipografía)</li>
                        <li>Render (alojamiento en la nube)</li>
                    </ul>

                    <a href="/" class="btn">Volver al inicio</a>
                </div>
            </div>
        </main>

        <footer class="footer">
            &copy; {TEXTO_AÑO} <span>{NOMBRE_SITIO}</span> &middot; {TEXTO_FOOTER}
        </footer>
    </body>
    </html>
    """
    return html


# ============================================================
# RUTA PARA RECIBIR EL FORMULARIO
# ============================================================
@app.route('/enviar-consulta', methods=['POST'])
def enviar_consulta():
    nombre = request.form.get('nombre')
    categoria = request.form.get('categoria')
    pregunta = request.form.get('pregunta')

    # Convertir valor de categoría a texto
    nombre_categoria = categoria
    for cat in CATEGORIAS:
        if cat["valor"] == categoria:
            nombre_categoria = cat["texto"]
            break

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Consulta enviada - {NOMBRE_SITIO}</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
        {generar_estilos()}
        <style>
            .detail-box {{
                background: {COLOR_FONDO_DORADO};
                border-radius: 12px;
                padding: 20px 24px;
                margin: 16px 0 20px;
                text-align: left;
                border: 1px solid {COLOR_DORADO_CLARO};
            }}
            .detail-box p {{ margin: 6px 0; color: {COLOR_AZUL}; font-size: 0.95rem; }}
            .detail-box strong {{ color: {COLOR_AZUL}; font-weight: 600; }}
            .detail-box .gold-text {{ color: {COLOR_DORADO}; font-weight: 600; }}
            .btn {{
                display: inline-block;
                background: {COLOR_DORADO};
                color: {COLOR_BLANCO};
                padding: 12px 32px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.95rem;
                transition: background 0.25s;
            }}
            .btn:hover {{ background: {COLOR_DORADO_OSCURO}; }}
            .check {{ color: {COLOR_DORADO}; font-size: 2.8rem; display: block; margin-bottom: 8px; }}
        </style>
    </head>
    <body>
        <header class="top-bar">
            <div class="logo">{NOMBRE_SITIO} <span>|</span> {TEXTO_BIENVENIDA}</div>
            <nav class="nav">
                <a href="/">{NOMBRE_INICIO}</a>
                <a href="/consultas">{NOMBRE_CONSULTAS}</a>
                <a href="/acerca">{NOMBRE_ACERCA}</a>
            </nav>
        </header>

        <main class="main-container">
            <aside class="sidebar">
                <h3>Menú</h3>
                <a href="/" class="menu-item"><span class="icon">🏠</span> {NOMBRE_INICIO}</a>
                <a href="/consultas" class="menu-item"><span class="icon">📋</span> {NOMBRE_CONSULTAS}</a>
                <a href="/acerca" class="menu-item"><span class="icon">ℹ️</span> {NOMBRE_ACERCA}</a>
            </aside>

            <div class="content">
                <div class="content-card" style="text-align:center;">
                    <span class="check">✓</span>
                    <h2 style="color:{COLOR_AZUL};">Consulta enviada</h2>
                    <p class="sub" style="color:#4a6a7a;">Su consulta ha sido recibida correctamente.</p>

                    <div class="detail-box">
                        <p><strong>Nombre:</strong> {nombre}</p>
                        <p><strong>Categoría:</strong> <span class="gold-text">{nombre_categoria}</span></p>
                        <p><strong>Pregunta:</strong> {pregunta}</p>
                    </div>

                    <p style="color: #4a6a7a; margin-bottom: 16px; font-size: 0.95rem;">
                        En breve recibirá una respuesta a su consulta.
                    </p>
                    <a href="/" class="btn">Realizar otra consulta</a>
                </div>
            </div>
        </main>

        <footer class="footer">
            &copy; {TEXTO_AÑO} <span>{NOMBRE_SITIO}</span> &middot; {TEXTO_FOOTER}
        </footer>
    </body>
    </html>
    """
    return html


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)