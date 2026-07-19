from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
import os


load_dotenv()


app = Flask(__name__)

CORS(app)



client = genai.Client(
    api_key=os.getenv("GEMINI_KEY")
)



@app.route("/chat", methods=["POST"])
def chat():


    data = request.json


    message = data.get("message")


    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=message
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