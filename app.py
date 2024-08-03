from flask import Flask, request, jsonify, send_from_directory
import openai

app = Flask(__name__, static_folder='static')

# Configurar tu API key
openai.api_key = ""

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generar_ejercicio', methods=['POST'])
def generar_ejercicio():
    try:
        data = request.json
        idioma = data['idioma']
        nivel = data['nivel']

        contexto = f"Eres un profesor de {idioma} que crea ejercicios de gramática y vocabulario para estudiantes de nivel {nivel}."

        prompt = f"""
        Crea un ejercicio de opción múltiple en {idioma} para estudiantes de nivel {nivel}.
        Instrucciones:
        Debe haber 3 opciones de las cuales solo una es la correcta. Cada opción debe ir en un div diferente igual que en el ejemplo.

        Ejemplo:
        Pregunta: Completa la frase: "El gato está en _____ casa."
        <div id="correcto">la</div>
        <div id="incorrecto">el</div>
        <div id="incorrecto2">los</div>

        Ejercicio:
        """

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": contexto},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )

        mensaje = response.choices[0].message['content'].strip()

        # Parse the generated text to extract question and options
        lines = mensaje.split('\n')
        pregunta = lines[0].replace("Pregunta: ", "").strip()
        correcto = lines[2].replace('<div id="correcto">', "").replace('</div>', "").replace("CORRECTA", "").strip()
        incorrecto1 = lines[3].replace('<div id="incorrecto">', "").replace('</div>', "").strip()
        incorrecto2 = lines[4].replace('<div id="incorrecto2">', "").replace('</div>', "").strip()

        return jsonify({
            "pregunta": pregunta,
            "correcto": correcto,
            "incorrecto1": incorrecto1,
            "incorrecto2": incorrecto2
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)












