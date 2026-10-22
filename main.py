import os
import telebot
import google.generativeai as genai

# El bot buscará estas llaves en Render
TOKEN_TELEGRAM = os.getenv('TELEGRAM_TOKEN')
API_KEY_GEMINI = os.getenv('GEMIMINI_API_KEY')

genai.configure(api_key=API_KEY_GEMINI)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(TOKEN_TELEGRAM)

@bot.message_handler(func=lambda message: 
True)
def responder(message):
 try: response =
   model.generate_content(message.text)
   bot.reply_to(message, response.text)
   except Exception as e:
   # Estas líneas TAMBIÉN deben tener sangría
   print(f"Error detectado: {e}")
   bot.reply_to(message, "Hubo un error al procesar tu mensaje.")

print("El bot está encendido...")
bot.infinity_polling()
