# Version 0.2.5 
# Creator Nater, @subadmin3
# Добавлен Патч Безопасности
from cgitb import text
from email import message
from gc import callbacks
import imp
import telebot
import config
import random
import os
import time
import datetime
import imp
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    if message.chat.type == 'supergroup':
        sypergroup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        syp1 = types.KeyboardButton("!ботик")
        sypergroup.add(syp1)
        bot.send_message(message.chat.id, "Это сообщение видно лишь при страте в группе", reply_markup=sypergroup)
    elif message.chat.type == 'private':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("⭕ Веб-Архив")
        item3 = types.KeyboardButton("😃 Профиль")
        item4 = types.KeyboardButton("💢 Команды")
        item5 = types.KeyboardButton("🎮 Игры")
        markup.add(item1, item3, item4, item5)
        bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    

@bot.message_handler(content_types=['text'])
def boss(message):
    dtn = datetime.datetime.now()
    log = open('log/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    log.writelines(dtn.strftime("%d-%m-%Y %H:%M") + '\n')
    log.writelines(f"Message from {str(message.chat.first_name)} {str(message.chat.last_name)} {str(message.chat.id)} \n")
    log.writelines(f"Text: {str(message.text)} \n")
    log.close
    # print(f"Message from {str(message.chat.first_name)} {str(message.chat.last_name)} {str(message.chat.id)}")
    # print(f"Text: {str(message.text)}")
    # f = open('log/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    # s = bot(message.text)
    # f.write('user: ' + message.text + '\n' + s + '\n')
    # f.close()
    # # Отправка ответа
    # bot.send_message(message.chat.id, s)
    a = 1
    if a == 1:
        if message.chat.type == 'private':  #private message.chat.type == 'private'
            if message.text == '💢 Команды':
                bot.send_message(message.chat.id, "⚠️Список команды ⚠️ \n❌ !Профиль - выводит данные вашего профиля для некоторых доп. функции для бота.  \n✅ !Dio - Просто чтобы было. \n❌ !РП - Рол-Плей команды (ударить, трахнуть и тд) \n❌ !Инфо - Выводит информацию о боте (список обновления, аплеты и тд) \n❌ !Группы - Список всех прилегающих групп АвеСатан \n❌ !Поддержка - Контенты админа \n❌ !Игра - Хз ещё не придумал")
            elif message.text == '⭕ Веб-Архив':
                markup = types.InlineKeyboardMarkup(row_width=2)
                if message.chat.id in config.data1: 
                    markup1 = types.InlineKeyboardMarkup(row_width=2)
                    item1 = types.InlineKeyboardButton("29.01.22+", callback_data='29.01.22')
                    item2 = types.InlineKeyboardButton("26.01.22", callback_data='26.01.22')
                    item3 = types.InlineKeyboardButton("31.10.21", callback_data='31.10.21')
                    item4 = types.InlineKeyboardButton("16.10.21+", callback_data='16.10.21')
                    item5 = types.InlineKeyboardButton("14.10.21", callback_data='14.10.21')
                    item6 = types.InlineKeyboardButton("04.09.21", callback_data='04.09.21')
                    item7 = types.InlineKeyboardButton("26.08.21", callback_data='26.08.21')
                    item8 = types.InlineKeyboardButton("16.08.21", callback_data='16.08.21')
                    item9 = types.InlineKeyboardButton("29.07.21+", callback_data='29.07.21')
                    item10 = types.InlineKeyboardButton("15.06.21", callback_data='15.06.21')
                    item11 = types.InlineKeyboardButton("10.06.21", callback_data='10.06.21')
                    markup1.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
                    bot.send_message(message.chat.id, 'Веб-Архив Все Помнит, \n ПОВЫШЕНОЕ ПРАВА', reply_markup=markup1)
                elif message.chat.id == config.rostik_katia:
                    item2 = types.InlineKeyboardButton("26.01.22", callback_data='26.01.22')
                    item3 = types.InlineKeyboardButton("31.10.21", callback_data='31.10.21')
                    item4 = types.InlineKeyboardButton("16.10.21+", callback_data='16.10.21')
                    item5 = types.InlineKeyboardButton("14.10.21", callback_data='14.10.21')
                    item6 = types.InlineKeyboardButton("04.09.21", callback_data='04.09.21')
                    item7 = types.InlineKeyboardButton("26.08.21", callback_data='26.08.21')
                    item8 = types.InlineKeyboardButton("16.08.21", callback_data='16.08.21')
                    item9 = types.InlineKeyboardButton("29.07.21+", callback_data='29.07.21')
                    item10 = types.InlineKeyboardButton("15.06.21", callback_data='15.06.21')
                    item11 = types.InlineKeyboardButton("10.06.21", callback_data='10.06.21')
                    markup.add(item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
                    bot.send_message(message.chat.id, 'Веб-Архив Все Помнит \n ОБЫЧНЫЕ ПРАВА', reply_markup=markup)
                else:
                    bot.send_message(message.chat.id, "{0.first_name} запрешено просматривать веб архив \nПо всем вопросам писать <b>@subadmin3</b>".format(message.from_user, bot.get_me()),
                    parse_mode='html', reply_markup=markup)
            elif message.text == '😃 Профиль': 
                if message.chat.id == config.PELMENI:
                    bot.send_message(message.chat.id, "А я знаю что ты саша пельмешка")
                elif message.chat.id == config.ADMIN:
                    # adminka = types.InlineKeyboardMarkup(row_width=1)
                    # admin_button = types.InlineKeyboardButton("Рассилка 🅰")
                    # adminka.add(admin_button)
                    bot.send_message(message.chat.id, "Админка ваша величество")
                    bot.send_document(message.chat.id, file_id)
                    # bot.send_message(message.chat.id, 'Enter SPAM text: ')
                elif message.chat.id == config.SASHAG:
                    bot.send_message(message.chat.id, "Ты Гей")
                elif message.chat.id == config.DIANA:
                    bot.send_message(message.chat.id, "Маааасло")
                elif message.chat.id == config.KATIAG:
                    bot.send_message(message.chat.id, "Лол, я знаю что ты Катя")
                else:
                    bot.send_message(message.chat.id, "Ты хто такой")
            elif message.text == '🎮 Игры':
                # Game
                markup3 = types.InlineKeyboardMarkup(row_width=1)
                gamebutton = types.InlineKeyboardButton("Agario Online", callback_data='Agario')
                gamebutton1 = types.InlineKeyboardButton("Soon", callback_data='Soon')
                markup3.add(gamebutton, gamebutton1)
                bot.send_message(message.chat.id, "🎮 Список Игр 🎮", reply_markup=markup3)
            elif message.text == '!Dio':
                bot.send_photo(message.chat.id, 'https://static.wikia.nocookie.net/jojo/images/0/0a/DIO_Normal_SC_Infobox_Anime.png/revision/latest?cb=20210610083452&path-prefix=ru')
            elif message.text == '!ботик':
                bot.send_message(message.chat.id, "Бот находится тут: \n@avesatan_bot")
            else:
                bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
        if message.chat.type == 'supergroup':
            if message.text == '!ботик':
                bot.send_message(message.chat.id, "Бот находится тут: \n@avesatan_bot")
    else:
        bot.send_message(message.chat.id, 'Не являешся участником Ave Satan Version 2')       

@bot.message_handler('sticker')
def hello(message):
        bot.send_message(message.chat.id, "Найс Стикер Бро")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Spam':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == 'Agario':
                bot.send_game(call.message.chat.id, game_short_name='')
                @bot.callback_query_handler(func=lambda callback_query: callback_query.game_short_name == 'agario')
                def game(call):
                    bot.answer_callback_query(callback_query_id=call.id, url='https://www.agar.io/#ffa')
                    bot.send_message(call.message.chat.id, "Aa")
            elif call.data == 'kaki':
                bot.send_message(call.message.chat.id, 'Зачем ты это нажал, тебе реально \n интересно как бот будет какать 🤨🤨🤨')
            elif call.data == '29.01.22':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/YUBYosKVvS9oYRFQ8')
            elif call.data == '26.01.22':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/Yz6q9bF2seyQWrPC7')
            elif call.data == '31.10.21':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/sJo3c88KAf6XCEP87')
            elif call.data == '16.10.21':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/unqA3TyViGFB1Jox5')
            elif call.data == '14.10.21':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/qXXueoUCcTA1VhdZ6')
            elif call.data == '04.09.21':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/8tYu5k6U9GqCouS4A')
            elif call.data == '26.08.21':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/rmhVxVNnjmET2f6GA')
            elif call.data == '16.08.21':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/xkaTcf5RYfmPu39K7')
            elif call.data == '29.07.21':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/EyDTyHc8YZ8rkbvQ8')
            elif call.data == '15.06.21':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/CiatsMrzia4r9F4P7')
            elif call.data == '10.06.21':
                bot.send_message(call.message.chat.id, 'https://photos.app.goo.gl/9WK3DPAYqTHjvXbV7')
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Воспоминания за это число", reply_markup=None)
 
            # Если False то всплывает тенивое сообщение Если True то всплывает окно уведомление с кнопкой "ОК"
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #     text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!")
    except Exception as e:
        print(repr(e))
 

# # Запись логов
    # f = open('log/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    # s = bot(message.text)
    # f.write('user: ' + message.text + '\n' + s + '\n')
    # f.close()
    # # Отправка ответа
    # bot.send_message(message.chat.id, s)

 # @bot.message_handler(content_types=['text'])
# def repeat_all_message(message):
#   print(message.chat.id)
#   if message.chat.id == ADMIN:
#     bot.send_message(message.chat.id,'Ты админ')
#   else:
#     bot.send_message(message.chat.id,'Ты не админ')

print('bot has bean started')
# RUN
bot.polling(none_stop=True)



