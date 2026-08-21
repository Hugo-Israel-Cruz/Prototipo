# ============================================================
# 🎨 CONFIGURACIÓN - Colores, textos y datos
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
# 🔐 CONFIGURACIÓN DE SEGURIDAD
# ============================================================

SECRET_KEY = "clave-super-secreta-para-desarrollo-cambia-en-produccion"

# ============================================================
# 👑 CONFIGURACIÓN DE ADMINISTRADOR
# ============================================================

ADMIN_EMAIL = "admin@jusdata.com"
ADMIN_PASSWORD = "admin123"
ADMIN_NOMBRE = "Administrador JUSDATA"

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
    },
    "divorcios": {
        "titulo": "Estadística de Divorcios 2024",
        "descripcion": "Información sobre divorcios en México durante el año 2024. Datos del INEGI sobre causas, características de las personas divorciantes, duración del matrimonio y más.",
        "institucion": "Instituto Nacional de Estadística y Geografía (INEGI)",
        "categoria": "Legal / Demografía",
        "datos": {}
    }
}

# ============================================================
# 📊 DATOS DE DIVORCIOS (desde el PDF del INEGI)
# ============================================================

DATOS_DIVORCIOS = {
    "resumen": {
        "total_divorcios": 161932,
        "judiciales": 145091,
        "administrativos": 16841,
        "tasa_2024": 1.79,
        "tasa_2015": 1.52,
        "mujeres_hombres": 161249,
        "mujeres_mujeres": 439,
        "hombres_hombres": 244
    },
    "causas": [
        {"causa": "Divorcio incausado", "porcentaje": 67.2},
        {"causa": "Mutuo consentimiento", "porcentaje": 31.3},
        {"causa": "Separación del hogar por más de 1 año", "porcentaje": 0.8},
        {"causa": "Otras causas", "porcentaje": 0.7}
    ],
    "duracion_matrimonio": [
        {"rango": "Menos de 1 año", "porcentaje": 1.6},
        {"rango": "1 a 5 años", "porcentaje": 19.4},
        {"rango": "6 a 9 años", "porcentaje": 15.1},
        {"rango": "10 a 15 años", "porcentaje": 17.9},
        {"rango": "16 a 20 años", "porcentaje": 11.7},
        {"rango": "21 años y más", "porcentaje": 33.8}
    ],
    "edad_promedio": {
        "mujeres": 41.1,
        "hombres": 43.6
    },
    "hijos_menores": [
        {"rango": "Sin hijos", "porcentaje": 55.1},
        {"rango": "1 hijo/a", "porcentaje": 22.5},
        {"rango": "2 hijos/as", "porcentaje": 16.2},
        {"rango": "Más de 2", "porcentaje": 5.5},
        {"rango": "No especificado", "porcentaje": 0.7}
    ],
    "custodia": [
        {"rango": "A una de las partes", "porcentaje": 38.2},
        {"rango": "A ninguna", "porcentaje": 55.1},
        {"rango": "A ambas", "porcentaje": 5.9},
        {"rango": "No especificado", "porcentaje": 0.8}
    ],
    "patria_potestad": [
        {"rango": "A ambas partes", "porcentaje": 38.46},
        {"rango": "A una parte", "porcentaje": 5.69},
        {"rango": "A ninguna", "porcentaje": 55.13},
        {"rango": "No especificado", "porcentaje": 0.72}
    ],
    "pension_alimenticia": [
        {"rango": "A hijas/os", "porcentaje": 38.6},
        {"rango": "A cónyuge", "porcentaje": 0.0},
        {"rango": "No asignada", "porcentaje": 61.4}
    ],
    "escolaridad_mujeres": [
        {"nivel": "Preparatoria", "porcentaje": 19.4},
        {"nivel": "Secundaria", "porcentaje": 18.0},
        {"nivel": "Profesional", "porcentaje": 17.5},
        {"nivel": "Primaria", "porcentaje": 12.5},
        {"nivel": "Otra", "porcentaje": 32.6}
    ],
    "escolaridad_hombres": [
        {"nivel": "Preparatoria", "porcentaje": 19.7},
        {"nivel": "Secundaria", "porcentaje": 17.1},
        {"nivel": "Profesional", "porcentaje": 16.3},
        {"nivel": "Primaria", "porcentaje": 12.0},
        {"nivel": "Otra", "porcentaje": 34.9}
    ],
    "tasa_entidades": [
        {"entidad": "Campeche", "tasa": 4.89},
        {"entidad": "Nuevo León", "tasa": 3.52},
        {"entidad": "Tamaulipas", "tasa": 3.32},
        {"entidad": "Veracruz", "tasa": 0.91},
        {"entidad": "Chiapas", "tasa": 1.16},
        {"entidad": "Estado de México", "tasa": 1.21}
    ],
    "relacion_divorcios_matrimonios": [
        {"entidad": "Campeche", "relacion": 69.7},
        {"entidad": "Tamaulipas", "relacion": 66.2},
        {"entidad": "Nuevo León", "relacion": 58.8},
        {"entidad": "Veracruz", "relacion": 16.6},
        {"entidad": "Chiapas", "relacion": 19.8},
        {"entidad": "Jalisco", "relacion": 22.4}
    ],
    "condicion_actividad": {
        "mujeres_trabajan": 51.8,
        "mujeres_no_trabajan": 48.2,
        "hombres_trabajan": 67.9,
        "hombres_no_trabajan": 32.1
    }
}

# Asignar los datos de divorcios a la categoría
INFORMACION_CATEGORIAS["divorcios"]["datos"] = DATOS_DIVORCIOS