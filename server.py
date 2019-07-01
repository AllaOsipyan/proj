from b import BotHandler

update_id = None


def make_reply(msg):

    if msg is not None:
        if msg == "Привет":
            reply = "Привет, дорогой друг!"
        else:
            reply = "Я вас не понимаю, пожалуйста, напишите ингредиенты"
    return reply
lastUpdate = BotHandler.get_last_update(BotHandler())
while True:
    print("...")
    update = BotHandler.get_last_update(BotHandler())
    if update != lastUpdate:
        if update:
            update_id = update["update_id"]
            try:
                message = update["message"]["text"]
            except:
                message = None
            from_ = update["message"]["from"]["id"]
            reply = make_reply(message)
            BotHandler.send_message(BotHandler(),from_,reply )
        lastUpdate=update
