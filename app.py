from flask import Flask, request

app = Flask(__name__)

# ============================================================
# 🎨 ZONA DE PERSONALIZACIÓN
# ============================================================

# ---------- COLORES ----------
COLOR_DORADO = "#C9A84C"
COLOR_DORADO_OSCURO = "#B8943A"
COLOR_DORADO_BORDE = "#A07D2E"
COLOR_DORADO_CLARO = "#D4C08A"
COLOR_FONDO_DORADO = "#FFFFFF"

COLOR_AZUL = "#1A3A5C"
COLOR_AZUL_CLARO = "#2C5F8A"
COLOR_AZUL_OSCURO = "#0F1B33"

COLOR_BLANCO = "#FFFFFF"
COLOR_GRIS = "#F8F6F1"
COLOR_GRIS_BORDE = "#C9A84C"

# ---------- TEXTOS ----------
NOMBRE_SITIO = "JUSDATA"
TEXTO_BIENVENIDA = "Sistema de consultas"
TEXTO_FORMULARIO = "Nueva consulta"
TEXTO_SUBFORMULARIO = "Complete los campos para realizar su pregunta."
TEXTO_BOTON = "Enviar consulta"
TEXTO_EJEMPLOS = "Consultas de ejemplo"
TEXTO_FOOTER = "Sistema profesional de gestión de consultas"
TEXTO_AÑO = "2026"

# ---------- NOMBRES DEL MENÚ ----------
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

# ---------- EJEMPLOS ----------
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
# ESTILOS CSS
# ============================================================
def generar_estilos():
    return f"""
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 30px 20px;
            background: {COLOR_DORADO};
            background-image: 
                radial-gradient(ellipse at 10% 20%, rgba(255,255,255,0.08) 0%, transparent 60%),
                radial-gradient(ellipse at 90% 80%, rgba(255,255,255,0.06) 0%, transparent 50%),
                linear-gradient(135deg, {COLOR_DORADO} 0%, {COLOR_DORADO_OSCURO} 100%);
            position: relative;
        }}

        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: 
                repeating-linear-gradient(45deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 2px, transparent 2px, transparent 6px);
            pointer-events: none;
            z-index: 0;
        }}

        .main-wrapper {{
            max-width: 1200px;
            width: 100%;
            background: {COLOR_BLANCO};
            border-radius: 28px;
            box-shadow: 
                0 30px 80px rgba(0, 0, 0, 0.20),
                0 10px 30px rgba(0, 0, 0, 0.08);
            overflow: hidden;
            position: relative;
            z-index: 1;
            border: 1px solid {COLOR_DORADO_CLARO};
        }}

        .header {{
            background: {COLOR_AZUL};
            padding: 18px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 4px solid {COLOR_DORADO};
            position: relative;
        }}

        .header::after {{
            content: '';
            position: absolute;
            bottom: -4px;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, {COLOR_DORADO}, {COLOR_DORADO_CLARO}, {COLOR_DORADO});
            background-size: 200% 100%;
            animation: shimmer 4s ease-in-out infinite;
        }}

        @keyframes shimmer {{
            0%, 100% {{ background-position: -200% 0; }}
            50% {{ background-position: 200% 0; }}
        }}

        .logo {{
            font-size: 1.4rem;
            font-weight: 700;
            color: {COLOR_BLANCO};
            letter-spacing: -0.3px;
        }}

        .logo span {{
            color: {COLOR_DORADO};
        }}

        .nav {{
            display: flex;
            gap: 32px;
            font-weight: 500;
            font-size: 0.9rem;
        }}

        .nav a {{
            color: rgba(255, 255, 255, 0.75);
            text-decoration: none;
            transition: all 0.3s ease;
            padding: 6px 0;
            position: relative;
        }}

        .nav a::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background: {COLOR_DORADO};
            transition: width 0.3s ease;
        }}

        .nav a:hover {{
            color: {COLOR_BLANCO};
        }}

        .nav a:hover::after,
        .nav a.active::after {{
            width: 100%;
        }}

        .nav a.active {{
            color: {COLOR_BLANCO};
        }}

        .body-wrapper {{
            display: flex;
            gap: 0;
            background: {COLOR_GRIS};
            min-height: 500px;
            align-items: stretch;
        }}

        .sidebar {{
            width: 250px;
            min-width: 220px;
            background: {COLOR_AZUL_OSCURO};
            padding: 28px 20px;
            margin: 0;
            border-radius: 0;
            height: 100%;
            box-shadow: none;
            border: none;
            border-right: 3px solid {COLOR_DORADO};
        }}

        .sidebar h3 {{
            color: {COLOR_DORADO};
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 600;
            margin-bottom: 18px;
            padding-bottom: 12px;
            border-bottom: 1.5px solid rgba(201, 168, 76, 0.2);
        }}

        .sidebar .menu-item {{
            display: block;
            color: rgba(255, 255, 255, 0.7);
            text-decoration: none;
            padding: 10px 16px;
            border-radius: 10px;
            font-size: 0.88rem;
            font-weight: 450;
            transition: all 0.25s ease;
            margin-bottom: 3px;
        }}

        .sidebar .menu-item:hover {{
            background: rgba(201, 168, 76, 0.12);
            color: {COLOR_DORADO};
            transform: translateX(4px);
        }}

        .sidebar .menu-item.active {{
            background: {COLOR_DORADO};
            color: {COLOR_AZUL_OSCURO};
            font-weight: 600;
            box-shadow: 0 4px 16px rgba(201, 168, 76, 0.3);
        }}

        .sidebar .menu-item .icon {{
            margin-right: 12px;
            font-size: 1rem;
        }}

        .content {{
            flex: 1;
            padding: 28px 32px 32px 28px;
            background: {COLOR_GRIS};
        }}

        .search-bar {{
            background: {COLOR_BLANCO};
            border-radius: 14px;
            padding: 4px 4px 4px 20px;
            border: 2px solid {COLOR_DORADO_CLARO};
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 24px;
            transition: all 0.3s ease;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        }}

        .search-bar:focus-within {{
            border-color: {COLOR_DORADO};
            box-shadow: 0 4px 20px rgba(201, 168, 76, 0.15);
            transform: translateY(-1px);
        }}

        .search-bar input {{
            flex: 1;
            border: none;
            padding: 12px 0;
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
            padding: 11px 28px;
            border-radius: 12px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Inter', sans-serif;
            font-size: 0.85rem;
        }}

        .search-bar .btn-search:hover {{
            background: {COLOR_DORADO_OSCURO};
            transform: scale(1.02);
            box-shadow: 0 4px 16px rgba(201, 168, 76, 0.3);
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            margin-bottom: 28px;
        }}

        .stat-card {{
            background: {COLOR_BLANCO};
            border-radius: 14px;
            padding: 20px 16px;
            text-align: center;
            border: 1px solid {COLOR_DORADO_CLARO};
            transition: all 0.3s ease;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
        }}

        .stat-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 30px rgba(201, 168, 76, 0.15);
            border-color: {COLOR_DORADO};
        }}

        .stat-card .numero {{
            font-size: 2rem;
            font-weight: 700;
            color: {COLOR_DORADO};
            display: block;
            line-height: 1.2;
        }}

        .stat-card .label {{
            font-size: 0.8rem;
            color: {COLOR_AZUL};
            font-weight: 500;
            margin-top: 4px;
        }}

        .content-card {{
            background: {COLOR_BLANCO};
            border-radius: 16px;
            padding: 28px 32px 32px;
            border: 1px solid {COLOR_DORADO_CLARO};
            box-shadow: 0 2px 16px rgba(0, 0, 0, 0.04);
        }}

        .content-card h2 {{
            font-size: 1.2rem;
            font-weight: 600;
            color: {COLOR_AZUL};
            margin-bottom: 2px;
            letter-spacing: -0.3px;
        }}

        .content-card h2::after {{
            content: '';
            display: block;
            width: 40px;
            height: 3px;
            background: {COLOR_DORADO};
            margin-top: 6px;
            border-radius: 4px;
        }}

        .content-card .sub {{
            color: #6a7a8a;
            font-size: 0.9rem;
            margin-bottom: 20px;
            margin-top: 6px;
        }}

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
            padding: 11px 16px;
            border: 2px solid {COLOR_GRIS_BORDE};
            border-radius: 12px;
            font-family: 'Inter', sans-serif;
            font-size: 0.9rem;
            background: {COLOR_BLANCO};
            transition: all 0.3s ease;
            color: {COLOR_AZUL};
        }}

        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {{
            outline: none;
            border-color: {COLOR_DORADO};
            box-shadow: 0 0 0 4px rgba(201, 168, 76, 0.12);
            transform: translateY(-1px);
        }}

        .form-group textarea {{
            min-height: 90px;
            resize: vertical;
        }}

        .btn-submit {{
            background: {COLOR_DORADO};
            color: {COLOR_BLANCO};
            border: none;
            padding: 13px 32px;
            font-size: 0.95rem;
            font-weight: 600;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            font-family: 'Inter', sans-serif;
            letter-spacing: 0.3px;
        }}

        .btn-submit:hover {{
            background: {COLOR_DORADO_OSCURO};
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(201, 168, 76, 0.35);
        }}

        .examples-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
            gap: 12px;
            margin-top: 12px;
        }}

        .example-item {{
            background: {COLOR_GRIS};
            border: 2px solid {COLOR_GRIS_BORDE};
            border-radius: 12px;
            padding: 14px 16px;
            font-size: 0.82rem;
            color: {COLOR_AZUL};
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
            font-weight: 450;
        }}

        .example-item:hover {{
            border-color: {COLOR_DORADO};
            background: {COLOR_FONDO_DORADO};
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(201, 168, 76, 0.2);
        }}

        .example-item .cat {{
            display: block;
            font-size: 0.6rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: {COLOR_DORADO};
            margin-top: 5px;
        }}

        .separator {{
            border: none;
            border-top: 2px solid {COLOR_GRIS_BORDE};
            margin: 22px 0 18px 0;
        }}

        .footer {{
            background: {COLOR_AZUL_OSCURO};
            padding: 18px 40px;
            text-align: center;
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.8rem;
            border-top: 3px solid {COLOR_DORADO};
        }}

        .footer span {{
            color: {COLOR_DORADO};
            font-weight: 600;
        }}

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
                padding: 16px 24px;
                gap: 10px;
                text-align: center;
            }}
            .nav {{
                gap: 20px;
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
                margin: 0;
                padding: 18px 16px;
                display: flex;
                flex-wrap: wrap;
                gap: 4px;
                border-right: none;
                border-bottom: 3px solid {COLOR_DORADO};
                border-radius: 0;
            }}
            .sidebar h3 {{
                width: 100%;
                margin-bottom: 8px;
            }}
            .sidebar .menu-item {{
                padding: 8px 14px;
                font-size: 0.82rem;
                margin-bottom: 0;
            }}
            .content {{
                padding: 20px 16px 24px;
            }}
            .form-row {{
                grid-template-columns: 1fr;
                gap: 14px;
            }}
            .stats-grid {{
                grid-template-columns: 1fr 1fr;
                gap: 12px;
            }}
            .stat-card .numero {{
                font-size: 1.6rem;
            }}
            .content-card {{
                padding: 20px 18px 24px;
            }}
            .search-bar {{
                flex-wrap: wrap;
                padding: 12px 16px;
                gap: 10px;
            }}
            .search-bar .btn-search {{
                width: 100%;
                padding: 11px;
            }}
            .examples-grid {{
                grid-template-columns: 1fr 1fr;
            }}
            .footer {{
                padding: 16px 24px;
                font-size: 0.75rem;
            }}
        }}

        @media (max-width: 480px) {{
            .nav {{
                gap: 14px;
                font-size: 0.78rem;
            }}
            .stats-grid {{
                grid-template-columns: 1fr 1fr;
                gap: 10px;
            }}
            .stat-card {{
                padding: 14px 10px;
            }}
            .stat-card .numero {{
                font-size: 1.4rem;
            }}
            .examples-grid {{
                grid-template-columns: 1fr;
            }}
            .logo {{
                font-size: 1.1rem;
            }}
            .sidebar {{
                padding: 14px 12px;
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
        <div class="main-wrapper">
            <header class="header">
                <div class="logo">{NOMBRE_SITIO} <span>✦</span> {TEXTO_BIENVENIDA}</div>
                <nav class="nav">
                    <a href="/" class="active">{NOMBRE_INICIO}</a>
                    <a href="/consultas">{NOMBRE_CONSULTAS}</a>
                    <a href="/acerca">{NOMBRE_ACERCA}</a>
                </nav>
            </header>
            <div class="body-wrapper">
                <aside class="sidebar">
                    <h3>Menú principal</h3>
                    <a href="/" class="menu-item active"><span class="icon">◈</span> {NOMBRE_INICIO}</a>
                    <a href="/consultas" class="menu-item"><span class="icon">◈</span> {NOMBRE_CONSULTAS}</a>
                    <a href="/acerca" class="menu-item"><span class="icon">◈</span> {NOMBRE_ACERCA}</a>
                    <a href="#" class="menu-item" onclick="alert('Función en desarrollo')"><span class="icon">◈</span> Nueva consulta</a>
                    <a href="#" class="menu-item" onclick="alert('Función en desarrollo')"><span class="icon">◈</span> Estadísticas</a>
                    <a href="#" class="menu-item" onclick="alert('Función en desarrollo')"><span class="icon">◈</span> Configuración</a>
                </aside>
                <main class="content">
                    <div class="search-bar">
                        <input type="text" placeholder="Buscar consultas, temas o palabras clave..." id="buscar">
                        <button class="btn-search" onclick="alert('Función de búsqueda en desarrollo')">Buscar</button>
                    </div>
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
                    <div class="content-card">
                        <h2>{TEXTO_FORMULARIO}</h2>
                        <p class="sub">{TEXTO_SUBFORMULARIO}</p>
                        <form action="/enviar-consulta" method="POST">
                            <div class="form-row">
                                <div class="form-group">
                                    <label for="nombre">Nombre completo <span class="required">*</span></label>
                                    <input type="text" id="nombre" name="nombre" placeholder="Ej. Luis Torres" required>
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
                        <hr class="separator">
                        <h3 style="font-size:0.85rem; font-weight:600; color:{COLOR_AZUL}; margin-bottom:8px;">{TEXTO_EJEMPLOS}</h3>
                        <div class="examples-grid">
                            {ejemplos_html}
                        </div>
                    </div>
                </main>
            </div>
            <footer class="footer">
                &copy; {TEXTO_AÑO} <span>{NOMBRE_SITIO}</span> &middot; {TEXTO_FOOTER}
            </footer>
        </div>
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
            .empty-state .icon {{
                font-size: 3rem;
                color: {COLOR_DORADO};
                display: block;
                margin-bottom: 12px;
                opacity: 0.6;
            }}
            .empty-state h2 {{
                color: {COLOR_AZUL};
                font-weight: 600;
                font-size: 1.3rem;
                margin-bottom: 6px;
            }}
            .empty-state p {{
                color: #6a7a8a;
                font-size: 0.95rem;
            }}
            .btn {{
                display: inline-block;
                margin-top: 18px;
                background: {COLOR_DORADO};
                color: {COLOR_BLANCO};
                padding: 12px 32px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.9rem;
                transition: all 0.3s ease;
            }}
            .btn:hover {{
                background: {COLOR_DORADO_OSCURO};
                transform: translateY(-2px);
                box-shadow: 0 8px 30px rgba(201, 168, 76, 0.3);
            }}
        </style>
    </head>
    <body>
        <div class="main-wrapper">
            <header class="header">
                <div class="logo">{NOMBRE_SITIO} <span>✦</span> {TEXTO_BIENVENIDA}</div>
                <nav class="nav">
                    <a href="/">{NOMBRE_INICIO}</a>
                    <a href="/consultas" class="active">{NOMBRE_CONSULTAS}</a>
                    <a href="/acerca">{NOMBRE_ACERCA}</a>
                </nav>
            </header>
            <div class="body-wrapper">
                <aside class="sidebar">
                    <h3>Menú principal</h3>
                    <a href="/" class="menu-item"><span class="icon">◈</span> {NOMBRE_INICIO}</a>
                    <a href="/consultas" class="menu-item active"><span class="icon">◈</span> {NOMBRE_CONSULTAS}</a>
                    <a href="/acerca" class="menu-item"><span class="icon">◈</span> {NOMBRE_ACERCA}</a>
                    <a href="#" class="menu-item" onclick="alert('Función en desarrollo')"><span class="icon">◈</span> Nueva consulta</a>
                    <a href="#" class="menu-item" onclick="alert('Función en desarrollo')"><span class="icon">◈</span> Estadísticas</a>
                    <a href="#" class="menu-item" onclick="alert('Función en desarrollo')"><span class="icon">◈</span> Configuración</a>
                </aside>
                <main class="content">
                    <div class="content-card empty-state">
                        <span class="icon">◈</span>
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
            .about-content h2 {{
                color: {COLOR_AZUL};
                font-weight: 600;
                font-size: 1.2rem;
                margin-bottom: 8px;
                margin-top: 18px;
            }}
            .about-content h2:first-of-type {{
                margin-top: 0;
            }}
            .about-content h2::after {{
                content: '';
                display: block;
                width: 30px;
                height: 3px;
                background: {COLOR_DORADO};
                margin-top: 4px;
                border-radius: 4px;
            }}
            .about-content p {{
                color: #4a5a6a;
                line-height: 1.7;
                margin-bottom: 8px;
                font-size: 0.95rem;
            }}
            .about-content ul {{
                padding-left: 22px;
                color: #4a5a6a;
                line-height: 1.8;
                font-size: 0.95rem;
            }}
            .about-content ul li {{
                margin-bottom: 4px;
            }}
            .about-content .gold {{
                color: {COLOR_DORADO};
                font-weight: 600;
            }}
            .btn {{
                display: inline-block;
                margin-top: 16px;
                background: {COLOR_DORADO};
                color: {COLOR_BLANCO};
                padding: 12px 32px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.9rem;
                transition: all 0.3s ease;
            }}
            .btn:hover {{
                background: {COLOR_DORADO_OSCURO};
                transform: translateY(-2px);
                box-shadow: 0 8px 30px rgba(201, 168, 76, 0.3);
            }}
        </style>
    </head>
    <body>
        <div class="main-wrapper">
            <header class="header">
                <div class="logo">{NOMBRE_SITIO} <span>✦</span> {TEXTO_BIENVENIDA}</div>
                <nav class="nav">
                    <a href="/">{NOMBRE_INICIO}</a>
                    <a href="/consultas">{NOMBRE_CONSULTAS}</a>
                    <a href="/acerca" class="active">{NOMBRE_ACERCA}</a>
                </nav>
            </header>
            <div class="body-wrapper">
                <aside class="sidebar">
                    <h3>Menú principal</h3>
                    <a href="/" class="menu-item"><span class="icon">◈</span> {NOMBRE_INICIO}</a>
                    <a href="/consultas" class="menu-item"><span class="icon">◈</span> {NOMBRE_CONSULTAS}</a>
                    <a href="/acerca" class="menu-item active"><span class="icon">◈</span> {NOMBRE_ACERCA}</a>
                    <a href="#" class="menu-item" onclick="alert('Función en desarrollo')"><span class="icon">◈</span> Nueva consulta</a>
                    <a href="#" class="menu-item" onclick="alert('Función en desarrollo')"><span class="icon">◈</span> Estadísticas</a>
                    <a href="#" class="menu-item" onclick="alert('Función en desarrollo')"><span class="icon">◈</span> Configuración</a>
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
# RUTA PARA ENVIAR CONSULTA
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
            .detail-box p {{
                margin: 6px 0;
                color: {COLOR_AZUL};
                font-size: 0.95rem;
            }}
            .detail-box strong {{
                color: {COLOR_AZUL};
                font-weight: 600;
            }}
            .detail-box .gold-text {{
                color: {COLOR_DORADO};
                font-weight: 600;
            }}
            .btn {{
                display: inline-block;
                background: {COLOR_DORADO};
                color: {COLOR_BLANCO};
                padding: 12px 32px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: 600;
                font-size: 0.9rem;
                transition: all 0.3s ease;
            }}
            .btn:hover {{
                background: {COLOR_DORADO_OSCURO};
                transform: translateY(-2px);
                box-shadow: 0 8px 30px rgba(201, 168, 76, 0.3);
            }}
            .check {{
                color: {COLOR_DORADO};
                font-size: 2.8rem;
                display: block;
                margin-bottom: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="main-wrapper">
            <header class="header">
                <div class="logo">{NOMBRE_SITIO} <span>✦</span> {TEXTO_BIENVENIDA}</div>
                <nav class="nav">
                    <a href="/">{NOMBRE_INICIO}</a>
                    <a href="/consultas">{NOMBRE_CONSULTAS}</a>
                    <a href="/acerca">{NOMBRE_ACERCA}</a>
                </nav>
            </header>
            <div class="body-wrapper">
                <aside class="sidebar">
                    <h3>Menú principal</h3>
                    <a href="/" class="menu-item"><span class="icon">◈</span> {NOMBRE_INICIO}</a>
                    <a href="/consultas" class="menu-item"><span class="icon">◈</span> {NOMBRE_CONSULTAS}</a>
                    <a href="/acerca" class="menu-item"><span class="icon">◈</span> {NOMBRE_ACERCA}</a>
                </aside>
                <main class="content">
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
# EJECUTAR LA APLICACIÓN
# ============================================================
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)