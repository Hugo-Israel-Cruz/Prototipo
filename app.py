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