import json  # Para cargar y manipular archivos JSON
import os    # Para manejar rutas de archivos y carpetas

# Obtiene la ruta absoluta del directorio donde está este archivo .py
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta completa al archivo conocimiento.json en el mismo directorio
ruta_json = os.path.join(directorio_actual, "conocimiento.json")

# Abre y carga el archivo JSON con la base de conocimiento en la variable 'conocimiento'
with open(ruta_json, "r", encoding="utf-8") as f:
    conocimiento = json.load(f)

def realizar_quiz():
    """
    Realiza un quiz de autoevaluación para ingreso a Ingeniería Mecatrónica.
    Muestra preguntas, recibe respuestas y recomienda áreas a mejorar.
    """
    # Extrae las preguntas y recomendaciones del diccionario 'conocimiento'
    preguntas = conocimiento["quiz"]["preguntas"]
    recomendaciones = conocimiento["quiz"]["recomendaciones"]

    print("\nIniciando evaluación para ingreso a Ingeniería Mecatrónica.\n")
    areas_a_mejorar = set()  # Usamos un set para evitar áreas repetidas

    # Itera sobre cada pregunta del quiz
    for pregunta in preguntas:
        print(f"{pregunta['id']}. {pregunta['texto']}")
        # Muestra las opciones de respuesta numeradas
        for i, opcion in enumerate(pregunta["opciones"], start=1):
            print(f"  {i}. {opcion}")
        # Solicita al usuario una respuesta válida (número dentro del rango)
        while True:
            try:
                respuesta = int(input("Tu respuesta: "))
                if 1 <= respuesta <= len(pregunta["opciones"]):
                    break  # Sale del ciclo si la respuesta es válida
                else:
                    print("Por favor, ingresa un número válido.")
            except ValueError:
                print("Entrada inválida. Ingresa un número.")

        # Si la respuesta es menor que la opción considerada correcta, se marca el área como a mejorar
        if respuesta < pregunta["correcta"]:
            areas_a_mejorar.add(pregunta["area"])

        print()  # Línea en blanco para separar preguntas

    # Al terminar, muestra recomendaciones según las áreas a mejorar
    if areas_a_mejorar:
        print("Áreas recomendadas para mejorar:")
        for area in areas_a_mejorar:
            # Busca la recomendación para cada área, o un mensaje por defecto si no existe
            rec = recomendaciones.get(area, "No hay recomendación disponible para esta área.")
            print(f"- {area.capitalize()}: {rec}")
    else:
        print("¡Felicidades! Tus respuestas indican que tienes un buen nivel en las áreas evaluadas.")
    print()  # Línea en blanco final

def mostrar_posgrados():
    """
    Muestra información de los posgrados disponibles relacionados con Ingeniería Mecatrónica.
    """
    posgrados = conocimiento["posgrados_unam"]  # Extrae los posgrados del JSON
    texto = "Posgrados disponibles relacionados con Ingeniería Mecatrónica:\n"
    # Itera sobre cada posgrado y agrega su información al texto
    for key, posgrado in posgrados.items():
        texto += f"\n{posgrado['nombre']}\n"
        texto += f"Instituto: {posgrado['instituto']}\n"
        texto += "Requisitos:\n"
        reqs = posgrado["requisitos"]
        texto += f"  - Promedio mínimo: {reqs['promedio_minimo']}\n"
        texto += f"  - Materias requeridas: {', '.join(reqs['materias_requeridas'])}\n"
        texto += f"  - Inglés: {reqs['ingles']}\n"
        texto += "Perfil ideal:\n"
        perfil = posgrado["perfil_ideal"]
        texto += f"  - Intereses: {', '.join(perfil['intereses'])}\n"
        texto += f"  - Habilidades: {', '.join(perfil['habilidades'])}\n"
    # Mensaje final para invitar al usuario a hacer el quiz de posgrados
    texto += "\nSi quieres, puedes hacer un quiz para recomendarte el posgrado más adecuado. Solo dime 'quiero hacer quiz posgrado' o algo similar."
    return texto

def quiz_posgrados():
    """
    Realiza un quiz para recomendar el posgrado más adecuado según las respuestas del usuario.
    Suma puntajes y muestra la recomendación final.
    """
    preguntas = conocimiento["quiz_posgrados"]["preguntas"]
    recomendaciones = conocimiento["quiz_posgrados"]["recomendaciones"]

    print("\nQuiz para recomendar el posgrado más adecuado.\nResponde seleccionando el número de la opción.\n")

    # Inicializa un diccionario para llevar el puntaje de cada posgrado
    puntajes = {clave: 0 for clave in recomendaciones.keys()}

    # Itera sobre cada pregunta del quiz de posgrados
    for pregunta in preguntas:
        print(f"{pregunta['id']}. {pregunta['texto']}")
        # Muestra las opciones de respuesta numeradas
        for i, opcion in enumerate(pregunta["opciones"], start=1):
            print(f"  {i}. {opcion}")
        # Solicita al usuario una respuesta válida
        while True:
            try:
                respuesta = int(input("Tu respuesta: "))
                if 1 <= respuesta <= len(pregunta["opciones"]):
                    break
                else:
                    print("Por favor, ingresa un número válido.")
            except ValueError:
                print("Entrada inválida. Ingresa un número.")

        # Suma los pesos correspondientes a cada posgrado según la respuesta
        for clave, peso in pregunta["pesos"].items():
            puntajes[clave] += peso

        print()  # Línea en blanco para separar preguntas

    # Determina el posgrado con mayor puntaje
    mejor_posgrado = max(puntajes, key=puntajes.get)
    recomendacion = recomendaciones.get(mejor_posgrado, "No hay recomendación disponible.")

    print(f"Basado en tus respuestas, te recomendamos el siguiente posgrado:\n- {recomendacion}\n")

def motor_de_reglas(intencion):
    """
    Motor de reglas principal: recibe la intención detectada y responde con la información adecuada.
    Puede mostrar información de ingreso, recomendaciones, posgrados, profesores, o iniciar quizzes.
    """
    profesores = conocimiento["profesores"]  # Extrae la información de profesores

    # Si la intención es sobre informes de ingreso a la carrera
    if intencion == "informes_ingreso":
        carrera = conocimiento["carrera"]
        requisitos = conocimiento["requisitos"]
        texto = (
            f"Carrera: {carrera['nombre']}\n"
            f"Facultad: {carrera['facultad']}\n"
            f"Duración: {carrera['duracion']}\n"
            f"Perfil de ingreso: {carrera['perfil_ingreso']}\n"
            f"Plan de estudios: {carrera['plan_estudios']}\n\n"
            "Requisitos de ingreso:\n"
            f"Tipo de ingreso: {requisitos['tipo_ingreso']}\n"
            "Proceso:\n"
        )
        # Agrega cada paso del proceso de ingreso
        for paso in requisitos["proceso"]:
            texto += f"- {paso}\n"
        # Agrega las materias clave del tronco común
        texto += "\nMaterias clave del tronco común:\n"
        for materia in requisitos["tronco_comun"]["materias_clave"]:
            texto += f"- {materia}\n"
        # Agrega información de contacto de la coordinación
        texto += "\nPara más información, contacta a la coordinación:\n"
        texto += f"{requisitos['coordinacion']['contacto']}\n"
        texto += f"Ubicación: {requisitos['coordinacion']['ubicacion']}\n"
        texto += f"{requisitos['coordinacion']['informacion_adicional']}\n"
        # Invita al usuario a hacer la evaluación de áreas de mejora
        texto += "\nSi quieres, puedes hacer una evaluación para identificar tus áreas de mejora. Solo dime 'quiero hacer la evaluación' o algo similar."
        return texto

    # Si la intención es pedir recomendaciones para mejorar habilidades
    elif intencion == "recomendaciones":
        recomendaciones = conocimiento["quiz"]["recomendaciones"]
        texto = "Recomendaciones para fortalecer tus habilidades:\n"
        for area, rec in recomendaciones.items():
            texto += f"- {area.capitalize()}: {rec}\n"
        return texto

    # Si la intención es pedir orientación sobre posgrados
    elif intencion == "orientacion_posgrado":
        return mostrar_posgrados()

    # Si la intención es realizar el quiz de posgrados
    elif intencion == "realizar_quiz_posgrado":
        quiz_posgrados()
        return ""

    # Si la intención es pedir información de todos los profesores
    elif intencion == "info_profesores":
        texto = "Información de contacto de los profesores:\n"
        for key, profe in profesores.items():
            texto += f"\n{profe['nombre']}\n"
            texto += f"  Cubículo: {profe['cubiculo']} - {profe['edificio']}\n"
            texto += "  Horario:\n"
            for dia, hora in profe["horario"].items():
                texto += f"    {dia}: {hora}\n"
            texto += f"  Materias: {', '.join(profe['materias'])}\n"
            texto += f"  Correo: {profe['correo']}\n"
            texto += f"  Teléfono: {profe['telefono']}\n"
        return texto

    # Si la intención es realizar la evaluación de ingreso (quiz de áreas)
    elif intencion == "realizar_evaluacion":
        print("Perfecto, vamos a iniciar la evaluación.")
        realizar_quiz()
        return ""

    # Si la intención es pedir información de un profesor específico
    elif intencion.startswith("profesor_"):
        clave = intencion.split("_")[1].capitalize()  # Extrae el apellido del profesor
        profe = profesores.get(clave)
        if profe:
            texto = (
                f"Información del profesor {profe['nombre']}:\n"
                f"  Cubículo: {profe['cubiculo']} - {profe['edificio']}\n"
                f"  Horario:\n"
            )
            for dia, hora in profe["horario"].items():
                texto += f"    {dia}: {hora}\n"
            texto += f"  Materias: {', '.join(profe['materias'])}\n"
            texto += f"  Correo: {profe['correo']}\n"
            texto += f"  Teléfono: {profe['telefono']}\n"
            return texto
        else:
            return "No encontré información para ese profesor."

    # Si la intención no se reconoce, responde con un mensaje genérico
    else:
        return "No entendí tu solicitud, ¿puedes reformularla?"