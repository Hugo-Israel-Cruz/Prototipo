
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


NOMBRE_SITIO = "JUSDATA"
TEXTO_BIENVENIDA = "Sistema de consultas"
TEXTO_FORMULARIO = "Nueva consulta"
TEXTO_SUBFORMULARIO = "Complete los campos para realizar su pregunta."
TEXTO_BOTON = "Enviar consulta"
TEXTO_EJEMPLOS = "Consultas de ejemplo"
TEXTO_FOOTER = "Sistema profesional de gestión de consultas"
TEXTO_AÑO = "2026"


NOMBRE_INICIO = "Inicio"
NOMBRE_CONSULTAS = "Mis consultas"
NOMBRE_ACERCA = "Acerca de"


CATEGORIAS = [
    {"valor": "general", "texto": "General"},
    {"valor": "tecnologia", "texto": "Tecnología"},
    {"valor": "educacion", "texto": "Educación"},
    {"valor": "salud", "texto": "Salud"},
    {"valor": "negocios", "texto": "Negocios"},
]


EJEMPLOS_CONSULTAS = [
    {"texto": "Fundamentos de programación orientada a objetos", "categoria": "Tecnología"},
    {"texto": "Cómo mejorar la productividad en el trabajo", "categoria": "Negocios"},
    {"texto": "Beneficios del aprendizaje continuo", "categoria": "Educación"},
    {"texto": "Cómo mantener una alimentación saludable", "categoria": "Salud"},
]

# ============================================================
# 🔐 CONFIGURACIÓN DE SEGURIDAD
# ============================================================

# Clave secreta para las sesiones (cambia esto)
SECRET_KEY = "clave-super-secreta-para-desarrollo-cambia-en-produccion"

# ============================================================
# 📊 DATOS DE CATEGORÍAS Y BASES DE DATOS
# ============================================================

INFORMACION_CATEGORIAS = {
    "tecnologia": {
        "titulo": "Tecnología",
        "descripcion": "Información sobre avances tecnológicos, programación e innovación.",
        "institucion": "Instituto de Innovación Tecnológica",
        "datos": [
            {"id": 1, "nombre": "Python", "descripcion": "Lenguaje de programación", "nivel": "Intermedio"},
            {"id": 2, "nombre": "Machine Learning", "descripcion": "Inteligencia artificial", "nivel": "Avanzado"},
            {"id": 3, "nombre": "Cloud Computing", "descripcion": "Computación en la nube", "nivel": "Intermedio"},
        ]
    },
    "negocios": {
        "titulo": "Negocios",
        "descripcion": "Estrategias empresariales, productividad y gestión organizacional.",
        "institucion": "Instituto de Estudios Empresariales",
        "datos": [
            {"id": 1, "nombre": "Productividad", "descripcion": "Métodos para mejorar eficiencia", "impacto": "Alto"},
            {"id": 2, "nombre": "Liderazgo", "descripcion": "Habilidades de gestión", "impacto": "Medio"},
        ]
    },
    "educacion": {
        "titulo": "Educación",
        "descripcion": "Métodos educativos, aprendizaje continuo y desarrollo académico.",
        "institucion": "Ministerio de Educación",
        "datos": [
            {"id": 1, "nombre": "Aprendizaje continuo", "descripcion": "Beneficios del estudio constante", "nivel": "Todos"},
            {"id": 2, "nombre": "Educación digital", "descripcion": "Herramientas tecnológicas", "nivel": "Intermedio"},
        ]
    },
    "salud": {
        "titulo": "Salud",
        "descripcion": "Información sobre bienestar, alimentación saludable y prevención.",
        "institucion": "Secretaría de Salud",
        "datos": [
            {"id": 1, "nombre": "Alimentación saludable", "descripcion": "Guía de nutrición", "categoria": "Prevención"},
            {"id": 2, "nombre": "Ejercicio físico", "descripcion": "Beneficios del deporte", "categoria": "Bienestar"},
        ]
    },
    "pensionados": {
        "titulo": "Fideicomisos (Fondos de pensiones)",
        "descripcion": "Información estadística respecto a los Fideicomisos relativos a Fondos de pensiones.",
        "institucion": "Instituto para Devolver al Pueblo lo Robado (INDEP)",
        "categoria": "Trabajo",
        "formato": "CSV",
        "ejercicio": "2026",
        "trimestre": "Segundo",
        "columnas": ["ejercicio", "trimestre", "mandato_encargo", "sexo", "mto_pension_min", "mto_pension_max", "per_monto", "edad_promedio", "tipo_moneda"],
        "datos": [
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPFINA", "sexo": "Mujer", "mto_pension_min": 43905.13, "mto_pension_max": 78686.0, "per_monto": "Mensual", "edad_promedio": 74.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPFINA", "sexo": "Hombre", "mto_pension_min": 143354.68, "mto_pension_max": 155051.99, "per_monto": "Mensual", "edad_promedio": 74.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPFINA", "sexo": "Mujer", "mto_pension_min": 34722.62, "mto_pension_max": 74333.31, "per_monto": "Mensual", "edad_promedio": 84.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPFINA", "sexo": "Hombre", "mto_pension_min": 125098.18, "mto_pension_max": 155445.67, "per_monto": "Mensual", "edad_promedio": 84.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPFINA", "sexo": "Mujer", "mto_pension_min": 123400.55, "mto_pension_max": 123400.55, "per_monto": "Mensual", "edad_promedio": 93.0, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPFINA", "sexo": "Hombre", "mto_pension_min": 114279.68, "mto_pension_max": 114279.68, "per_monto": "Mensual", "edad_promedio": 93.0, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPBNCI", "sexo": "Mujer", "mto_pension_min": 14945.6, "mto_pension_max": 14945.6, "per_monto": "Mensual", "edad_promedio": 67.0, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPBNCI", "sexo": "Hombre", "mto_pension_min": 14373.7, "mto_pension_max": 14373.7, "per_monto": "Mensual", "edad_promedio": 67.0, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPBNCI", "sexo": "Mujer", "mto_pension_min": 14373.7, "mto_pension_max": 14373.7, "per_monto": "Mensual", "edad_promedio": 72.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPBNCI", "sexo": "Hombre", "mto_pension_min": 27501.46, "mto_pension_max": 27501.46, "per_monto": "Mensual", "edad_promedio": 87.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPBNCI", "sexo": "Hombre", "mto_pension_min": 18308.68, "mto_pension_max": 18308.68, "per_monto": "Mensual", "edad_promedio": 97.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPIL", "sexo": "Mujer", "mto_pension_min": 22903.08, "mto_pension_max": 219486.88, "per_monto": "Mensual", "edad_promedio": 85.0, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPBANPESCA", "sexo": "Mujer", "mto_pension_min": 16811.54, "mto_pension_max": 23984.03, "per_monto": "Mensual", "edad_promedio": 85.0, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPBANPESCA", "sexo": "Hombre", "mto_pension_min": 14373.7, "mto_pension_max": 14373.7, "per_monto": "Mensual", "edad_promedio": 88.0, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPBANPESCA", "sexo": "Mujer", "mto_pension_min": 19762.37, "mto_pension_max": 19762.37, "per_monto": "Mensual", "edad_promedio": 93.0, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPBANPESCA", "sexo": "Mujer", "mto_pension_min": 14373.7, "mto_pension_max": 17749.0, "per_monto": "Mensual", "edad_promedio": 95.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPMANTE", "sexo": "Hombre", "mto_pension_min": 1267.48, "mto_pension_max": 5129.27, "per_monto": "Mensual", "edad_promedio": 70.0, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPMANTE", "sexo": "Mujer", "mto_pension_min": 1456.1, "mto_pension_max": 1456.1, "per_monto": "Mensual", "edad_promedio": 75.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPMANTE", "sexo": "Hombre", "mto_pension_min": 12240.16, "mto_pension_max": 12240.16, "per_monto": "Mensual", "edad_promedio": 85.5, "tipo_moneda": "Moneda Nacional"},
            {"ejercicio": 2026, "trimestre": "Segundo", "mandato_encargo": "FPMANTE", "sexo": "Mujer", "mto_pension_min": 2450.68, "mto_pension_max": 2450.68, "per_monto": "Mensual", "edad_promedio": 95.5, "tipo_moneda": "Moneda Nacional"},
        ]
    }
}