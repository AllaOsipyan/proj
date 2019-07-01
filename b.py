import telebot
import requests
import datetime
import json
import configparser as cfg
class BotHandler:
    def __init__(self):
        self.base = "https://api.telegram.org/bot705945456:AAEW_vQWoL-lEqX_cpTZv7L55FmSYBGzH0I"

    def get_updates(self, offset=None):
        url = self.base + "/getUpdates"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return  json.loads(r.content)
    def send_message(self, chat_id, text):
        url = self.base + "/sendMessage?chat_id={}&text={}".format(chat_id, text)
        if text is not None:
            requests.get(url)

    def get_last_update(self):
        get_result = self.get_updates()
        get_result1 = get_result["result"]
        d = len(get_result1)
        last_update = get_result["result"][len(get_result1)-1]
        return last_update
