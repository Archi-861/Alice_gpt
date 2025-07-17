from flask import Flask, request, jsonify
from gpt_api import ask_gpt

app = Flask(__name__)

# Типовые фразы без GPT
PRESET_RESPONSES = {
    "привет": "Привет! Я GPT. Задай мне любой вопрос.",
    "помощь": "Ты можешь спросить у меня что угодно — я постараюсь ответить.",
    "что ты умеешь": "Я могу отвечать на любые вопросы, объяснять, советовать и помогать.",
}

@app.route("/alice", methods=["POST"])
def handle_alice():
    data = request.json
    message = data.get("request", {}).get("original_utterance", "").strip().lower()
    version = data.get("version")

    if not message:
        answer = "Привет! Скажи что-нибудь, и я передам это GPT."
    elif message in PRESET_RESPONSES:
        answer = PRESET_RESPONSES[message]
    else:
        answer = ask_gpt(message)

    return jsonify({
        "response": {
            "text": answer,
            "end_session": False
        },
        "version": version
    })

# Пинг эндпоинт для автопрогрева
@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

if __name__ == "__main__":
    app.run(debug=True)