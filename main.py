import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI




api = CoinGeckoAPI()
bot = telebot.TeleBot('6185836382:AAHCHt2N632Hkd2h3IImnOWGu1rhIAVFo88')
base_currency = 'usd'
base_currency1 = 'rub'


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='💸USD💸')
    btn2 = types.KeyboardButton(text='💵RUB💵')
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id,'Выбери в какую валюту нужно переводить цену',reply_markup=kb)





@bot.message_handler(content_types=['text'])
def crypto_price_usd(message):
    if message.text == '💸USD💸':
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='bitcoin')
        btn2 = types.KeyboardButton(text='ethereum')
        btn3 = types.KeyboardButton(text='Обратно')
        kb.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выбери валюту или выйди обратно', reply_markup=kb)

    if message.text == 'bitcoin':
        crypto_id = message.text
        price = api.get_price(ids=crypto_id, vs_currencies="usd")

        if price:
            price = price[crypto_id][base_currency]
        else:
            bot.send_message(message.chat.id, "Не найден")
            return

        bot.send_message(message.chat.id, f"цена {crypto_id}={price}$")

    elif message.text == 'ethereum':
        crypto_id = message.text
        price = api.get_price(ids=crypto_id, vs_currencies="usd")

        if price:
            price = price[crypto_id][base_currency]
        else:
            bot.send_message(message.chat.id, "Не найден")
            return

        bot.send_message(message.chat.id, f"Цена {crypto_id}={price}$")

    elif message.text == 'Обратно':
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='💸USD💸')
        btn2 = types.KeyboardButton(text='💵RUB💵')
        kb.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Выбери в какую валюту нужно переводить цену', reply_markup=kb)



    if message.text == '💵RUB💵':
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Bitcoin')
        btn2 = types.KeyboardButton(text='usd')
        btn3 = types.KeyboardButton(text='обратно')
        kb.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выбери валюту', reply_markup=kb)

    if message.text == 'Bitcoin':
        message.text = 'bitcoin'
        crypto_id = message.text
        price = api.get_price(ids=crypto_id, vs_currencies="rub")

        if price:
            price = price[crypto_id][base_currency1]
        else:
            bot.send_message(message.chat.id, "Не найден")
            return

        bot.send_message(message.chat.id, f"Цена {crypto_id}={price}₽")


    elif message.text == 'usd':
        crypto_id = message.text
        price = api.get_price(ids=crypto_id, vs_currencies="rub")

        if price:
            price = price[crypto_id][base_currency1]
        else:
            bot.send_message(message.chat.id, "Не найден")
            return

        bot.send_message(message.chat.id, f"Цена {crypto_id}={price}₽")

    elif message.text == 'обратно':
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='💸USD💸')
        btn2 = types.KeyboardButton(text='💵RUB💵')
        kb.add(btn1, btn2)
        bot.send_message(message.chat.id, 'Выбери в какую валюту нужно переводить цену', reply_markup=kb)




if __name__ == '__main__':
    bot.polling()
