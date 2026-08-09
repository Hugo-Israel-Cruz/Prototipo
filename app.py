from flask import Flask, request

app = Flask(__name__)

# ============================================================
# 🎨 ZONA DE PERSONALIZACIÓN - EDITA AQUÍ LOS COLORES Y TEXTOS
# ============================================================

# ---------- COLORES PRINCIPALES ----------
COLOR_DORADO = "#C9A84C"        # Dorado principal
COLOR_DORADO_OSCURO = "#B8943A"  # Dorado más oscuro
COLOR_DORADO_BORDE = "#A07D2E"   # Borde de elementos
COLOR_DORADO_CLARO = "#D4C08A"   # Dorado claro para bordes suaves
COLOR_FONDO_DORADO = "#F5EDD6"   # Fondo dorado muy claro para detalles

COLOR_AZUL = "#1A3A5C"          # Azul principal
COLOR_AZUL_CLARO = "#2C5F8A"     # Azul más claro
COLOR_AZUL_OSCURO = "#0F1B33"    # Azul muy oscuro

COLOR_BLANCO = "#FFFFFF"        # Blanco para fondos
COLOR_GRIS = "#F8F6F1"          # Gris suave para fondos secundarios
COLOR_GRIS_BORDE = "#E8DFC8"    # Gris para bordes

# ---------- TEXTOS EDITABLES ----------
NOMBRE_SITIO = "ConsultaRápida"
TEXTO_BIENVENIDA = "Sistema de consultas"
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

# ---------- CATEGORÍAS ----------
CATEGORIAS = [
    {"valor": "general", "texto": "General"},
    {"valor": "tecnologia", "texto": "Tecnología"},
    {"valor": "educacion", "texto": "Educación"},
    {"valor": "salud", "texto": "Salud"},
    {"valor": "negocios", "texto": "Negocios"},
]

# ---------- EJEMPLOS DE CONSULTAS ----------
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
# FUNCIÓN PARA GENERAR ESTILOS CSS
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
            justify-content: center;
            align-items: center;
            padding: 30px 20px;
        }}

        /* ========================================
           CONTENEDOR PRINCIPAL (blanco central)
           TODO el contenido va dentro de este
        ======================================== */
        .main-wrapper {{
            max-width: 1200px;
            width: 100%;
            background: {COLOR_BLANCO};
            border-radius: 24px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
            overflow: hidden;
            border: 1px solid {COLOR_DORADO_CLARO};
        }}

        /* ========================================
           ENCABEZADO (dentro del contenedor blanco)
        ======================================== */
        .header {{
            background: {COLOR_AZUL};
            padding: 16px 32px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 3px solid {COLOR_DORADO};
        }}

        .logo {{
            font-size: 1.3rem;
            font-weight: 700;
            color: {COLOR_BLANCO};
            letter-spacing: -0.3px;
        }}

        .logo span {{
            color: {COLOR_DORADO};
        }}

        .nav {{
            display: flex;
            gap: 28px;
            font-weight: 500;
            font-size: 0.9rem;
        }}

        .nav a {{
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
            transition: color 0.2s;
            padding: 4px 0;
            border-bottom: 2px solid transparent;
        }}

        .nav a:hover,
        .nav a.active {{
            color: {COLOR_DORADO};
            border-bottom-color: {COLOR_DORADO};
        }}

        /* ========================================
           CUERPO: SIDEBAR + CONTENIDO
        ======================================== */
        .body-wrapper {{
            display: flex;
            gap: 0;
            background: {COLOR_GRIS};
        }}

        /* ========================================
           BARRA LATERAL (azul oscuro)
        ======================================== */
        .sidebar {{
            width: 220px;
            min-width: 200px;
            background: {COLOR_AZUL_OSCURO};
            padding: 24px 16px;
            height: 100%;
        }}

        .sidebar h3 {{
            color: {COLOR_DORADO};
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 600;
            margin-bottom: 16px;
            padding-bottom: 10px;
            border-bottom: 1.5px solid rgba(201, 168, 76, 0.25);
        }}

        .sidebar .menu-item {{
            display: block;
            color: rgba(255, 255, 255, 0.75);
            text-decoration: none;
            padding: 10px 14px;
            border-radius: 10px;
            font-size: 0.88rem;
            font-weight: 450;
            transition: all 0.2s;
            margin-bottom: 4px;
        }}

        .sidebar .menu-item:hover {{
            background: rgba(201, 168, 76, 0.12);
            color: {COLOR_DORADO};
        }}

        .sidebar .menu-item.active {{
            background: {COLOR_DORADO};
            color: {COLOR_AZUL_OSCURO};
            font-weight: 600;
        }}

        .sidebar .menu-item .icon {{
            margin-right: 10px;
            font-size: 1rem;
        }}

        /* ========================================
           CONTENIDO PRINCIPAL
        ======================================== */
        .content {{
            flex: 1;
            padding: 28px 32px 32px;
            background: {COLOR_BLANCO};
        }}

        /* ========================================
           BARRA DE BÚSQUEDA
        ======================================== */
        .search-bar {{
            background: {COLOR_GRIS};
            border-radius: 12px;
            padding: 6px 6px 6px 18px;
            border: 1.5px solid {COLOR_DORADO_CLARO};
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 24px;
            transition: border-color 0.2s;
        }}

        .search-bar:focus-within {{
            border-color: {COLOR_DORADO};
        }}

        .search-bar input {{
            flex: 1;
            border: none;
            padding: 11px 0;
            font-size: 0.9rem;
            font-family: 'Inter', sans-serif;
            color: {COLOR_AZUL};
            background: transparent;
            outline: none;
        }}

        .search-bar input::placeholder {{
            color: #aaa;
        }}

        .search-bar .btn-search {{
            background: {COLOR_DORADO};
            color: {COLOR_BLANCO};
            border: none;
            padding: 10px 22px;
            border-radius: 10px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.25s;
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
        }}

        .search-bar .btn-search:hover {{
            background: {COLOR_DORADO_OSCURO};
        }}

        /* ========================================
           ESTADÍSTICAS
        ======================================== */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 14px;
            margin-bottom: 28px;
        }}

        .stat-card {{
            background: {COLOR_GRIS};
            border-radius: 12px;
            padding: 18px 14px;
            text-align: center;
            border: 1px solid {COLOR_DORADO_CLARO};
            transition: transform 0.2s;
        }}

        .stat-card:hover {{
            transform: translateY(-3px);
        }}

        .stat-card .numero {{
            font-size: 1.8rem;
            font-weight: 700;
            color: {COLOR_DORADO};
            display: block;
            line-height: 1.2;
        }}

        .stat-card .label {{
            font-size: 0.78rem;
            color: {COLOR_AZUL};
            font-weight: 500;
            margin-top: 2px;
        }}

        /* ========================================
           TARJETA DE CONTENIDO (formulario)
        ======================================== */
        .content-card {{
            background: {COLOR_GRIS};
            border-radius: 14px;
            padding: 24px 28px 28px;
            border: 1px solid {COLOR_DORADO_CLARO};
        }}

        .content-card h2 {{
            font-size: 1.15rem;
            font-weight: 600;
            color: {COLOR_AZUL};
            margin-bottom: 2px;
            letter-spacing: -0.3px;
        }}

        .content-card .sub {{
            color: #6a7a8a;
            font-size: 0.9rem;
            margin-bottom: 18px;
        }}

        /* ========================================
           FORMULARIO
        ======================================== */
        .form-row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 14px;
        }}

        .form-group {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .form-group.full {{
            grid-column: 1 / -1;
        }}

        .form-group label {{
            font-weight: 500;
            font-size: 0.82rem;
            color: {COLOR_AZUL};
        }}

        .form-group label .required {{
            color: #c0392b;
            font-weight: 400;
        }}

        .form-group input,
        .form-group select,
        .form-group textarea {{
            padding: 10px 14px;
            border: 1.5px solid {COLOR_DORADO_CLARO};
            border-radius: 10px;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            background: {COLOR_BLANCO};
            transition: border-color 0.25s, box-shadow 0.25s;
            color: {COLOR_AZUL};
        }}

        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {{
            outline: none;
            border-color: {COLOR_DORADO};
            box-shadow: 0 0 0 4px rgba(201, 168, 76, 0.12);
        }}

        .form-group textarea {{
            min-height: 85px;
            resize: vertical;
        }}

        .btn-submit {{
            background: {COLOR_DORADO};
            color: {COLOR_BLANCO};
            border: none;
            padding: 12px 28px;
            font-size: 0.95rem;
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
            margin-top: 10px;
        }}

        .example-item {{
            background: {COLOR_BLANCO};
            border: 1.5px solid {COLOR_DORADO_CLARO};
            border-radius: 10px;
            padding: 12px 14px;
            font-size: 0.82rem;
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
            font-size: 0.6rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: {COLOR_DORADO};
            margin-top: 4px;
        }}

        /* ========================================
           SEPARADOR
        ======================================== */
        .separator {{
            border: none;
            border-top: 1.5px solid {COLOR_DORADO_CLARO};
            margin: 22px 0 16px 0;
        }}

        /* ========================================
           PIE DE PÁGINA (dentro del contenedor blanco)
        ======================================== */
        .footer {{
            background: {COLOR_AZUL_OSCURO};
            padding: 16px 32px;
            text-align: center;
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.8rem;
            border-top: 2px solid {COLOR_DORADO};
        }}

        .footer span {{
            color: {COLOR_DORADO};
            font-weight: 600;
        }}

        /* ========================================
           RESPONSIVE
        ======================================== */
        @media (max-width: 992px) {{
            .stats-grid {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 16px 12px;
            }}

            .header {{
                flex-direction: column;
                padding: 14px 20px;
                gap: 8px;
                text-align: center;
            }}

            .nav {{
                gap: 18px;
                font-size: 0.85rem;
                flex-wrap: wrap;
                justify-content: center;
            }}

            .body-wrapper {{
                flex-direction: column;
            }}

            .sidebar {{
                width: 100%;
                min-width: unset;
                display: flex;
                flex-wrap: wrap;
                gap: 4px;
                padding: 14px 18px;
            }}

            .sidebar h3 {{
                width: 100%;
                margin-bottom: 6px;
            }}

            .sidebar .menu-item {{
                padding: 7px 14px;
                font-size: 0.82rem;
                margin-bottom: 0;
            }}

            .content {{
                padding: 20px 16px 24px;
            }}

            .form-row {{
                grid-template-columns: 1fr;
                gap: 12px;
            }}

            .stats-grid {{
                grid-template-columns: 1fr 1fr;
                gap: 10px;
            }}

            .stat-card .numero {{
                font-size: 1.5rem;
            }}

            .content-card {{
                padding: 18px 16px 20px;
            }}

            .search-bar {{
                flex-wrap: wrap;
                padding: 10px 12px;
                gap: 8px;
            }}

            .search-bar .btn-search {{
                width: 100%;
                padding: 10px;
            }}

            .examples-grid {{
                grid-template-columns: 1fr 1fr;
            }}

            .footer {{
                padding: 14px 20px;
                font-size: 0.75rem;
            }}
        }}

        @media (max-width: 480px) {{
            .nav {{
                gap: 12px;
                font-size: 0.78rem;
            }}

            .stats-grid {{
                grid-template-columns: 1fr 1fr;
                gap: 8px;
            }}

            .stat-card {{
                padding: 12px 8px;
            }}

            .stat-card .numero {{
                font-size: 1.3rem;
            }}

            .examples-grid {{
                grid-template-columns: 1fr;
            }}

            .logo {{
                font-size: 1.1rem;
            }}
        }}
    </style>
    """


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================
@app.route('/')
def inicio():
    opciones_categorias = ""
    for cat in CATEGORIAS:
        opciones_categorias += f'<option value="{cat["valor"]}">{cat["texto"]}</option>'

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

        <!-- ========================================
             CONTENEDOR BLANCO CENTRAL
             TODO EL CONTENIDO DENTRO DE ÉL
        ======================================== -->
        <div class="main-wrapper">

            <!-- ENCABEZADO -->
            <header class="header">
                <div class="logo">{NOMBRE_SITIO} <span>|</span> {TEXTO_BIENVENIDA}</div>
                <nav class="nav">
                    <a href="/" class="active">{NOMBRE_INICIO}</a>
                    <a href="/consultas">{NOMBRE_CONSULTAS}</a>
                    <a href="/acerca">{NOMBRE_ACERCA}</a>
                </nav>
            </header>

            <!-- CUERPO: SIDEBAR + CONTENIDO -->
            <div class="body-wrapper">

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

                <!-- CONTENIDO PRINCIPAL -->
                <main class="content">

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
                        <hr class="separator">
                        <h3 style="font-size:0.85rem; font-weight:500; color:{COLOR_AZUL}; margin-bottom:8px;">{TEXTO_EJEMPLOS}</h3>
                        <div class="examples-grid">
                            {ejemplos_html}
                        </div>
                    </div>

                </main>
            </div>

            <!-- PIE DE PÁGINA -->
            <footer class="footer">
                &copy; {TEXTO_AÑO} <span>{NOMBRE_SITIO}</span> &middot; {TEXTO_FOOTER}
            </footer>

        </div>
        <!-- FIN CONTENEDOR BLANCO CENTRAL -->

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
                padding: 30px 10px;
            }}
            .empty-state .icon {{ font-size: 2.8rem; color: {COLOR_DORADO}; display: block; margin-bottom: 10px; }}
            .empty-state h2 {{ color: {COLOR_AZUL}; font-weight: 600; font-size: 1.3rem; margin-bottom: 4px; }}
            .empty-state p {{ color: #6a7a8a; font-size: 0.95rem; }}
            .btn {{
                display: inline-block;
                margin-top: 16px;
                background: {COLOR_DORADO};
                color: {COLOR_BLANCO};
                padding: 11px 28px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.9rem;
                transition: background 0.25s;
            }}
            .btn:hover {{ background: {COLOR_DORADO_OSCURO}; }}
        </style>
    </head>
    <body>
        <div class="main-wrapper">
            <header class="header">
                <div class="logo">{NOMBRE_SITIO} <span>|</span> {TEXTO_BIENVENIDA}</div>
                <nav class="nav">
                    <a href="/">{NOMBRE_INICIO}</a>
                    <a href="/consultas" class="active">{NOMBRE_CONSULTAS}</a>
                    <a href="/acerca">{NOMBRE_ACERCA}</a>
                </nav>
            </header>

            <div class="body-wrapper">
                <aside class="sidebar">
                    <h3>Menú</h3>
                    <a href="/" class="menu-item"><span class="icon">🏠</span> {NOMBRE_INICIO}</a>
                    <a href="/consultas" class="menu-item active"><span class="icon">📋</span> {NOMBRE_CONSULTAS}</a>
                    <a href="/acerca" class="menu-item"><span class="icon">ℹ️</span> {NOMBRE_ACERCA}</a>
                    <a href="/" class="menu-item"><span class="icon">➕</span> Nueva consulta</a>
                    <a href="/" class="menu-item"><span class="icon">📊</span> Estadísticas</a>
                    <a href="/" class="menu-item"><span class="icon">⚙️</span> Configuración</a>
                </aside>

                <main class="content">
                    <div class="content-card empty-state">
                        <span class="icon">📋</span>
                        <h2>Aún no hay consultas</h2>
                        <p>Realice su primera consulta desde la página de inicio.</p>
                        <a href="/" class="btn">Ir al inicio</a>
                    </div>
                </main>
            </div>

            <footer class="footer">
                &copy; {TEXTO_AÑO} <span>{NOMBRE_SITIO}</span> &middot; {TEXTO_FOOTER}
            </footer>
        </div>
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
            .about-content h2 {{ color: {COLOR_AZUL}; font-weight: 600; font-size: 1.2rem; margin-bottom: 8px; margin-top: 16px; }}
            .about-content p {{ color: #4a5a6a; line-height: 1.7; margin-bottom: 8px; font-size: 0.95rem; }}
            .about-content ul {{ padding-left: 22px; color: #4a5a6a; line-height: 1.8; font-size: 0.95rem; }}
            .about-content ul li {{ margin-bottom: 3px; }}
            .about-content .gold {{ color: {COLOR_DORADO}; font-weight: 600; }}
            .btn {{
                display: inline-block;
                margin-top: 12px;
                background: {COLOR_DORADO};
                color: {COLOR_BLANCO};
                padding: 11px 28px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.9rem;
                transition: background 0.25s;
            }}
            .btn:hover {{ background: {COLOR_DORADO_OSCURO}; }}
        </style>
    </head>
    <body>
        <div class="main-wrapper">
            <header class="header">
                <div class="logo">{NOMBRE_SITIO} <span>|</span> {TEXTO_BIENVENIDA}</div>
                <nav class="nav">
                    <a href="/">{NOMBRE_INICIO}</a>
                    <a href="/consultas">{NOMBRE_CONSULTAS}</a>
                    <a href="/acerca" class="active">{NOMBRE_ACERCA}</a>
                </nav>
            </header>

            <div class="body-wrapper">
                <aside class="sidebar">
                    <h3>Menú</h3>
                    <a href="/" class="menu-item"><span class="icon">🏠</span> {NOMBRE_INICIO}</a>
                    <a href="/consultas" class="menu-item"><span class="icon">📋</span> {NOMBRE_CONSULTAS}</a>
                    <a href="/acerca" class="menu-item active"><span class="icon">ℹ️</span> {NOMBRE_ACERCA}</a>
                    <a href="/" class="menu-item"><span class="icon">➕</span> Nueva consulta</a>
                    <a href="/" class="menu-item"><span class="icon">📊</span> Estadísticas</a>
                    <a href="/" class="menu-item"><span class="icon">⚙️</span> Configuración</a>
                </aside>

                <main class="content">
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
                </main>
            </div>

            <footer class="footer">
                &copy; {TEXTO_AÑO} <span>{NOMBRE_SITIO}</span> &middot; {TEXTO_FOOTER}
            </footer>
        </div>
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
                background: {COLOR_GRIS};
                border-radius: 12px;
                padding: 18px 22px;
                margin: 14px 0 18px;
                text-align: left;
                border: 1px solid {COLOR_DORADO_CLARO};
            }}
            .detail-box p {{ margin: 