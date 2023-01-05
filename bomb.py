# -*- coding: utf-8 -*-

import vk_api
import time
import json
import random
import datetime

vk = vk_api.VkApi(token="38b25da0a4608c3a3fbcd7ee1650f36b3d1a28eadb0d4549bdad4cb52de0e2168999b6b9d6ca2e8630063")
vk._auth_token()


def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])


print('The server is running')

print(datetime.date.today())

print('В формате : ', 'год - месяц - день')

print(' ')

print('Cписок сообщений и id пользователей : ')

# Выбор класса
keyboard = {
    "one_time": True,
    "buttons": [

        [get_button(label="Тиму", color="positive"),
         get_button(label="Мияги", color="positive")],
        [get_button(label="Ваники", color="positive"),
         get_button(label="Героиники", color="positive")],
        [get_button(label="Нефорики", color="positive"),
         get_button(label="Телепорт", color="positive")]
    ]
}

# def bomber(number):



keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))





while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            message = messages["items"][0]["last_message"]["text"]

            if message == "Старт" or message == "Бомбить" or message == "бомбить" or message == "старт":
                vk.method("messages.send", {"peer_id": id,
                                            "message": "Привет, я бомбер бот. Напиши мне номер кого будем бомбить.",
                                            "keyboard": keyboard, "random_id": get_random_id()})
                vk.method("messages.send", {"peer_id": id,
                                            "message": "Введи номер в формате\n+7XXXXXXXXXX",
                                            "random_id": get_random_id()})


            # Обновление клавиатур
            elif message == "123123123":
                vk.method("messages.send",
                          {"peer_id": id, 'message': 'Бомбер запущен.', "keyboard": keyboard,
                           "random_id": get_random_id()})





            else:
                vk.method("messages.send", {"peer_id": id,
                                            "message": "Для начала работы напиши мне",
                                            "keyboard": keyboard, "random_id": get_random_id()})
                vk.method("messages.send", {"peer_id": id,
                                            "message": "Бомбить",
                                            "random_id": get_random_id()})

            time.sleep(0.05)

            print('"', message, '"', " от пользователя :", id, ';', 'Время - ', time.ctime())
            print(' ')

            vk_mess = message
            # filename = messages["items"][0]["last_message"]["from_id"]
            # file = open('{0}.txt'.format(filename), 'a', encoding='utf-8')
            # file.write('"' + message + '"' + ' - ' + 'Время : ' + time.ctime() + '\n')
            # file.write('\n')
            # file.close()



    except Exception as E:
        time.sleep(1)