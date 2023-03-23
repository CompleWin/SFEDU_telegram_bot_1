'''

made by complewin

'''

from datetime import datetime
import telebot
from config import *
import pytz

bot = telebot.TeleBot("5911254681:AAExn3rFlXSPyL-Ih58BUqzpw7UnEgn6d2c")


@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document',
                                    'text', 'location', 'contact', 'sticker'])
def start(message):
    if message.text == '/start':
        keyboard = telebot.types.InlineKeyboardMarkup()
        key_date = telebot.types.InlineKeyboardButton(text='Узнать сегодняшнюю неделю', callback_data='date')
        key_week = telebot.types.InlineKeyboardButton(text='/week', callback_data='week')
        key_help = telebot.types.InlineKeyboardButton(text='/help', callback_data='help')
        key_about = telebot.types.InlineKeyboardButton(text='/about', callback_data='about')
        keyboard.add(key_date)
        keyboard.add(key_week, key_about, row_width=2)
        bot.send_message(message.from_user.id, start_message + start_message_avtor, reply_markup=keyboard,
                         parse_mode="Markdown")
    elif message.text == "/help":
        bot.reply_to(message, start_message_help)
    elif message.text == 'Узнать сегодняшнюю неделю' or message.text == '/week':
        week(message)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'date':
        week(call.message)
    if call.data == 'week':
        week(call.message)
    if call.data == 'about':
        bot.send_message(call.message.chat.id, start_message_about, parse_mode="Markdown")


def week(message):
    tz = pytz.timezone('Europe/Moscow')
    date = str(datetime.now(tz).date()).split('-')
    if date[2][0] == '0':
        date[2] = date[2][1:]
    if date[1] == '03':
        if date[2] in top_week_march:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} марта - это *верхняя неделя*', parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} марта - это *нижняя неделя*', parse_mode="Markdown")
    if date[1] == '04':
        if date[2] in top_week_april:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} апреля - это *верхняя неделя*', parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} апреля - это *нижняя неделя*', parse_mode="Markdown")
    if date[1] == '05':
        if date[2] in top_week_may:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} мая - это *верхняя неделя*', parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} мая - это *нижняя неделя*', parse_mode="Markdown")
    if date[1] == '06':
        if date[2] in top_week_june:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} июня - это *верхняя неделя*', parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} июня - это *нижняя неделя*', parse_mode="Markdown")
    if date[1] == '07':
        if date[2] in top_week_july:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} июля - это *верхняя неделя*', parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, f'Сегодня {date[2]} июля - это *нижняя неделя*', parse_mode="Markdown")


if __name__ == '__main__':
    bot.polling(none_stop=True)
