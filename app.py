from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/alice", methods=["POST"])
def handle_alice():
    data = request.json
    version = data.get("version", "1.0")
    message = data.get("request", {}).get("original_utterance", "").strip().lower()

    # Всегда возвращаем безопасный ответ
    if not message:
        answer = "Привет! Скажи что-нибудь, и я попробую ответить."
    else:
        answer = f"Вы сказали: {message}"

    response = {
        "response": {
            "text": answer,
            "end_session": False
        },
        "version": version
    }

    return jsonify(response)

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

if __name__ == "__main__":
    app.run(debug=True)
