from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/mp-proxy", methods=["POST"])
def mp_proxy():
    try:
        print("Notificação recebida:", request.json)

        # Reenvia para o seu endpoint no PythonAnywhere
        response = requests.post(
            "http://digitalstoregames.pythonanywhere.com/notificacao-teste",
            json=request.json,
            timeout=5
        )

        print("Resposta do seu servidor:", response.status_code)
        return {"status": "forwarded"}, 200
    except Exception as e:
        print("Erro:", e)
        return {"error": str(e)}, 500
