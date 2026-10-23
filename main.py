import os
import telebot
from google import genai
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running!", 200

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

Thread(target=run_flask).start()

TOKEN_TELEGRAM = os.getenv('TELEGRAM_TOKEN')
API_KEY_GEMINI = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=API_KEY_GEMINI)
bot = telebot.TeleBot(TOKEN_TELEGRAM)

@bot.message_handler(func=lambda message: True)
def responder(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error detectado: {e}")
        bot.reply_to(message, "Hubo un error al procesar tu mensaje.")

print("El bot está encendido...")
bot.remove_webhook()
bot.infinity_polling()
