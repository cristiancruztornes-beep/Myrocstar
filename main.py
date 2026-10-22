import os
import telebot
import google.generativeai as genai

# El bot buscará estas llaves en Render
TOKEN_TELEGRAM = os.getenv('TELEGRAM_TOKEN')
API_KEY_GEMINI = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=API_KEY_GEMINI)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(TOKEN_TELEGRAM)

@bot.message_handler(func=lambda message: True)
def responder(message):
 try:
   # Estas líneas tienen la sangría necesaria para pertenecer al bloque try
    response = 
   model.generate_content(message.text)
    bot.reply_to(message, response.text)
    except Exception as e:
 # Esta línea tiene la sangría necesaria para pertenecer al bloque except
    print(f"Error detectado: {e}")
    bot.reply_to(message, "Hubo un error al procesar tu mensaje.")

   print("El bot está encendido...")
   bot.infinity_polling()
