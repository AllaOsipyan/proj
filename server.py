import telebot
from b import BotHandler
from  recipe import Recipe
from newUser import NewUser
from telebot import types
bot = telebot.TeleBot('631641496:AAH6KyVo5Ct02QppaOx7rLoxTJqaSlgu1Po')
def selectIngr(upd):
    k=True
    while k:
        upd.last_Up=upd.update
        hm = "Введите ингредиенты через запятую"
        BotHandler.send_message(BotHandler(), upd.from_, hm)
        get_mess(upd)
        upd.data.ingridients.append(str(upd.message).split(','))

        hm = "Хотите добавить еще ингредиентов?"
        BotHandler.send_message(BotHandler(), upd.from_, hm)
        upd.message = get_mess(upd)
        if upd.message =='нет':
            k = False
    #upd.data.names = етод получения рецептов по ингредиентам
    select_rec(upd)

def select_rec(upd):
    hm = "Топ 10 рецептов:"
    BotHandler.send_message(BotHandler(), upd.from_, hm)
    # upd.data.names[]
    upd.last_Up = upd.update
    hm = "Введите название рецепта"
    BotHandler.send_message(BotHandler(), upd.from_, hm)

    upd.data.name = get_mess(upd)  # нужно конвертить цифру в название
    # (upd.data) вызов функции обработки данных
    BotHandler.send_message(BotHandler(), upd.from_, upd.data.name)
    BotHandler.send_message(BotHandler(), upd.from_, upd.data.ingridients)
    BotHandler.send_message(BotHandler(), upd.from_, upd.data.instructions)
    BotHandler.send_message(BotHandler(), upd.from_, upd.data.raiting)

def selectCateg(upd):
    upd.last_Up = upd.update
    hm = "Выберите категорию: "
    BotHandler.send_message(BotHandler(), upd.from_, hm)
    # метод вывода категорий
    get_mess(upd)
    upd.data.categ=upd.message
    selectIngr(upd)

def selectAuthor(upd):
    upd.last_Up = upd.update
    hm = "Вывести список авторов?"
    BotHandler.send_message(BotHandler(), upd.from_, hm)
    if get_mess(upd)=="да":
        pass #метод получения списка авторов
    upd.last_Up = upd.update
    hm = "Введите имя автора"
    BotHandler.send_message(BotHandler(), upd.from_, hm)
    upd.data.author = get_mess(upd)
    #вызов метода получения рецептов по автору
    select_rec(upd)

def selectRating(upd):
    hm = "Выберите рейтинг(0, 20, 40, 60, 80 или 100)"
    BotHandler.send_message(BotHandler(), upd.from_, hm)
    upd.data.rating = get_mess(upd)
    #вызов метода полученя рецептов по рейтингу
    select_rec(upd)
    #отправиться в selectIngr()

def get_mess(upd):
    if newUpd.from_== BotHandler.get_prev_update(BotHandler())["message"]["from"]["id"]:
        upd.update = BotHandler.get_last_update(BotHandler())
    while upd.update == upd.last_Up:
        if newUpd.from_== BotHandler.get_prev_update(BotHandler())["message"]["from"]["id"]:
           upd.update = BotHandler.get_last_update(BotHandler())
    if upd.update:
        upd.update_id = upd.update["update_id"]
    try:
        upd.message = str(upd.update["message"]["text"]).lower().strip(" ")
    except:
        pass
    upd.last_Up=upd.update
    return upd.message
# @bot.message_handler(commands=['start'])
# def keyBoard(upd, mess):
#     keyboard = types.InlineKeyboardMarkup()
#     callback_button = types.InlineKeyboardButton(text=mess, callback_data="test")
#     keyboard.add(callback_button)
#     bot.send_message(upd.chat_id, "", reply_markup=keyboard)

def make_reply(upd):

    if newUpd.message is not None:
        reply="kxzkjx"
        if upd.message == "Начать":#попробовать кнопки
            # keyBoard("Введите тип поиска", list = ["По ингредиентам", "По категориям", "По автору", "По рейтингу"])
            reply="Введите тип поиска"
        elif upd.message =="По ингредиентам":
            selectIngr(upd)
            reply="Для того чтобы начать сначала напишите Начать"
        elif upd.message == "По категориям":
            selectCateg(upd)
            reply = "Для того чтобы начать сначала напишите Начать"
        elif upd.message=="По автору":
            selectAuthor(upd)
            reply = "Для того чтобы начать сначала напишите Начать"
        elif upd.message == "По рейтингу":
            selectRating(upd)
            reply = "Для того чтобы начать сначала напишите Начать"
        else:
            reply = "Пожалуйста, выберите поиск по одному из заданных критериев"
    return reply





users=dict()

while True:
    print(BotHandler.get_last_update(BotHandler()))
    user_id = BotHandler.get_last_update(BotHandler())["message"]["from"]["id"]
    if  user_id not in users:
        users[user_id]= NewUser(BotHandler.get_last_update(BotHandler()), BotHandler.get_last_update(BotHandler()), user_id,BotHandler.get_last_update(BotHandler())["message"]["chat"]["id"])
    newUpd = users[user_id]

    if newUpd.from_== BotHandler.get_prev_update(BotHandler())["message"]["from"]["id"]:
        newUpd.update = BotHandler.get_last_update(BotHandler())#!найти последнее обновление именно этого пользователя

    if newUpd.update != newUpd.last_Up:
        if newUpd.update:
            newUpd.up_id = newUpd.update["update_id"]
            try:
                newUpd.message = str(newUpd.update["message"]["text"])
                if newUpd.message == 'Начать':
                    newUpd.data.clear()
            except:
                newUpd.message = None
            make_reply(newUpd)

    newUpd.last_Up = newUpd.update
