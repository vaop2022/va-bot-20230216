from dotenv import dotenv_values
from VaScript import getVaScript
import telebot

def setup(bot):

    config = dotenv_values(".env")

    ### The Bot variables setting
    bot.defineVariable('telebot.TeleBot(5662687046******)...b10', telebot.TeleBot(config.get("TELEGRAM_BOT_TOKEN")))

    bot.defineVariable('message from customer...b11', 'unknown message from customer')
    bot.defineVariable('message type from customer...message type', 'unknown message type from customer')
    bot.defineVariable('input [call.data] from customer...input from customer', 'unknown input [call.data] from customer')

    bot.defineVariable('message type constant: any_text...any text', 'any_text')
    bot.defineVariable('message_type constant: commands...commands', 'commands')
    bot.defineVariable('message_type constant: input...input', 'input')

    bot.defineVariable('input from customer constant...yes or no', 'yes_or_no')
    bot.defineVariable('input from customer constant...yes or no or uptoyou', 'yes_or_no_or_uptoyou')

    bot.defineVariable('input from customer constant...again', 'again')

    bot.defineVariable('Ask V-agent...msg_010', 'Ask V-agent to Rent or to Buy :')
    bot.defineVariable('button title...Yes/No', 'Rent')
    bot.defineVariable('button title...Yes/No/Up to You', 'Buy')
    bot.defineVariable('button title...Again', 'Ask V-agent again')


  
