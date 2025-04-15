# chatgpt_simulado.py - Simulación de un chat con modelo GPT desde consola
# Autor: Valentín Arrigoni
# Descripción: Este script simula un sistema de conversación básico
# utilizando lógica fija para responder preguntas de usuario.

def responder(prompt):
    """
    Simula una respuesta del modelo ChatGPT a un mensaje dado.
    Retorna una respuesta predefinida si detecta ciertas palabras clave.
    """
    # Normalizamos el prompt a minúsculas
    prompt = prompt.lower()

    # Verifica si el mensaje es un saludo
    if "hola" in prompt:
        return "¡Hola! ¿Cómo estás? Soy una IA simulada :)"

    # Verifica si el usuario pregunta por el clima
    if "clima" in prompt:
        return "Lo siento, no tengo acceso a datos del clima."

    # Respuesta por defecto
    return "Lo siento, no entendí tu consulta."

def main():
    """
    Función principal para ejecutar el chat simulado por consola.
    """
    print("Bienvenido al chat simulado de GPT. Escriba 'salir' para terminar.")

    while True:
        try:
            # Lee entrada del usuario
            entrada = input("Usuario: ")

            # Condición para salir
            if entrada.strip().lower() == "salir":
                print("¡Hasta luego!")
                break

            # Procesa la respuesta
            respuesta = responder(entrada)
            print("IA:", respuesta)

        except KeyboardInterrupt:
            # Manejo de Ctrl+C
            print("\nInterrupción manual. Cerrando chat...")
            break
        except Exception as e:
            # Captura cualquier otro error inesperado
            print("Ocurrió un error:", e)

# Punto de entrada del script
if __name__ == "__main__":
    main()
