import telebot
import random
from telebot import types 
# import ssl
# from aiohttp import web
# import src

# from src import *
# from src.message import sendVideo


bot = telebot.TeleBot("5878230153:AAEcYYZrePdcRiWxl-hY1mzf03ZbkkMIEV4", parse_mode=None)

songs = ['Twice - Merry & Happy', 'Itzy - In the morning', 'Iz*one - Fiesta', 'Blackpink - Typa Girl', 'Aespa - Girls', 'New Jeans - Ditto']
names = ['Юкі', 'Найон', 'Йеджі', 'Дженні', 'Вінтер', 'Шухуа']
twice = ['Найон', 'Чоньон', 'Момо', 'Сана', 'Джіхьо', 'Міна', 'Дахьон', 'Чейон', 'Цзуі']
itzy = ['Йеджи', 'Ліа', 'Юна', 'Черьон', 'Рюджин']
leSserafim = ['Чевон', 'Сакура', 'Инче', 'Юнджин', 'Казуха']
newJeans = ['Херін', 'Мінджі', 'Хані', 'Хейон', 'Даніель']
aespa = ['Каріна', 'Вінтер', 'Жизель', 'НінНін']
quest = ['На чому побудований бот? - На Python', 'Бот працює завжди? - Поки ні, але скоро будемо це фіксити', 'В мене пропозиція, куди звернутись? - Напишіть боту команду /feedback']
picNayeon = ['https://i.scdn.co/image/ab6761610000e5ebbb55fc616733b6c09d48481f', 'https://file.tinnhac.com/resize/600x-/2022/06/14/20220614110606-a688.jpg', 'https://file.tinnhac.com/resize/600x-/2022/06/14/20220614110615-3ae9.jpg', 'https://a.allegroimg.com/original/118646/7f65b5f040f7a6979e9e14f16ddb/NAYEON-TWICE-IM-NAYEON-I-M-VERSION', 'https://file.tinnhac.com/resize/600x-/2022/06/14/20220614110613-d64d.jpg', 'https://pbs.twimg.com/media/FUk4KqeakAAldwA?format=jpg&name=4096x4096', 'https://pbs.twimg.com/media/FUpwKZ8VsAA2k4h.jpg:large']
picSeulgi = ['https://www.rollingstone.com/wp-content/uploads/2022/10/Seulgi-of-Red-Velvet.jpg', 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxgZTZJvBtoxNMnZod0nwD34K4YEfGQ_pghfSwxM8H-uJjmQHDIAocNHGb-ZR1dzg-90n6I-8fPEp7JQ8--YJNYjbskQ_eOq0Lc7fPrSf-j7obutgXIyj9qpbzz7ppSUSeKz8Twj8yPOsT__mLwCuZutGVG9WmNRTZCWjy1U-OwShzdTbih-mitlOk4A/s4096/seulgi-red-velvet-solo.jpeg', 'https://www.nme.com/wp-content/uploads/2022/10/seulgi-red-velvet-28-reasons-interview-2.jpg', 'https://i.redd.it/red-velvet-seulgi-the-1st-mini-album-28-reasons-teaser-v0-oywrjqpv1fq91.jpg?width=3141&format=pjpg&auto=webp&s=1580cd448c045f45e97057f4041cd7785c5350a7', 'https://a-static.besthdwallpaper.com/red-velvet-s-seulgi-28-reasons-mv-wallpaper-2048x1536-106622_26.jpg']
videoNayeon = [open('a.mp4', 'rb'), open('b.mp4', 'rb'), open('c.mp4', 'rb')]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if (message.chat.type == 'private'):
        print(types)
        bot.send_message(message.chat.id, "Вітаємо! Це k-pop-бот, який має інформацію про жіночі групи")

    elif (message.chat.type == 'group'):
        # print(types)
        bot.send_message(message.chat.id, 'Це k-pop-бот, який має інформацію про жіночі групи')

    elif (message.chat.type == 'supergroup'):
        # print(types)
        bot.send_message(message.chat.id, 'Привітики! Це k-pop-бот, який має інформацію про жіночі групи')

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, "Це k-pop-бот, який має інформацію про жіночі групи")

@bot.message_handler(commands=['getsong'])
def song(message):
	bot.send_message(message.chat.id, songs[random.randrange(len(songs))])

@bot.message_handler(commands=['questions'])
def question(message):
	bot.send_message(message.chat.id, quest[random.randrange(len(quest))])

@bot.message_handler(commands=['getname'])
def name(message):
	bot.send_message(message.chat.id, names[random.randrange(len(names))])

@bot.message_handler(commands=['feedback'])
def feedback_bot(message):
	bot.send_message(message.chat.id, 'Щоб написати пропозицію або скаргу, будь ласка, напишіть нам через @kpopFeedback_bot. Ми не відповімо вам, але врахуємо ваше повідомлення')

@bot.message_handler(commands=['companies'])
def company(message):
    if (message.chat.type == 'group'):
        bot.send_message(message.chat.id, 'Компанія вашої групи -  SM Entertaiment')
    elif (message.chat.type == 'supergroup'):
        bot.send_message(message.chat.id, 'Компанія вашої групи -  JYP Entertaiment')

@bot.message_handler(commands=['candies'])
def candy(message):
    if (message.chat.type == 'group'):
        bot.send_message(message.chat.id, 'Конфети для вашої групи -  Рошен')
    elif (message.chat.type == 'supergroup'):
        bot.send_message(message.chat.id, 'Конфети для вашої групи -  АВК')

@bot.message_handler(commands=['useful']) 
def useful_button(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Github", url='https://github.com/')
    button2 = types.InlineKeyboardButton("Stack Overflow", url='https://stackoverflow.com/')
    markup.add(button1)
    markup.add(button2)
    bot.send_message(message.chat.id,"Нажми на кнопку та перейди на сайт".format(message.from_user),reply_markup=markup)

@bot.message_handler(commands=['kpop']) 
def kpop_button(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Твайс", callback_data = 'sendNameTwice')
    button2 = types.InlineKeyboardButton("Ітзі", callback_data = 'sendNameItzy')
    button3 = types.InlineKeyboardButton("Ле Ссерафім", callback_data = 'sendNameSserafim')
    button4 = types.InlineKeyboardButton("Н'ю Джинс", callback_data = 'sendNameJeans')
    button5 = types.InlineKeyboardButton("Еспа", callback_data = 'sendNameAespa')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    bot.send_message(message.chat.id,"Нажми на кнопку".format(message.from_user),reply_markup=markup)

@bot.message_handler(commands=['pics']) 
def pics_button(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Найон", callback_data = 'sendPicNayeon')
    button2 = types.InlineKeyboardButton("Сильгі", callback_data = 'sendPicSeulgi')
    markup.add(button1)
    markup.add(button2)
    bot.send_message(message.chat.id,"Нажми на кнопку".format(message.from_user),reply_markup=markup)

@bot.message_handler(commands=['video']) 
def video_button(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Найон", callback_data = 'sendVideoNayeon')
    markup.add(button1)
    bot.send_message(message.chat.id,"Нажми на кнопку".format(message.from_user),reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
	if call.data == 'sendNameTwice': bot.send_message(call.from_user.id, twice[random.randrange(len(twice))])
	elif call.data == 'sendNameItzy': bot.send_message(call.from_user.id, itzy[random.randrange(len(itzy))])
	elif call.data == 'sendNameSserafim': bot.send_message(call.from_user.id, leSserafim[random.randrange(len(leSserafim))])
	elif call.data == 'sendNameJeans': bot.send_message(call.from_user.id, newJeans[random.randrange(len(newJeans))])
	elif call.data == 'sendNameAespa': bot.send_message(call.from_user.id, aespa[random.randrange(len(aespa))])
	elif call.data == 'sendPicNayeon': bot.send_photo(call.from_user.id, picNayeon[random.randrange(len(picNayeon))])
	elif call.data == 'sendPicSeulgi': bot.send_photo(call.from_user.id, picSeulgi[random.randrange(len(picSeulgi))], caption = 'Сильгі з Ред Велвет')
	elif call.data == 'sendVideoNayeon': bot.send_video(call.from_user.id, videoNayeon[random.randrange(len(videoNayeon))])

@bot.message_handler(content_types=['text'])
def delete_message(message):
    if (message.chat.type == 'private'):
        bot.delete_message(message.chat.id, message.message_id)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def inline(query):
	# print(query)
	# print(query.id)
    if (query.query ==  'kpop'):
        results = [types.InlineQueryResultArticle('1', 'Twice', types.InputTextMessageContent('Корейська група, сформована у 2015 році за допомогою шоу "Sixteen" на телеканалі "Mnet".')),types.InlineQueryResultArticle('2', 'Girls Generation', types.InputTextMessageContent('Корейська група, сформована у 2008 році, котрі до сих пір продовжують свою діяльність у к-поп індустрії.')),(types.InlineQueryResultArticle('3', 'Iz*One', types.InputTextMessageContent('Корейська група, сформована у 2018 році за допомогою шоу "Produce 48" на телеканалі "Mnet". Закінчили свій промоушен у 2021 році'))),]
        
        (bot.answer_inline_query(query.id, results))

bot.infinity_polling()	