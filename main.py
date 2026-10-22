import os
import telebot
import google.generativeai as genai
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/') 
def home():  
 return ""

def run_flask():
  port = int(os.environ.get('PORT', 8080))  
  app.run(host='0.0.0.0', port=port)
# El bot buscará estas llaves en Render
TOKEN_TELEGRAM = os.getenv('TELEGRAM_TOKEN')
API_KEY_GEMINI = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=API_KEY_GEMINI)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(TOKEN_TELEGRAM)

@bot.message_handler(func=lambda message: 
True)
def responder(message):
 try: 
   response = model.generate_content(message.text)
   bot.reply_to(message, response.text)
 except Exception as e:
   print(f"Error detectado: {e}")
   bot.reply_to(message, "Hubo un error al procesar tu mensaje.")

server_thread = Thread(target=run_flask) 
server_thread.start()

print("El bot está encendido...")
bot.infinity_polling()
