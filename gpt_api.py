import openai
from config import OPENAI_API_KEY
import time

openai.api_key = OPENAI_API_KEY

MAX_GPT_RESPONSE_CHARS = 300  # Максимум символов для Алисы

def ask_gpt(message: str) -> str:
    start = time.time()
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": message}],
            temperature=0.4,
        )
        answer = response.choices[0].message.content.strip()
        elapsed = time.time() - start
        print(f"[GPT] Ответ за {elapsed:.2f} сек")

        if len(answer) > MAX_GPT_RESPONSE_CHARS:
            answer = answer[:MAX_GPT_RESPONSE_CHARS].rsplit('.', 1)[0] + "."

        return answer

    except Exception as e:
        return f"Ошибка GPT: {e}"
