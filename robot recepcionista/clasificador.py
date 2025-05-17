import re  # Importa el módulo para expresiones regulares

def clasificar_intencion(texto_usuario):
    # Convierte el texto a minúsculas para facilitar la comparación
    texto = texto_usuario.lower()
    # Elimina signos de puntuación para evitar interferencias en la búsqueda de palabras clave
    texto = re.sub(r'[^\w\s]', '', texto)

    # Listas de palabras o frases clave para diferentes intenciones
    sin_ingenieria = [
        "ingresar", "ingreso", "admisión", "admitir", "requisitos", "carrera",
        "mecatrónica", "informes", "inscripción", "matrícula", "estudiar mecatrónica",
        "quiero entrar", "quiero estudiar", "quiero inscribirme", "perfil", "plan de estudios"
    ]

    sin_recomendaciones = [
        "curso", "recomendación", "aprender", "estudiar", "sugerencia", "ayuda",
        "fortalecer", "mejorar", "nivelar", "nivelación", "clases", "taller"
    ]

    sin_posgrado = [
        "posgrado", "maestría", "doctorado", "postgrado", "especialización",
        "estudios avanzados", "continuar estudios", "educación superior"
    ]

    sin_quiz_posgrado = [
        "quiz posgrado", "recomendar posgrado", "posgrado recomendado", "ayuda posgrado",
        "quiero hacer quiz posgrado", "quiero recomendación posgrado"
    ]

    sin_profesores = [
        "profesor", "docente", "catedrático", "contacto", "maestro", "clase",
        "horario", "cubículo", "teléfono", "correo", "información docente"
    ]

    sin_evaluacion = [
        "evaluación", "evaluar", "quiz", "examen", "prueba", "test", "áreas de mejora"
    ]

    # Diccionario que relaciona apellidos de profesores con intenciones específicas
    profesores_clave = {
        "garcia": "profesor_garcia",
        "lopez": "profesor_lopez",
        "martinez": "profesor_martinez",
        "ramirez": "profesor_ramirez",
        "hernandez": "profesor_hernandez",
        "perez": "profesor_perez",
        "sanchez": "profesor_sanchez"
    }

    # Busca si el texto contiene el apellido de algún profesor para clasificar la intención
    for clave, intencion_prof in profesores_clave.items():
        if clave in texto:
            return intencion_prof

    # Verifica si el texto contiene alguna frase o palabra clave para cada categoría y retorna la intención correspondiente
    if any(frase in texto for frase in sin_quiz_posgrado):
        return "realizar_quiz_posgrado"
    if any(palabra in texto for palabra in sin_ingenieria):
        return "informes_ingreso"
    if any(palabra in texto for palabra in sin_recomendaciones):
        return "recomendaciones"
    if any(palabra in texto for palabra in sin_posgrado):
        return "orientacion_posgrado"
    if any(palabra in texto for palabra in sin_profesores):
        return "info_profesores"
    if any(palabra in texto for palabra in sin_evaluacion):
        return "realizar_evaluacion"

    # Si no se reconoce ninguna intención, retorna "no_reconocido"
    return "no_reconocido"