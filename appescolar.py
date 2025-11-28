import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import random
import io
import base64

# ← ¡YA NO NECESITAS NINGUNA LÍNEA DE FPDF AQUÍ!
# ← reportlab se importa DENTRO de la función generar_certificado_pdf
#    (así Streamlit Cloud no se queja al inicio)

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================
st.set_page_config(
    page_title="Sistema Escolar Interactivo",
    page_icon="🏫",
    layout="wide"
)

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================
st.set_page_config(
    page_title="Sistema Escolar Interactivo",
    page_icon="🏫",
    layout="wide"
)

# ============================================
# DATOS DE ESTUDIANTES - COLEGIO CARLOS GIRALDO
# ============================================
data_carlos_giraldo = [
    ["Alejandro Vargas", 13579246, "Matemáticas", 4.5, 8], 
    ["Alejandro Vargas", 13579246, "Español", 7.2, 9],
    ["Alejandro Vargas", 13579246, "Inglés", 6.8, 7], 
    ["Alejandro Vargas", 13579246, "Ciencias", 5.9, 8],
    ["Beatriz Morales", 24681357, "Matemáticas", 8.1, 10], 
    ["Beatriz Morales", 24681357, "Español", 9.0, 10],
    ["Beatriz Morales", 24681357, "Inglés", 7.5, 9], 
    ["Beatriz Morales", 24681357, "Ciencias", 8.8, 10],
    ["Carlos Mendoza", 35792468, "Matemáticas", 6.4, 7], 
    ["Carlos Mendoza", 35792468, "Español", 5.8, 6],
    ["Carlos Mendoza", 35792468, "Inglés", 8.2, 9], 
    ["Carlos Mendoza", 35792468, "Ciencias", 7.0, 8],
    ["Daniela Ortiz", 46813579, "Matemáticas", 3.8, 5], 
    ["Daniela Ortiz", 46813579, "Español", 6.5, 8],
    ["Daniela Ortiz", 46813579, "Inglés", 5.0, 6], 
    ["Daniela Ortiz", 46813579, "Ciencias", 4.2, 4],
    ["Eduardo Navarro", 57924680, "Matemáticas", 9.2, 10], 
    ["Eduardo Navarro", 57924680, "Español", 8.7, 9],
    ["Eduardo Navarro", 57924680, "Inglés", 9.5, 10], 
    ["Eduardo Navarro", 57924680, "Ciencias", 8.9, 10],
]

# ============================================
# DATOS DE ESTUDIANTES - INSTITUTO OLGA SANTAMARÍA
# ============================================
data_olga_santamaria = [
    ["Fernanda Pérez", 68035791, "Matemáticas", 7.9, 9], 
    ["Fernanda Pérez", 68035791, "Español", 8.8, 10],
    ["Fernanda Pérez", 68035791, "Inglés", 9.0, 10], 
    ["Fernanda Pérez", 68035791, "Ciencias", 8.5, 9],
    ["Gabriel Quintana", 79146802, "Matemáticas", 5.3, 7], 
    ["Gabriel Quintana", 79146802, "Español", 7.6, 9],
    ["Gabriel Quintana", 79146802, "Inglés", 6.1, 8], 
    ["Gabriel Quintana", 79146802, "Ciencias", 6.8, 7],
    ["Helena Ruiz", 80257913, "Matemáticas", 8.5, 10], 
    ["Helena Ruiz", 80257913, "Español", 7.3, 8],
    ["Helena Ruiz", 80257913, "Inglés", 8.9, 10], 
    ["Helena Ruiz", 80257913, "Ciencias", 7.7, 9],
    ["Ignacio Salazar", 91368024, "Matemáticas", 6.7, 8], 
    ["Ignacio Salazar", 91368024, "Español", 5.5, 6],
    ["Ignacio Salazar", 91368024, "Inglés", 7.4, 9], 
    ["Ignacio Salazar", 91368024, "Ciencias", 6.9, 8],
    ["Juliana Torres", 2479135, "Matemáticas", 9.0, 10], 
    ["Juliana Torres", 2479135, "Español", 8.6, 9],
    ["Juliana Torres", 2479135, "Inglés", 9.3, 10], 
    ["Juliana Torres", 2479135, "Ciencias", 8.8, 10],
]

# Crear DataFrames
columns = ["Nombre", "Cedula", "Asignatura", "Nota_Parcial", "Nota_Final"]
df_carlos_giraldo = pd.DataFrame(data_carlos_giraldo, columns=columns)
df_carlos_giraldo["Colegio"] = "Colegio Departamental Carlos Giraldo"

df_olga_santamaria = pd.DataFrame(data_olga_santamaria, columns=columns)
df_olga_santamaria["Colegio"] = "Instituto Técnico Olga Santamaría"

# DataFrame combinado
df_all_students = pd.concat([df_carlos_giraldo, df_olga_santamaria], ignore_index=True)

# ============================================
# DATOS DE PROFESORES
# ============================================
profesores_data = {
    "Colegio Departamental Carlos Giraldo": [
        {"nombre": "Prof. María García", "cedula": 11111111, "asignatura": "Matemáticas"},
        {"nombre": "Prof. Juan López", "cedula": 22222222, "asignatura": "Español"},
        {"nombre": "Prof. Ana Martínez", "cedula": 33333333, "asignatura": "Inglés"},
        {"nombre": "Prof. Pedro Sánchez", "cedula": 44444444, "asignatura": "Ciencias"},
    ],
    "Instituto Técnico Olga Santamaría": [
        {"nombre": "Prof. Laura Rodríguez", "cedula": 55555555, "asignatura": "Matemáticas"},
        {"nombre": "Prof. Carlos Hernández", "cedula": 66666666, "asignatura": "Español"},
        {"nombre": "Prof. Diana Gómez", "cedula": 77777777, "asignatura": "Inglés"},
        {"nombre": "Prof. Roberto Díaz", "cedula": 88888888, "asignatura": "Ciencias"},
    ]
}

# ============================================
# INFORMACIÓN ESCOLAR
# ============================================
info_escolar = {
    "calendario_academico": """
📅 **CALENDARIO ACADÉMICO 2024-2025**

**Primer Semestre:**
- Inicio de clases: 22 de Enero 2024
- Semana de receso: 25-29 de Marzo (Semana Santa)
- Fin primer período: 12 de Abril
- Entrega de boletines: 19 de Abril
- Fin segundo período: 14 de Junio
- Vacaciones mitad de año: 17 Junio - 7 Julio

**Segundo Semestre:**
- Inicio segundo semestre: 8 de Julio
- Semana de receso: 7-11 de Octubre
- Fin tercer período: 13 de Septiembre
- Fin cuarto período: 22 de Noviembre
- Clausura: 29 de Noviembre
    """,
    
    "matriculas": """
📋 **INFORMACIÓN DE MATRÍCULAS**

**Fechas de matrícula 2025:**
- Estudiantes antiguos: 1-15 de Noviembre 2024
- Estudiantes nuevos: 18-30 de Noviembre 2024

**Requisitos:**
1. Fotocopia documento de identidad
2. Certificado de estudios anteriores
3. Fotos 3x4 fondo azul (2 unidades)
4. Certificado médico
5. Paz y salvo año anterior

**Costos:**
- Matrícula: $150.000
- Pensión mensual: $180.000
- Seguro estudiantil: $45.000/año
    """,
    
    "actividades_escolares": """
🎭 **ACTIVIDADES ESCOLARES 2024**

**Próximos eventos:**
- 15 Feb: Día del Amor y la Amistad
- 8 Mar: Día de la Mujer
- 23 Abr: Día del Idioma
- 30 Abr: Día del Niño
- 15 May: Día del Maestro
- 20 Jul: Izadas de bandera - Independencia
- 7 Ago: Batalla de Boyacá
- 12 Oct: Día de la Raza
- 31 Oct: Halloween escolar
- 11 Nov: Festival de talentos
- 29 Nov: Clausura y grados
    """,
    
    "rutas_escolares": """
🚌 **RUTAS ESCOLARES**

**Rutas disponibles:**

**Ruta 1 - Norte:**
- Salida: 6:00 AM
- Paradas: Centro, La Estación, Barrio Norte
- Costo: $120.000/mes

**Ruta 2 - Sur:**
- Salida: 6:15 AM
- Paradas: Terminal, Barrio Sur, La Esperanza
- Costo: $120.000/mes

**Ruta 3 - Oriente:**
- Salida: 6:00 AM
- Paradas: Comuneros, San José, El Prado
- Costo: $130.000/mes

**Contacto transporte:** 310-555-1234
    """,
    
    "horarios": """
⏰ **HORARIOS DE CLASE**

**Jornada Mañana:**
- Entrada: 6:30 AM
- Primera hora: 6:45 - 7:35 AM
- Segunda hora: 7:35 - 8:25 AM
- Descanso: 8:25 - 8:50 AM
- Tercera hora: 8:50 - 9:40 AM
- Cuarta hora: 9:40 - 10:30 AM
- Descanso: 10:30 - 10:50 AM
- Quinta hora: 10:50 - 11:40 AM
- Sexta hora: 11:40 AM - 12:30 PM

**Jornada Tarde:**
- Entrada: 12:30 PM
- Salida: 6:30 PM
    """,
    
    "asignaturas": """
📚 **ASIGNATURAS**

**Áreas Fundamentales:**
- Matemáticas (5 horas/semana)
- Español y Literatura (5 horas/semana)
- Inglés (4 horas/semana)
- Ciencias Naturales (4 horas/semana)
- Ciencias Sociales (3 horas/semana)

**Áreas Complementarias:**
- Educación Física (2 horas/semana)
- Artística (2 horas/semana)
- Tecnología e Informática (2 horas/semana)
- Ética y Valores (1 hora/semana)
- Religión (1 hora/semana)
    """,
    
    "reuniones": """
👥 **REUNIONES DE PADRES**

**Próximas reuniones:**

📌 **Entrega de boletines 1er período:**
- Fecha: 19 de Abril 2024
- Hora: 7:00 AM - 12:00 PM
- Lugar: Salones de clase

📌 **Asamblea general de padres:**
- Fecha: 10 de Mayo 2024
- Hora: 8:00 AM
- Lugar: Auditorio principal

📌 **Escuela de padres:**
- Fechas: Último viernes de cada mes
- Hora: 6:00 PM
- Tema Mayo: "Acompañamiento escolar"
    """,
    
    "fechas_entrega": """
📝 **FECHAS DE ENTREGA**

**Período actual - Abril 2024:**

| Asignatura | Trabajo | Fecha |
|------------|---------|-------|
| Matemáticas | Taller álgebra | 15 Abril |
| Español | Ensayo literario | 18 Abril |
| Inglés | Presentación oral | 20 Abril |
| Ciencias | Proyecto ecosistemas | 22 Abril |
| Sociales | Línea de tiempo | 25 Abril |

**Exámenes finales período:**
- 8-12 de Abril 2024
    """,
    
    "actividades": """
📋 **ACTIVIDADES PENDIENTES**

**Esta semana:**
- Lunes: Quiz de matemáticas
- Martes: Exposición de inglés
- Miércoles: Laboratorio de ciencias
- Jueves: Entrega taller español
- Viernes: Evaluación sociales

**Próxima semana:**
- Preparación día del idioma
- Ensayos grupo de danzas
- Inicio proyecto de feria científica
    """,
    
    "tutoria": f"""
📖 **TUTORÍAS Y REFUERZOS ACADÉMICOS**

¡Excelente que busques apoyo académico! Aquí tienes un recurso de refuerzo:

🎥 **Video de refuerzo recomendado:**
https://www.youtube.com/watch?v=0d5VWxcSUIk

**Horarios de tutorías presenciales:**
- Lunes y Miércoles: 2:00 PM - 4:00 PM (Matemáticas)
- Martes y Jueves: 2:00 PM - 4:00 PM (Español e Inglés)
- Viernes: 2:00 PM - 4:00 PM (Ciencias)

**Para agendar tutoría:**
1. Habla con tu director de grupo
2. Inscríbete en coordinación académica
3. Las tutorías son gratuitas

**Contacto:** coordinacion@colegio.edu.co
    """
}

# ============================================
# INICIALIZAR SESSION STATE
# ============================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_type' not in st.session_state:
    st.session_state.user_type = None
if 'user_data' not in st.session_state:
    st.session_state.user_data = None
if 'colegio' not in st.session_state:
    st.session_state.colegio = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'consultas' not in st.session_state:
    st.session_state.consultas = {
        "calendario": 0, "matriculas": 0, "actividades": 0,
        "rutas": 0, "horarios": 0, "asignaturas": 0,
        "reuniones": 0, "fechas_entrega": 0, "tutoria": 0, "notas": 0
    }
if 'privacy_accepted' not in st.session_state:
    st.session_state.privacy_accepted = False

# ============================================
# FUNCIONES AUXILIARES
# ============================================

def generar_certificado_pdf(nombre, cedula, colegio, promedio):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from io import BytesIO

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Título
    p.setFont("Helvetica-Bold", 24)
    p.drawCentredString(width/2, height - 100, "CERTIFICADO DE ESTUDIOS")

    # Colegio
    p.setFont("Helvetica-Bold", 18)
    p.drawCentredString(width/2, height - 140, colegio.upper())

    # Línea
    p.setStrokeColorRGB(0, 0.3, 0.6)
    p.line(100, height - 160, width-100, height - 160)

    # Cuerpo
    p.setFont("Helvetica", 14)
    texto = [
        "",
        "El rector(a) de la institución,",
        "",
        "CERTIFICA QUE:",
        "",
        f"El(la) estudiante {nombre},",
        f"identificado(a) con cédula N° {cedula},",
        "se encuentra matriculado(a) y cursando estudios",
        "en esta institución durante el año lectivo 2024.",
        "",
        f"Promedio académico actual: {promedio:.2f}",
        "",
        f"Bogotá D.C., {datetime.now().strftime('%d de %B de %Y')}"
    ]
    
    y = height - 220
    for linea in texto:
        p.drawCentredString(width/2, y, linea)
        y -= 22

    # Firma
    p.line(200, y-30, 400, y-30)
    p.setFont("Helvetica-Bold", 12)
    p.drawCentredString(width/2, y-50, "RECTOR(A)")
    p.drawCentredString(width/2, y-70, colegio)

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer.read()

def procesar_pregunta(pregunta):
    """Procesa la pregunta del chatbot y retorna la respuesta apropiada"""
    pregunta_lower = pregunta.lower()
    
    # Detectar intención
    if any(palabra in pregunta_lower for palabra in ['calendario', 'fechas', 'cuando empiezan', 'vacaciones']):
        st.session_state.consultas["calendario"] += 1
        return info_escolar["calendario_academico"]
    
    elif any(palabra in pregunta_lower for palabra in ['matricula', 'inscripción', 'inscribir', 'requisitos matricula']):
        st.session_state.consultas["matriculas"] += 1
        return info_escolar["matriculas"]
    
    elif any(palabra in pregunta_lower for palabra in ['actividad', 'evento', 'celebración', 'festival']):
        st.session_state.consultas["actividades"] += 1
        return info_escolar["actividades_escolares"]
    
    elif any(palabra in pregunta_lower for palabra in ['ruta', 'transporte', 'bus', 'recorrido']):
        st.session_state.consultas["rutas"] += 1
        return info_escolar["rutas_escolares"]
    
    elif any(palabra in pregunta_lower for palabra in ['horario', 'hora', 'jornada', 'entrada', 'salida']):
        st.session_state.consultas["horarios"] += 1
        return info_escolar["horarios"]
    
    elif any(palabra in pregunta_lower for palabra in ['asignatura', 'materia', 'clase', 'área']):
        st.session_state.consultas["asignaturas"] += 1
        return info_escolar["asignaturas"]
    
    elif any(palabra in pregunta_lower for palabra in ['reunión', 'padres', 'citación', 'asamblea']):
        st.session_state.consultas["reuniones"] += 1
        return info_escolar["reuniones"]
    
    elif any(palabra in pregunta_lower for palabra in ['entrega', 'tarea', 'trabajo', 'examen', 'quiz']):
        st.session_state.consultas["fechas_entrega"] += 1
        return info_escolar["fechas_entrega"]
    
    elif any(palabra in pregunta_lower for palabra in ['tutoria', 'tutoría', 'refuerzo', 'ayuda', 'apoyo', 'no entiendo']):
        st.session_state.consultas["tutoria"] += 1
        return info_escolar["tutoria"]
    
    elif any(palabra in pregunta_lower for palabra in ['nota', 'calificación', 'promedio', 'boletin']):
        st.session_state.consultas["notas"] += 1
        return "📊 Para ver tus notas y promedio, ve a la sección **'Mis Notas'** en el menú lateral."
    
    elif any(palabra in pregunta_lower for palabra in ['certificado', 'constancia', 'documento']):
        return "📜 Para descargar tu certificado de estudios, ve a la sección **'Certificado'** en el menú lateral."
    
    elif any(palabra in pregunta_lower for palabra in ['hola', 'buenos dias', 'buenas tardes', 'hey']):
        return f"👋 ¡Hola {st.session_state.user_data['nombre']}! ¿En qué puedo ayudarte hoy? Puedo darte información sobre:\n\n• Calendario académico\n• Matrículas\n• Actividades escolares\n• Rutas escolares\n• Horarios\n• Asignaturas\n• Reuniones\n• Fechas de entrega\n• Tutorías y refuerzos"
    
    elif any(palabra in pregunta_lower for palabra in ['gracias', 'thank', 'genial']):
        return "😊 ¡Con gusto! Si tienes más preguntas, no dudes en consultarme."
    
    else:
        return """🤔 No estoy seguro de entender tu pregunta. Puedo ayudarte con:

📅 **Calendario académico** - Fechas importantes del año
📋 **Matrículas** - Requisitos y fechas
🎭 **Actividades escolares** - Eventos y celebraciones
🚌 **Rutas escolares** - Transporte disponible
⏰ **Horarios** - Jornadas y horas de clase
📚 **Asignaturas** - Materias y carga horaria
👥 **Reuniones** - Encuentros con padres
📝 **Fechas de entrega** - Trabajos y evaluaciones
📖 **Tutorías** - Apoyo académico y refuerzos

¿Sobre cuál tema te gustaría saber más?"""

# ============================================
# PÁGINA DE PRIVACIDAD
# ============================================
def mostrar_aviso_privacidad():
    st.markdown("""
    <style>
    .privacy-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        color: white !important;
    }
    .privacy-container h1, .privacy-container h2, .privacy-container h3, .privacy-container h4 {
        color: white !important;
    }
    .privacy-container strong {
        color: #a8d5ff !important;
    }
    .privacy-container p, .privacy-container li {
        color: #e0e0e0 !important;
        font-size: 1.1em;
        line-height: 1.7;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="privacy-container">
        <h1 style="text-align:center; margin-bottom:30px;">Aviso de Privacidad y Protección de Datos</h1>
        
        <h3>POLÍTICA DE PRIVACIDAD Y PROTECCIÓN DE DATOS PERSONALES</h3>
        <p><strong>Fecha de última actualización:</strong> Enero 2024</p>

        <h4>1. RESPONSABLE DEL TRATAMIENTO</h4>
        <p>El responsable del tratamiento de sus datos personales es la institución educativa seleccionada.</p>

        <h4>2. DATOS QUE RECOPILAMOS</h4>
        <ul>
            <li>Nombre completo</li>
            <li>Número de identificación (cédula)</li>
            <li>Información académica (notas, asignaturas)</li>
            <li>Historial de consultas en el sistema</li>
        </ul>

        <h4>3. FINALIDAD DEL TRATAMIENTO</h4>
        <p>Sus datos serán utilizados para:</p>
        <ul>
            <li>Gestión académica y administrativa</li>
            <li>Generación de certificados de estudio</li>
            <li>Seguimiento del rendimiento académico</li>
            <li>Comunicación de información institucional</li>
        </ul>

        <h4>4. DERECHOS DEL TITULAR</h4>
        <p>Usted tiene derecho a:</p>
        <ul>
            <li>Conocer, actualizar y rectificar sus datos</li>
            <li>Solicitar prueba de la autorización</li>
            <li>Ser informado sobre el uso de sus datos</li>
            <li>Revocar la autorización</li>
            <li>Acceder gratuitamente a sus datos</li>
        </ul>

        <h4>5. MEDIDAS DE SEGURIDAD</h4>
        <p>Implementamos medidas técnicas y organizativas para proteger sus datos contra acceso no autorizado, pérdida o uso indebido.</p>

        <h4>6. TRANSFERENCIA DE DATOS</h4>
        <p>Sus datos <strong>NO serán compartidos</strong> con terceros sin su consentimiento, salvo obligación legal.</p>

        <h4>7. CONSERVACIÓN DE DATOS</h4>
        <p>Los datos se conservarán mientras exista vínculo con la institución y el tiempo legalmente requerido.</p>

        <h4>8. CONTACTO</h4>
        <p>Email: <strong>protecciondatos@colegio.edu.co</strong><br>
        Teléfono: <strong>(601) 555-0123</strong></p>

        <hr style="border-color:#555; margin:30px 0;">
        <p style="text-align:center; color:#a0d8ff;">
            <strong>Ley 1581 de 2012 • Habeas Data • Colombia</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        acepto = st.checkbox("He leído y acepto la política de privacidad y tratamiento de datos personales", value=False)
        if acepto:
            if st.button("Continuar al Sistema", type="primary", use_container_width=True):
                st.session_state.privacy_accepted = True
                st.rerun()

# ============================================
# PÁGINA DE LOGIN
# ============================================
def mostrar_login():
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    .school-card {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        transition: transform 0.3s;
    }
    .school-card:hover {
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="main-header"><h1>🏫 Sistema Escolar Interactivo</h1><p>Bienvenido al portal estudiantil</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 📍 Paso 1: Selecciona tu Colegio")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f4f8; padding: 20px; border-radius: 10px; text-align: center;">
        <h3>🏛️ Colegio Departamental Carlos Giraldo</h3>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Seleccionar Carlos Giraldo", key="cg", use_container_width=True):
            st.session_state.colegio = "Colegio Departamental Carlos Giraldo"
            
    with col2:
        st.markdown("""
        <div style="background-color: #f8e8e8; padding: 20px; border-radius: 10px; text-align: center;">
        <h3>🏛️ Instituto Técnico Olga Santamaría</h3>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Seleccionar Olga Santamaría", key="os", use_container_width=True):
            st.session_state.colegio = "Instituto Técnico Olga Santamaría"
    
    if st.session_state.colegio:
        st.success(f"✅ Colegio seleccionado: **{st.session_state.colegio}**")
        
        st.markdown("---")
        st.markdown("### 👤 Paso 2: Selecciona tu rol")
        
        user_type = st.radio(
            "¿Eres estudiante o profesor?",
            ["Estudiante", "Profesor"],
            horizontal=True
        )
        
        st.markdown("---")
        st.markdown("### 🔐 Paso 3: Ingresa tu número de cédula")
        
        cedula = st.text_input("Número de cédula:", placeholder="Ej: 12345678")
        
        if st.button("🚀 Ingresar al Sistema", type="primary", use_container_width=True):
            if cedula:
                try:
                    cedula_num = int(cedula)
                    
                    if user_type == "Estudiante":
                        # Buscar en el DataFrame correcto
                        if st.session_state.colegio == "Colegio Departamental Carlos Giraldo":
                            df_buscar = df_carlos_giraldo
                        else:
                            df_buscar = df_olga_santamaria
                        
                        estudiante = df_buscar[df_buscar['Cedula'] == cedula_num]
                        
                        if not estudiante.empty:
                            st.session_state.logged_in = True
                            st.session_state.user_type = "estudiante"
                            st.session_state.user_data = {
                                "nombre": estudiante['Nombre'].iloc[0],
                                "cedula": cedula_num,
                                "colegio": st.session_state.colegio
                            }
                            st.rerun()
                        else:
                            st.error("❌ Cédula no encontrada. Verifica que estés en el colegio correcto.")
                    
                    else:  # Profesor
                        profesores = profesores_data.get(st.session_state.colegio, [])
                        profesor = next((p for p in profesores if p['cedula'] == cedula_num), None)
                        
                        if profesor:
                            st.session_state.logged_in = True
                            st.session_state.user_type = "profesor"
                            st.session_state.user_data = {
                                "nombre": profesor['nombre'],
                                "cedula": cedula_num,
                                "asignatura": profesor['asignatura'],
                                "colegio": st.session_state.colegio
                            }
                            st.rerun()
                        else:
                            st.error("❌ Cédula de profesor no encontrada.")
                            
                except ValueError:
                    st.error("❌ Por favor ingresa un número de cédula válido.")
            else:
                st.warning("⚠️ Por favor ingresa tu número de cédula.")

# ============================================
# DASHBOARD ESTUDIANTE
# ============================================
def mostrar_dashboard_estudiante():
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/student-male--v1.png", width=80)
        st.markdown(f"### 👋 ¡Hola, {st.session_state.user_data['nombre']}!")
        st.markdown(f"📍 {st.session_state.colegio}")
        st.markdown(f"🆔 C.C. {st.session_state.user_data['cedula']}")
        st.markdown("---")
        
        menu = st.radio(
            "📌 Menú",
            ["💬 Chat Bot", "📊 Mis Notas", "📜 Certificado", "📈 Dashboard", "🔒 Privacidad"]
        )
        
        st.markdown("---")
        if st.button("🚪 Cerrar Sesión", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_type = None
            st.session_state.user_data = None
            st.session_state.chat_history = []
            st.rerun()
    
    # Contenido principal según menú
    if menu == "💬 Chat Bot":
        mostrar_chatbot()
    elif menu == "📊 Mis Notas":
        mostrar_notas()
    elif menu == "📜 Certificado":
        mostrar_certificado()
    elif menu == "📈 Dashboard":
        mostrar_dashboard_stats()
    elif menu == "🔒 Privacidad":
        mostrar_info_privacidad()

def mostrar_chatbot():
    st.title("💬 Asistente Virtual Escolar")
    st.markdown("Pregúntame sobre calendario, matrículas, actividades, rutas, horarios, tutorías y más.")
    
    # Contenedor del chat
    chat_container = st.container()
    
    with chat_container:
        for mensaje in st.session_state.chat_history:
            if mensaje["role"] == "user":
                st.markdown(f"""
                <div style="background-color: #dcf8c6; padding: 10px; border-radius: 10px; margin: 5px 0; text-align: right;">
                    <strong>Tú:</strong> {mensaje["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background-color: #f1f0f0; padding: 10px; border-radius: 10px; margin: 5px 0;">
                    <strong>🤖 Asistente:</strong><br>{mensaje["content"]}
                </div>
                """, unsafe_allow_html=True)
    
    # Input del usuario
    st.markdown("---")
    
    # Botones de acceso rápido
    st.markdown("**🚀 Accesos rápidos:**")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📅 Calendario"):
            pregunta = "calendario académico"
            respuesta = procesar_pregunta(pregunta)
            st.session_state.chat_history.append({"role": "user", "content": pregunta})
            st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
            st.rerun()
    
    with col2:
        if st.button("⏰ Horarios"):
            pregunta = "horarios"
            respuesta = procesar_pregunta(pregunta)
            st.session_state.chat_history.append({"role": "user", "content": pregunta})
            st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
            st.rerun()
    
    with col3:
        if st.button("📖 Tutorías"):
            pregunta = "tutoria refuerzo"
            respuesta = procesar_pregunta(pregunta)
            st.session_state.chat_history.append({"role": "user", "content": pregunta})
            st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
            st.rerun()
    
    with col4:
        if st.button("🚌 Rutas"):
            pregunta = "rutas escolares"
            respuesta = procesar_pregunta(pregunta)
            st.session_state.chat_history.append({"role": "user", "content": pregunta})
            st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
            st.rerun()
    
    # Input de texto
    pregunta_usuario = st.text_input("✍️ Escribe tu pregunta:", key="chat_input", placeholder="Ej: ¿Cuándo son las vacaciones?")
    
    if st.button("Enviar", type="primary"):
        if pregunta_usuario:
            respuesta = procesar_pregunta(pregunta_usuario)
            st.session_state.chat_history.append({"role": "user", "content": pregunta_usuario})
            st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
            st.rerun()
    
    # Botón para limpiar chat
    if st.button("🗑️ Limpiar conversación"):
        st.session_state.chat_history = []
        st.rerun()

def mostrar_notas():
    st.title("📊 Mis Notas y Calificaciones")
    
    cedula = st.session_state.user_data['cedula']
    
    # Obtener datos del estudiante
    if st.session_state.colegio == "Colegio Departamental Carlos Giraldo":
        df_estudiante = df_carlos_giraldo[df_carlos_giraldo['Cedula'] == cedula]
    else:
        df_estudiante = df_olga_santamaria[df_olga_santamaria['Cedula'] == cedula]
    
    if not df_estudiante.empty:
        st.markdown(f"### 👤 Estudiante: {df_estudiante['Nombre'].iloc[0]}")
        st.markdown(f"🏫 {st.session_state.colegio}")
        
        st.markdown("---")
        
        # Tabla de notas
        st.markdown("#### 📋 Detalle de Calificaciones")
        
        notas_display = df_estudiante[['Asignatura', 'Nota_Parcial', 'Nota_Final']].copy()
        notas_display.columns = ['Asignatura', 'Nota Parcial', 'Nota Final']
        
        st.dataframe(notas_display, hide_index=True, use_container_width=True)
        
        # Calcular promedios
        promedio_parcial = df_estudiante['Nota_Parcial'].mean()
        promedio_final = df_estudiante['Nota_Final'].mean()
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("📊 Promedio Parcial", f"{promedio_parcial:.2f}")
        
        with col2:
            st.metric("📈 Promedio Final", f"{promedio_final:.2f}")
        
        with col3:
            estado = "✅ Aprobado" if promedio_final >= 6 else "⚠️ En riesgo"
            st.metric("📋 Estado", estado)
        
        # Gráfico de notas
        st.markdown("---")
        st.markdown("#### 📈 Gráfico de Rendimiento")
        
        import plotly.graph_objects as go
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            name='Nota Parcial',
            x=df_estudiante['Asignatura'],
            y=df_estudiante['Nota_Parcial'],
            marker_color='lightblue'
        ))
        fig.add_trace(go.Bar(
            name='Nota Final',
            x=df_estudiante['Asignatura'],
            y=df_estudiante['Nota_Final'],
            marker_color='darkblue'
        ))
        
        fig.update_layout(
            barmode='group',
            title='Comparación de Notas por Asignatura',
            xaxis_title='Asignatura',
            yaxis_title='Nota',
            yaxis_range=[0, 10]
        )
        
        st.plotly_chart(fig, use_container_width=True)

def mostrar_certificado():
    st.title("📜 Certificado de Estudios")
    
    st.markdown("""
    Genera y descarga tu certificado de estudios oficial. Este documento certifica 
    tu matrícula activa en la institución educativa.
    """)
    
    cedula = st.session_state.user_data['cedula']
    nombre = st.session_state.user_data['nombre']
    colegio = st.session_state.colegio
    
    # Calcular promedio
    if colegio == "Colegio Departamental Carlos Giraldo":
        df_estudiante = df_carlos_giraldo[df_carlos_giraldo['Cedula'] == cedula]
    else:
        df_estudiante = df_olga_santamaria[df_olga_santamaria['Cedula'] == cedula]
    
    promedio = df_estudiante['Nota_Final'].mean()
    
    st.markdown("---")
    
    st.markdown("### 📄 Vista Previa del Certificado")
    
    st.markdown(f"""
    <div style="background-color: #fffbf0; padding: 30px; border: 2px solid #d4a574; border-radius: 10px;">
        <h2 style="text-align: center; color: #1a3a5c;">CERTIFICADO DE ESTUDIOS</h2>
        <h3 style="text-align: center; color: #2c5282;">{colegio.upper()}</h3>
        <hr style="border-color: #d4a574;">
        <p style="text-align: justify; font-size: 14px;">
            El/La rector(a) del {colegio}, <strong>CERTIFICA QUE:</strong>
        </p>
        <p style="text-align: center; font-size: 16px;">
            El/La estudiante <strong>{nombre}</strong>, identificado(a) con documento 
            de identidad No. <strong>{cedula}</strong>, se encuentra matriculado(a) 
            y cursando estudios en esta institución educativa durante el año lectivo 2024.
        </p>
        <p style="text-align: center; font-size: 14px;">
            Promedio académico actual: <strong>{promedio:.2f}</strong>
        </p>
        <p style="text-align: center; font-size: 12px; color: #666;">
            Expedido el {datetime.now().strftime('%d de %B de %Y')}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("📥 Descargar Certificado PDF", type="primary", use_container_width=True):
        pdf_bytes = generar_certificado_pdf(nombre, cedula, colegio, promedio)
        
        st.download_button(
            label="💾 Guardar PDF",
            data=pdf_bytes,
            file_name=f"certificado_{nombre.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf",
            mime="application/pdf"
        )
        st.success("✅ ¡Certificado generado exitosamente!")

def mostrar_dashboard_stats():
    st.title("📈 Dashboard de Estadísticas")
    
    st.markdown("### 📊 Temas Más Consultados")
    
    # Gráfico de consultas
    import plotly.express as px
    
    consultas_df = pd.DataFrame({
        'Tema': list(st.session_state.consultas.keys()),
        'Consultas': list(st.session_state.consultas.values())
    })
    
    fig = px.bar(consultas_df, x='Tema', y='Consultas', 
                 title='Frecuencia de Consultas por Tema',
                 color='Consultas',
                 color_continuous_scale='Blues')
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("### 📚 Promedios por Asignatura (Todos los Estudiantes)")
    
    # Obtener datos del colegio actual
    if st.session_state.colegio == "Colegio Departamental Carlos Giraldo":
        df_colegio = df_carlos_giraldo
    else:
        df_colegio = df_olga_santamaria
    
    # Promedios por asignatura
    promedios_asignatura = df_colegio.groupby('Asignatura')['Nota_Final'].mean().reset_index()
    
    fig2 = px.pie(promedios_asignatura, values='Nota_Final', names='Asignatura',
                  title='Distribución de Promedios por Asignatura')
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("### 👥 Ranking de Estudiantes")
    
    # Calcular promedio por estudiante
    ranking = df_colegio.groupby(['Nombre', 'Cedula'])['Nota_Final'].mean().reset_index()
    ranking = ranking.sort_values('Nota_Final', ascending=False)
    ranking.columns = ['Nombre', 'Cédula', 'Promedio']
    ranking['Posición'] = range(1, len(ranking) + 1)
    
    st.dataframe(ranking[['Posición', 'Nombre', 'Promedio']], hide_index=True, use_container_width=True)

def mostrar_info_privacidad():
    st.title("🔒 Política de Privacidad")
    
    st.markdown("""
    ### Tus Datos Están Protegidos
    
    En nuestra institución nos tomamos muy en serio la protección de tus datos personales.
    
    #### 📋 Datos que manejamos:
    - Nombre completo
    - Número de identificación
    - Calificaciones académicas
    - Historial de consultas
    
    #### 🛡️ Cómo protegemos tu información:
    - Acceso solo con autenticación
    - Datos encriptados
    - No compartimos con terceros
    - Cumplimiento de Ley 1581 de 2012
    
    #### ✅ Tus derechos:
    - Acceder a tu información
    - Corregir datos incorrectos
    - Solicitar eliminación
    - Revocar autorización
    
    #### 📞 Contacto:
    Para ejercer tus derechos: **protecciondatos@colegio.edu.co**
    """)

# ============================================
# DASHBOARD PROFESOR
# ============================================
def mostrar_dashboard_profesor():
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/teacher.png", width=80)
        st.markdown(f"### 👋 ¡Hola, {st.session_state.user_data['nombre']}!")
        st.markdown(f"📚 {st.session_state.user_data['asignatura']}")
        st.markdown(f"🏫 {st.session_state.colegio}")
        st.markdown("---")
        
        menu = st.radio(
            "📌 Menú",
            ["📊 Ver Estudiantes", "📈 Estadísticas", "🔒 Privacidad"]
        )
        
        st.markdown("---")
        if st.button("🚪 Cerrar Sesión", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user_type = None
            st.session_state.user_data = None
            st.rerun()
    
    if menu == "📊 Ver Estudiantes":
        st.title("📊 Lista de Estudiantes")
        
        if st.session_state.colegio == "Colegio Departamental Carlos Giraldo":
            df_mostrar = df_carlos_giraldo
        else:
            df_mostrar = df_olga_santamaria
        
        asignatura = st.session_state.user_data['asignatura']
        df_asignatura = df_mostrar[df_mostrar['Asignatura'] == asignatura]
        
        st.markdown(f"### 📚 Estudiantes de {asignatura}")
        st.dataframe(df_asignatura[['Nombre', 'Cedula', 'Nota_Parcial', 'Nota_Final']], 
                    hide_index=True, use_container_width=True)
        
    elif menu == "📈 Estadísticas":
        st.title("📈 Estadísticas de la Clase")
        
        if st.session_state.colegio == "Colegio Departamental Carlos Giraldo":
            df_mostrar = df_carlos_giraldo
        else:
            df_mostrar = df_olga_santamaria
        
        asignatura = st.session_state.user_data['asignatura']
        df_asignatura = df_mostrar[df_mostrar['Asignatura'] == asignatura]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("📊 Promedio Clase", f"{df_asignatura['Nota_Final'].mean():.2f}")
        with col2:
            st.metric("📈 Nota Máxima", f"{df_asignatura['Nota_Final'].max():.2f}")
        with col3:
            st.metric("📉 Nota Mínima", f"{df_asignatura['Nota_Final'].min():.2f}")
            
    elif menu == "🔒 Privacidad":
        mostrar_info_privacidad()

# ============================================
# MAIN APP
# ============================================
def main():
    if not st.session_state.privacy_accepted:
        mostrar_aviso_privacidad()
    elif not st.session_state.logged_in:
        mostrar_login()
    elif st.session_state.user_type == "estudiante":
        mostrar_dashboard_estudiante()
    elif st.session_state.user_type == "profesor":
        mostrar_dashboard_profesor()

if __name__ == "__main__":
    main()
