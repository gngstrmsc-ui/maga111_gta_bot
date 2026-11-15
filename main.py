import telebot
import os

TOKEN = "9175097071:AAGbaPqW7pkwi5ivYTeFuqPBam9cTT--x9s"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salam! Mən GTA San Andreas fayl konverteri botuyam. Faylını göndər, konvertasiya edim!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Faylını qəbul etdim! Tezliklə konverter işə düşəcək.")

if __name__ == "__main__":
    bot.infinity_polling()


