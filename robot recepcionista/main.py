from clasificador import clasificar_intencion  # Importa la función para clasificar intenciones
from motor import motor_respuesta              # Importa la función que genera respuestas

def main():
    print("Bienvenido al sistema de atención. Escribe 'salir' para terminar.")
    while True:
        texto_usuario = input("Tú: ")          # Solicita entrada del usuario
        if texto_usuario.lower() == 'salir':   # Condición para salir del programa
            print("Sistema: ¡Hasta luego!")
            break
        # Clasifica la intención del texto ingresado
        intencion = clasificar_intencion(texto_usuario)
        # Obtiene la respuesta correspondiente a la intención
        respuesta = motor_respuesta(intencion)
        print("Sistema:", respuesta)            # Muestra la respuesta al usuario

if __name__ == "__main__":
    main()  # Ejecuta la función principal cuando se corre el script