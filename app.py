from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carrega .env
load_dotenv()

# Lê a API KEY
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise Exception("❌ ERRO: API KEY não encontrada. Verifique a variável de ambiente GEMINI_API_KEY.")

# Configura o Gemini
genai.configure(api_key=API_KEY)

# Carrega o modelo
model = genai.GenerativeModel("gemini-2.5-flash")

# Inicia chat
chat = model.start_chat(history=[])

app = Flask(__name__)

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Endpoint do chat
@app.route("/api/chat", methods=["POST"])
def chat_api():
    data = request.get_json()
    user_msg = data.get("mensagem", "")

    # Envia mensagem ao Gemini
    response = chat.send_message(user_msg)

    return jsonify({"resposta": response.text})


if __name__ == "__main__":
    app.run(debug=True)
