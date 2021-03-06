import schedule
import telebot
import config

from telebot import types
from threading import Thread
from time import sleep
from datetime import datetime


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Время старта программы =", current_time)


bot = telebot.TeleBot(config.TOKEN)
some_id = 735662028

@bot.message_handler (commands=['start'])
def welcome(message):
    sticker = open('sticker/sticker.webp', 'rb')
    bot.send_sticker(some_id, sticker)

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Время начала работы бота", callback_data='Time')
    item2 = types.InlineKeyboardButton("ТЫ натурал?", callback_data='natural')

    markup.add(item1, item2)

    bot.send_message (message.from_user.id, 'Добро пожаловать, Человек!\nЯ - <b>{1.first_name}</b>, бот созданые как ежедневник для Neewal!'.format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    print("Сообщение 'welcome' отправлено!")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Time':
                bot.send_message(call.message.chat.id, current_time)
            elif call.data == 'natural':
                bot.send_message(call.message.chat.id, 'БЫВАЕТ(')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Добро пожаловать, Человек!\nЯ - <b>Олег</b>, бот созданые как ежедневник для Neewal!",
                parse_mode='html', reply_markup=None)
    except Exception as e:
            print(repr(e))

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def test():
    return bot.send_message(some_id, "Доброе утро, {0.first_name}!")
    print("Сообщение 'welcome' отправлено!")


def good_morning():
    return bot.send_message(some_id, "Доброе утро, {0.first_name}!")
def go():
    return bot.send_message(some_id, "Пора одеваться, {0.first_name}!")


def one_lesson_start():
    return bot.send_message(some_id, "До первого урока осталось 5 минута!", print("start one_lesson_start"))
def one_lesson_start1():
    return bot.send_message(some_id, "До первого урока осталось 1 минута!", print("start one_lesson_start1"))
def one_lesson_go():
    return bot.send_message(some_id, "Первый урок начался!", print("start one_lesson_go"))
def one_lesson_end(): 
    return bot.send_message(some_id, "До окончания первого урока осталось 5 минута!", print("start one_lesson_end"))
def one_lesson_end1(): 
    return bot.send_message(some_id, "До окончания первого урока осталось 1 минута!", print("start one_lesson_end1"))
def one_lesson_stop():
    return bot.send_message(some_id, "Первый урок закончился!", print("start one_lesson_stop"))


def two_lesson_start():
    return bot.send_message(some_id, "До второго урока осталось 5 минута!", print("start two_lesson_start"))
def two_lesson_start1():
    return bot.send_message(some_id, "До второго урока осталось 1 минута!", print("start two_lesson_start1"))
def two_lesson_go():
    return bot.send_message(some_id, "Второй урок начался!", print("start two_lesson_go"))
def two_lesson_end():
    return bot.send_message(some_id, "До окончания второго урока осталось 5 минута!", print("start two_lesson_end"))
def two_lesson_end1():
    return bot.send_message(some_id, "До окончания второго урока осталось 1 минута!", print("start two_lesson_end1"))
def two_lesson_stop():
    return bot.send_message(some_id, "Второй урок закончился!", print("start two_lesson_stop"))


def three_lesson_start():
    return bot.send_message(some_id, "До третьего урока осталось 5 минута!", print("start three_lesson_start"))
def three_lesson_start1():
    return bot.send_message(some_id, "До третьего урока осталось 1 минута!", print("start three_lesson_start1"))
def three_lesson_go():
    return bot.send_message(some_id, "Третий урок начался!", print("start three_lesson_go"))
def three_lesson_end():
    return bot.send_message(some_id, "До окончания третьего урока осталось 5 минута!", print("start three_lesson_end"))
def three_lesson_end1():
    return bot.send_message(some_id, "До окончания третьего урока осталось 1 минута!", print("start three_lesson_end1"))
def three_lesson_stop():
    return bot.send_message(some_id, "Третий урок закончился!", print("start three_lesson_stop"))


def four_lesson_start():
    return bot.send_message(some_id, "До четвёртого урока осталось 5 минута!", print("start four_lesson_start"))
def four_lesson_start1():
    return bot.send_message(some_id, "До четвёртого урока осталось 1 минута!", print("start four_lesson_start1"))
def four_lesson_go():
    return bot.send_message(some_id, "Четвёртый урок начался!", print("start four_lesson_go"))
def four_lesson_end():
    return bot.send_message(some_id, "До окончания четвёртого урока осталось 5 минута!", print("start four_lesson_end"))
def four_lesson_end1():
    return bot.send_message(some_id, "До окончания четвёртого урока осталось 1 минута!", print("start four_lesson_end1"))
def four_lesson_stop():
    return bot.send_message(some_id, "Четвёртый урок закончился!", print("start four_lesson_stop"))


def five_lesson_start():
    return bot.send_message(some_id, "До пятого урока осталось 5 минута!", print("start five_lesson_start"))
def five_lesson_start1():
    return bot.send_message(some_id, "До пятого урока осталось 1 минута!", print("start five_lesson_start1"))
def five_lesson_go():
    return bot.send_message(some_id, "Пятый урок начался!", print("start five_lesson_go"))
def five_lesson_end():
    return bot.send_message(some_id, "До окончания пятого урока осталось 5 минута!", print("start five_lesson_end"))
def five_lesson_end1():
    return bot.send_message(some_id, "До окончания пятого урока осталось 1 минута!", print("start five_lesson_end1"))
def five_lesson_stop():
    return bot.send_message(some_id, "Пятый урок закончился!", print("start five_lesson_stop"))


def six_lesson_start():
    return bot.send_message(some_id, "До шестого урока осталось 5 минута!", print("start six_lesson_start"))
def six_lesson_start1():
    return bot.send_message(some_id, "До шестого урока осталось 1 минута!", print("start six_lesson_start1"))
def six_lesson_go():
    return bot.send_message(some_id, "Шестой урок начался!", print("start six_lesson_go"))
def six_lesson_end():
    return bot.send_message(some_id, "До окончания шестого урока осталось 5 минута!", print("start six_lesson_end"))
def six_lesson_end1():
    return bot.send_message(some_id, "До окончания шестого урока осталось 1 минута!", print("start six_lesson_end1"))
def six_lesson_stop():
    return bot.send_message(some_id, "Шестой урок закончился!", print("start six_lesson_stop"))


def seven_lesson_start():
    return bot.send_message(some_id, "До седьмого урока осталось 5 минута!", print("start seven_lesson_start"))
def seven_lesson_start1():
    return bot.send_message(some_id, "До седьмого урока осталось 1 минута!", print("start seven_lesson_start1"))
def seven_lesson_go():
    return bot.send_message(some_id, "Седьмой урок начался!", print("start seven_lesson_go"))
def seven_lesson_end():
    return bot.send_message(some_id, "До окончания седьмого урока осталось 5 минута!", print("start seven_lesson_end"))
def seven_lesson_end1():
    return bot.send_message(some_id, "До окончания седьмого урока осталось 1 минута!", print("start seven_lesson_end1"))
def seven_lesson_stop():
    return bot.send_message(some_id, "Седьмой урок закончился!", print("start seven_lesson_stop"))

if __name__ == "__main__":
    schedule.every().monday.at("07:00").do(good_morning)
    schedule.every().tuesday.at("07:00").do(good_morning)
    schedule.every().wednesday.at("07:00").do(good_morning)
    schedule.every().thursday.at("07:00").do(good_morning)
    schedule.every().friday.at("07:00").do(good_morning)


    schedule.every().monday.at("08:10").do(go)
    schedule.every().tuesday.at("08:10").do(go)
    schedule.every().wednesday.at("08:10").do(go)
    schedule.every().thursday.at("08:10").do(go)
    schedule.every().friday.at("08:10").do(go)

    # ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    schedule.every().monday.at("08:55").do(one_lesson_start)
    schedule.every().tuesday.at("08:55").do(one_lesson_start)
    schedule.every().wednesday.at("08:55").do(one_lesson_start)
    schedule.every().thursday.at("08:55").do(one_lesson_start)
    schedule.every().friday.at("08:55").do(one_lesson_start)

    schedule.every().monday.at("08:59").do(one_lesson_start1)
    schedule.every().tuesday.at("08:59").do(one_lesson_start1)
    schedule.every().wednesday.at("08:59").do(one_lesson_start1)
    schedule.every().thursday.at("08:59").do(one_lesson_start1)
    schedule.every().friday.at("08:59").do(one_lesson_start1)

    schedule.every().monday.at("09:00").do(one_lesson_go)
    schedule.every().tuesday.at("09:00").do(one_lesson_go)
    schedule.every().wednesday.at("09:00").do(one_lesson_go)
    schedule.every().thursday.at("09:00").do(one_lesson_go)
    schedule.every().friday.at("09:00").do(one_lesson_go)

    schedule.every().monday.at("09:40").do(one_lesson_end)
    schedule.every().tuesday.at("09:40").do(one_lesson_end)
    schedule.every().wednesday.at("09:40").do(one_lesson_end)
    schedule.every().thursday.at("09:40").do(one_lesson_end)
    schedule.every().friday.at("09:40").do(one_lesson_end)

    schedule.every().monday.at("09:44").do(one_lesson_end1)
    schedule.every().tuesday.at("09:44").do(one_lesson_end1)
    schedule.every().wednesday.at("09:44").do(one_lesson_end1)
    schedule.every().thursday.at("09:44").do(one_lesson_end1)
    schedule.every().friday.at("09:44").do(one_lesson_end1)

    schedule.every().monday.at("09:45").do(one_lesson_stop)
    schedule.every().tuesday.at("09:45").do(one_lesson_stop)
    schedule.every().wednesday.at("09:45").do(one_lesson_stop)
    schedule.every().thursday.at("09:45").do(one_lesson_stop)
    schedule.every().friday.at("09:45").do(one_lesson_stop)
 
    # ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    schedule.every().monday.at("09:50").do(two_lesson_start)
    schedule.every().tuesday.at("09:50").do(two_lesson_start)
    schedule.every().wednesday.at("09:50").do(two_lesson_start)
    schedule.every().thursday.at("09:50").do(two_lesson_start)
    schedule.every().friday.at("09:50").do(two_lesson_start)

    schedule.every().monday.at("09:54").do(two_lesson_start1)
    schedule.every().tuesday.at("09:54").do(two_lesson_start1)
    schedule.every().wednesday.at("09:54").do(two_lesson_start1)
    schedule.every().thursday.at("09:54").do(two_lesson_start1)
    schedule.every().friday.at("09:54").do(two_lesson_start1)

    schedule.every().monday.at("09:55").do(two_lesson_go)
    schedule.every().tuesday.at("09:55").do(two_lesson_go)
    schedule.every().wednesday.at("09:55").do(two_lesson_go)
    schedule.every().thursday.at("09:55").do(two_lesson_go)
    schedule.every().friday.at("09:55").do(two_lesson_go)

    schedule.every().monday.at("10:35").do(two_lesson_end)
    schedule.every().tuesday.at("10:35").do(two_lesson_end)
    schedule.every().wednesday.at("10:35").do(two_lesson_end)
    schedule.every().thursday.at("10:35").do(two_lesson_end)
    schedule.every().friday.at("10:35").do(two_lesson_end)

    schedule.every().monday.at("10:39").do(two_lesson_end1)
    schedule.every().tuesday.at("10:39").do(two_lesson_end1)
    schedule.every().wednesday.at("10:39").do(two_lesson_end1)
    schedule.every().thursday.at("10:39").do(two_lesson_end1)
    schedule.every().friday.at("10:39").do(two_lesson_end1)

    schedule.every().monday.at("10:40").do(two_lesson_stop)
    schedule.every().tuesday.at("10:40").do(two_lesson_stop)
    schedule.every().wednesday.at("10:40").do(two_lesson_stop)
    schedule.every().thursday.at("10:40").do(two_lesson_stop)
    schedule.every().friday.at("10:40").do(two_lesson_stop)

    # ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    schedule.every().monday.at("10:55").do(three_lesson_start)
    schedule.every().tuesday.at("10:55").do(three_lesson_start)
    schedule.every().wednesday.at("10:55").do(three_lesson_start)
    schedule.every().thursday.at("10:55").do(three_lesson_start)
    schedule.every().friday.at("10:55").do(three_lesson_start)

    schedule.every().monday.at("10:59").do(three_lesson_start1)
    schedule.every().tuesday.at("10:59").do(three_lesson_start1)
    schedule.every().wednesday.at("10:59").do(three_lesson_start1)
    schedule.every().thursday.at("10:59").do(three_lesson_start1)
    schedule.every().friday.at("10:59").do(three_lesson_start1)

    schedule.every().monday.at("11:00").do(three_lesson_go)
    schedule.every().tuesday.at("11:00").do(three_lesson_go)
    schedule.every().wednesday.at("11:00").do(three_lesson_go)
    schedule.every().thursday.at("11:00").do(three_lesson_go)
    schedule.every().friday.at("11:00").do(three_lesson_go)

    schedule.every().monday.at("11:40").do(three_lesson_end)
    schedule.every().tuesday.at("11:40").do(three_lesson_end)
    schedule.every().wednesday.at("11:40").do(three_lesson_end)
    schedule.every().thursday.at("11:40").do(three_lesson_end)
    schedule.every().friday.at("11:40").do(three_lesson_end)

    schedule.every().monday.at("11:44").do(three_lesson_end1)
    schedule.every().tuesday.at("11:44").do(three_lesson_end1)
    schedule.every().wednesday.at("11:44").do(three_lesson_end1)
    schedule.every().thursday.at("11:44").do(three_lesson_end1)
    schedule.every().friday.at("11:44").do(three_lesson_end1)

    schedule.every().monday.at("11:45").do(three_lesson_stop)
    schedule.every().tuesday.at("11:45").do(three_lesson_stop)
    schedule.every().wednesday.at("11:45").do(three_lesson_stop)
    schedule.every().thursday.at("11:45").do(three_lesson_stop)
    schedule.every().friday.at("11:45").do(three_lesson_stop)
 
    # ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    schedule.every().monday.at("11:50").do(four_lesson_start)
    schedule.every().tuesday.at("11:50").do(four_lesson_start)
    schedule.every().wednesday.at("11:50").do(four_lesson_start)
    schedule.every().thursday.at("11:50").do(four_lesson_start)
    schedule.every().friday.at("11:50").do(four_lesson_start)

    schedule.every().monday.at("11:54").do(four_lesson_start1)
    schedule.every().tuesday.at("11:54").do(four_lesson_start1)
    schedule.every().wednesday.at("11:54").do(four_lesson_start1)
    schedule.every().thursday.at("11:54").do(four_lesson_start1)
    schedule.every().friday.at("11:54").do(four_lesson_start1)

    schedule.every().monday.at("11:55").do(four_lesson_go)
    schedule.every().tuesday.at("11:55").do(four_lesson_go)
    schedule.every().wednesday.at("11:55").do(four_lesson_go)
    schedule.every().thursday.at("11:55").do(four_lesson_go)
    schedule.every().friday.at("11:55").do(four_lesson_go)

    schedule.every().monday.at("12:35").do(four_lesson_end)
    schedule.every().tuesday.at("12:35").do(four_lesson_end)
    schedule.every().wednesday.at("12:35").do(four_lesson_end)
    schedule.every().thursday.at("12:35").do(four_lesson_end)
    schedule.every().friday.at("12:35").do(four_lesson_end)

    schedule.every().monday.at("12:39").do(four_lesson_end1)
    schedule.every().tuesday.at("12:39").do(four_lesson_end1)
    schedule.every().wednesday.at("12:39").do(four_lesson_end1)
    schedule.every().thursday.at("12:39").do(four_lesson_end1)
    schedule.every().friday.at("12:39").do(four_lesson_end1)

    schedule.every().monday.at("12:40").do(four_lesson_stop)
    schedule.every().tuesday.at("12:40").do(four_lesson_stop)
    schedule.every().wednesday.at("12:40").do(four_lesson_stop)
    schedule.every().thursday.at("12:40").do(four_lesson_stop)
    schedule.every().friday.at("12:40").do(four_lesson_stop)

    # ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    schedule.every().monday.at("12:55").do(five_lesson_start)
    schedule.every().tuesday.at("12:55").do(five_lesson_start)
    schedule.every().wednesday.at("12:55").do(five_lesson_start)
    schedule.every().thursday.at("12:55").do(five_lesson_start)
    schedule.every().friday.at("12:55").do(five_lesson_start)

    schedule.every().monday.at("12:59").do(five_lesson_start1)
    schedule.every().tuesday.at("12:59").do(five_lesson_start1)
    schedule.every().wednesday.at("12:59").do(five_lesson_start1)
    schedule.every().thursday.at("12:59").do(five_lesson_start1)
    schedule.every().friday.at("12:59").do(five_lesson_start1)

    schedule.every().monday.at("13:00").do(five_lesson_go)
    schedule.every().tuesday.at("13:00").do(five_lesson_go)
    schedule.every().wednesday.at("13:00").do(five_lesson_go)
    schedule.every().thursday.at("13:00").do(five_lesson_go)
    schedule.every().friday.at("13:00").do(five_lesson_go)

    schedule.every().monday.at("13:40").do(five_lesson_end)
    schedule.every().tuesday.at("13:40").do(five_lesson_end)
    schedule.every().wednesday.at("13:40").do(five_lesson_end)
    schedule.every().thursday.at("13:40").do(five_lesson_end)
    schedule.every().friday.at("13:40").do(five_lesson_end)

    schedule.every().monday.at("13:44").do(five_lesson_end1)
    schedule.every().tuesday.at("13:44").do(five_lesson_end1)
    schedule.every().wednesday.at("13:44").do(five_lesson_end1)
    schedule.every().thursday.at("13:44").do(five_lesson_end1)
    schedule.every().friday.at("13:44").do(five_lesson_end1)

    schedule.every().monday.at("13:45").do(five_lesson_stop)
    schedule.every().tuesday.at("13:45").do(five_lesson_stop)
    schedule.every().wednesday.at("13:45").do(five_lesson_stop)
    schedule.every().thursday.at("13:45").do(five_lesson_stop)
    schedule.every().friday.at("13:45").do(five_lesson_stop)

    # ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    schedule.every().monday.at("13:50").do(six_lesson_start)
    schedule.every().tuesday.at("13:50").do(six_lesson_start)
    schedule.every().wednesday.at("13:50").do(six_lesson_start)
    schedule.every().thursday.at("13:50").do(six_lesson_start)
    schedule.every().friday.at("13:50").do(six_lesson_start)

    schedule.every().monday.at("13:54").do(six_lesson_start1)
    schedule.every().tuesday.at("13:54").do(six_lesson_start1)
    schedule.every().wednesday.at("13:54").do(six_lesson_start1)
    schedule.every().thursday.at("13:54").do(six_lesson_start1)
    schedule.every().friday.at("13:54").do(six_lesson_start1)

    schedule.every().monday.at("13:55").do(six_lesson_go)
    schedule.every().tuesday.at("13:55").do(six_lesson_go)
    schedule.every().wednesday.at("13:55").do(six_lesson_go)
    schedule.every().thursday.at("13:55").do(six_lesson_go)
    schedule.every().friday.at("13:55").do(six_lesson_go)

    schedule.every().monday.at("14:35").do(six_lesson_end)
    schedule.every().tuesday.at("14:35").do(six_lesson_end)
    schedule.every().wednesday.at("14:35").do(six_lesson_end)
    schedule.every().thursday.at("14:35").do(six_lesson_end)
    schedule.every().friday.at("14:35").do(six_lesson_end)

    schedule.every().monday.at("14:39").do(six_lesson_end1)
    schedule.every().tuesday.at("14:39").do(six_lesson_end1)
    schedule.every().wednesday.at("14:39").do(six_lesson_end1)
    schedule.every().thursday.at("14:39").do(six_lesson_end1)
    schedule.every().friday.at("14:39").do(six_lesson_end1)

    schedule.every().monday.at("14:40").do(six_lesson_stop)
    schedule.every().tuesday.at("14:40").do(six_lesson_stop)
    schedule.every().wednesday.at("14:40").do(six_lesson_stop)
    schedule.every().thursday.at("14:40").do(six_lesson_stop)
    schedule.every().friday.at("14:40").do(six_lesson_stop)

    # ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    schedule.every().monday.at("14:55").do(seven_lesson_start)
    schedule.every().monday.at("14:59").do(seven_lesson_start1)
    schedule.every().monday.at("15:00").do(seven_lesson_go)
    schedule.every().monday.at("15:40").do(seven_lesson_end)
    schedule.every().monday.at("15:44").do(seven_lesson_end1)
    schedule.every().monday.at("15:45").do(seven_lesson_stop)

    # ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    schedule.every().tuesday.at("14:55").do(seven_lesson_start)
    schedule.every().tuesday.at("14:59").do(seven_lesson_start1)
    schedule.every().tuesday.at("15:00").do(seven_lesson_go)
    schedule.every().tuesday.at("15:40").do(seven_lesson_end)
    schedule.every().tuesday.at("15:44").do(seven_lesson_end1)
    schedule.every().tuesday.at("15:45").do(seven_lesson_stop)

    # ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    schedule.every().wednesday.at("14:55").do(seven_lesson_start)
    schedule.every().wednesday.at("14:59").do(seven_lesson_start1)
    schedule.every().wednesday.at("15:00").do(seven_lesson_go)
    schedule.every().wednesday.at("15:40").do(seven_lesson_end)
    schedule.every().wednesday.at("15:44").do(seven_lesson_end1)
    schedule.every().wednesday.at("15:45").do(seven_lesson_stop)

    Thread(target=schedule_checker).start()

bot.polling (none_stop=True)