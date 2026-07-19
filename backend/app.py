from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
import os
from knowledge_loader import load_knowledge

load_dotenv()


app = Flask(__name__)

CORS(app)



client = genai.Client(
    api_key=os.getenv("GEMINI_KEY")
)


knowledge = load_knowledge()

print("Размер базы знаний:", len(knowledge))
print(knowledge[:500])


@app.route("/chat", methods=["POST"])
def chat():


    data = request.json


    message = data.get("message")


    prompt = f"""
Ты Phoenix AI — AI-ассистент компании.

ВАЖНО:

- Используй базу знаний компании для ответов.
- Если информация есть в базе знаний, используй только её.
- Не придумывай факты.
- Не упоминай Gemini, Google или то, что ты языковая модель.
- Представляйся как Phoenix AI только при первом сообщении пользователя или если пользователь спрашивает "кто ты?".
- Не начинай каждый ответ с приветствия.
- Отвечай сразу по сути вопроса.
- Пиши кратко, понятно и профессионально.
- Если ответа нет в базе знаний, сообщи пользователю, что такой информации пока нет.   
База знаний компании:

{knowledge}


Вопрос пользователя:

{message}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )


    return jsonify({

        "answer": response.text

    })




@app.route("/")
def home():

    return "Phoenix AI Server работает"



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )