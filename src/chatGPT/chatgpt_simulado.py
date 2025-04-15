"""
Simulación local del uso del API de OpenAI para trabajo práctico de Ingeniería de Sistemas.
No requiere conexión a internet ni uso de una API Key.
"""

import json

# Historial simulado de consultas
historial = []
indice_historial = -1

def obtener_entrada_usuario():
    """
    Obtiene la entrada del usuario con soporte para tecla 'Arriba'.
    """
    global indice_historial
    try:
        entrada = input(">> ")
        if entrada == "" and historial:
            indice_historial = max(0, indice_historial - 1)
            print(f"(Última consulta): {historial[indice_historial]}")
            return historial[indice_historial]
        historial.append(entrada)
        indice_historial = len(historial)
        return entrada
    except KeyboardInterrupt:
        print("\nSaliendo...")
        exit()

def procesar_consulta(context, usertask, userquery):
    """
    Simula una llamada al API de OpenAI y devuelve una respuesta predefinida.
    """
    # Esta parte simula cómo OpenAI estructura la respuesta
    simulated_response = {
        "choices": [{
            "message": {
                "content": f"""
¡Hola! Soy una simulación de ChatGPT 😄

📌 Contexto: {context}
🎯 Tarea: {usertask}
❓ Consulta: {userquery}

✅ Respuesta simulada:
Hola, estoy bien, gracias por preguntar. Soy un asistente conversacional entrenado para ayudarte en tareas de Ingeniería de Sistemas. ¿En qué puedo ayudarte hoy?
                """.strip()
            }
        }]
    }
    return simulated_response

def main():
    print("🧪 Simulador de API de ChatGPT (Versión Local - Sin conexión)")
    context = "Actuás como un asistente para estudiantes de Ingeniería de Sistemas."
    usertask = "Ayudás a interpretar el uso del API de OpenAI para consultas técnicas."

    while True:
        try:
            userquery = obtener_entrada_usuario()
            if not userquery.strip():
                print("Por favor, ingresá una consulta válida.")
                continue

            print(f"You: {userquery}")

            # Simula llamada a API
            response = procesar_consulta(context, usertask, userquery)

            # Procesar respuesta simulada
            jsonStr = response["choices"][0]["message"]["content"]
            print(f"chatGPT: {jsonStr}")

        except Exception as e:
            print(f"chatGPT: Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
