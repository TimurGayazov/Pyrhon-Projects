# -*- coding: utf-8 -*-

import vk_api
import time
import json
from utils_1 import get_random_id



vk = vk_api.VkApi(token="Токен")
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

# Клавиатура появляется после команды "Начать"
keyboard = {
    "one_time": True,
    "buttons": [

     [get_button(label="Трейлеры 🎥", color="negative")],
     [get_button(label="Список премьер на 2019 год 🎬", color="primary")],
     [get_button(label="Сотрудничество 💸", color="positive")]


    ]
}

# Клавиатура появляется после нажатия кнопки "Трейлеры"
keyboard_2 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Хоббс и Шоу (2019)", color="positive"),
     get_button(label="Хищные птицы(2020)", color="positive")],
     [get_button(label="Человек-Паук: вдали от дома.", color="positive")],
     [get_button(label="Мстители: Финал.", color="positive"),
     get_button(label="Капитан Марвел(2019)", color="positive")],
     [get_button(label="Мстители: Финал- тв спот.", color="positive"),
     get_button(label="Дамбо(2019)", color="positive")],
     [get_button(label="Кладбище домашних животных(2019)", color="positive")],
     [get_button(label="Аладдин (2019)", color="positive")],
     [get_button(label="Вернуться в меню 🔙", color="negative")]

    ]
}




keyboard_season = {
    "one_time": False,
    "buttons": [

     #[get_button(label="Зима", color="positive")],
     [get_button(label="Весна 🌦", color="positive")],
     [get_button(label="Лето 🌞", color="positive")],
     [get_button(label="Осень ☔", color="positive")],
     [get_button(label="Вернуться в меню 🔙", color="negative")]

    ]
}


# Массивы хранящие в себе данные команд
conver = ['Начать']

But = ['Трейлеры 🎥', 'Инфо о паблике', 'Сотрудничество 💸', 'Свежие Новости', 'Вернуться в меню 🔙', 'Список премьер на 2019 год 🎬']

films = ['Хоббс и Шоу (2019)', 'Хищные птицы(2020)', 'Человек-Паук: вдали от дома.', 'Мстители: Финал.', 'Капитан Марвел(2019)', 'Мстители: Финал- тв спот.', 'Дамбо(2019)', 'Кладбище домашних животных(2019)', 'Аладдин (2019)']

month = ['Зима', 'Весна 🌦', 'Лето 🌞', 'Осень ☔']


premiere = ['winter', 'spring', 'summer', 'autumn']

premiere[1] = 'Капитан Марвел; Премьера — 7 марта 2019' + 'Дамбо; Премьера — 28 марта 2019'




# Для работы клавиатур
keyboard = json.dumps(keyboard,  ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

keyboard_2 = json.dumps(keyboard_2,  ensure_ascii=False).encode('utf-8')
keyboard_2 = str(keyboard_2.decode('utf-8'))

keyboard_season = json.dumps(keyboard_season,  ensure_ascii=False).encode('utf-8')
keyboard_season = str(keyboard_season.decode('utf-8'))







while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            message = messages["items"][0]["last_message"]["text"]
            # 'Начать'
            if message == conver[0]:
                vk.method("messages.send", {"peer_id": id, "message": "Привет! Я ГикБот 😎.  Выбери в меню то, что тебя интересует!", "keyboard": keyboard, "random_id": get_random_id()})
            # Ответ на команду Трейлеры : Появляется новая панель(Клавиатура)
            elif message == But[0]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Держи подборку самых свежих трейлеров 🔥🔥🔥' , "keyboard": keyboard_2, "random_id": get_random_id()})
            # Функции для обновления клавиатур 1 и 2
            elif message == 'update':
                vk.method("messages.send", {"peer_id": id, 'message': 'Клавиатура обновлена', "keyboard": keyboard, "random_id": get_random_id()})
            elif message == 'update1':
                vk.method("messages.send", {"peer_id": id, 'message': 'Клавиатура обновлена', "keyboard": keyboard_2, "random_id": get_random_id()})
            elif message == 'update2':
                vk.method("messages.send", {"peer_id": id, 'message': 'Клавиатура обновлена', "keyboard": keyboard_season, "random_id": get_random_id()})
            # Функция возвращает пользователя на главный экран
            elif message == But[4]:vk.method("messages.send", {"peer_id": id, 'message': 'Вы перешли в главное меню', "keyboard": keyboard, "random_id": get_random_id()})
            # список премьер на 2019 год
            elif message == But[5]:vk.method("messages.send", {"peer_id": id, 'message': 'Выбери время года, премьеры которого тебя интересуют', "keyboard": keyboard_season, "random_id": get_random_id()})
            # Кнопка сотруднечество
            elif message == But[2]:vk.method("messages.send", {"peer_id": id, "message": 'По вопросам рекламы \nhttps://vk.com/id414630527', "keyboard": keyboard, "random_id": get_random_id()})


            # Бот присылает определённое сообщение по трейлеру фильма
            elif message == films[0]:vk.method("messages.send", {"peer_id": id, "message": 'https://vk.com/videos-177379032?z=video-177379032_456239028%2Fclub177379032%2Fpl_-177379032_-2', "random_id": get_random_id()})

            elif message == films[1]:vk.method("messages.send", {"peer_id": id, "message": 'https://vk.com/videos-177379032?z=video-177379032_456239021%2Fclub177379032%2Fpl_-177379032_-2', "random_id": get_random_id()})

            elif message == films[2]:vk.method("messages.send", {"peer_id": id, "message": 'https://vk.com/videos-177379032?z=video-177379032_456239020%2Fclub177379032%2Fpl_-177379032_-2', "random_id": get_random_id()})

            elif message == films[3]:vk.method("messages.send", {"peer_id": id, "message": 'https://vk.com/videos-177379032?z=video-177379032_456239017%2Fclub177379032%2Fpl_-177379032_-2', "random_id": get_random_id()})

            elif message == films[4]:vk.method("messages.send", {"peer_id": id, "message": 'https://vk.com/videos-177379032?z=video-177379032_456239018%2Fclub177379032%2Fpl_-177379032_-2', "random_id": get_random_id()})

            elif message == films[5]:vk.method("messages.send", {"peer_id": id, "message": 'https://vk.com/videos-177379032?z=video-177379032_456239032%2Fclub177379032%2Fpl_-177379032_-2', "random_id": get_random_id()})

            elif message == films[6]:vk.method("messages.send", {"peer_id": id, "message": 'https://vk.com/geekipedia?w=wall-177379032_266', "random_id": get_random_id()})

            elif message == films[7]:vk.method("messages.send", {"peer_id": id, "message": 'https://vk.com/videos-177379032?z=video-177379032_456239036%2Fclub177379032%2Fpl_-177379032_-2', "random_id": get_random_id()})

            elif message == films[8]:vk.method("messages.send", {"peer_id": id, "message": 'https://vk.com/videos-177379032?z=video-177379032_456239039%2Fclub177379032%2Fpl_-177379032_-2', "random_id": get_random_id()})

            # Бот присылает пользователю список премьер на 2019 год по сортировке (месяца)
            elif message == month[1]:vk.method("messages.send", {"peer_id": id, "message": 'Держи самые топовые премьеры на эту весну 🆕🔥\n' + '\n1️⃣Капитан Марвел; Премьера — 7 марта 2019\n' + '\n2️⃣Дамбо; Премьера — 28 марта 2019\n' + '\n3️⃣Шазам; Премьера — 4 апреля 2019\n' + '\n4️⃣Хеллбой; Премьера — 11 апреля 2019\n' + '\n5️⃣Игра престолов 8-ой сезон; Премьера — 14 апреля 2019\n' + '\n6️⃣Мстители:Финал; Премьера — 25 апреля 2019\n' + '\n7️⃣Джон Уик 3; Премьера — 16 мая 2019\n' + '\n8️⃣Детектив Пикачу; Премьера — 16 мая 2019\n' + '\n9️⃣Аладдин; Премьера — 23 мая 2019\n' + '\n🔟Годзилла 2: Король монстров; Премьера — 30 мая 2019\n', "random_id": get_random_id()})
            elif message == month[2]:vk.method("messages.send", {"peer_id": id, "message": 'Держи самые топовые премьеры на это лето 🌞🔥\n' + '\n1️⃣Люди Икс: Темный Феникс; Премьера — 6 июня 2019\n' + '\n2️⃣Люди в черном: Интернэшнл; Премьера — 13 июня 2019\n' + '\n3️⃣История игрушек 4; Премьера — 20 июня 2019\n' + '\n4️⃣Человек-паук: Вдали от дома; Премьера — 4 июля 2019\n' + '\n5️⃣Король Лев; Премьера — 18 июля 2019\n' + '\n6️⃣Новые мутанты; Премьера — 1 августа 2019\n' + '\n7️⃣Хоббс и Шоу; Премьера — 1 августа 2019\n', "random_id": get_random_id()})
            elif message == month[3]:vk.method("messages.send", {"peer_id": id, "message": 'Держи самые топовые премьеры на эту осень 🍂🔥\n' + '\n1️⃣Оно 2; Премьера — 5 сентября 2019\n' + '\n2️⃣Джокер; Премьера — 3 октября 2019\n' + '\n3️⃣Соник; Премьера — 25 ноября 2019\n' + '\n4️⃣Зомбилэнд; Премьера — 11 октября 2019\n', "random_id": get_random_id()})

            # Функция ответа бота на непонятную ему ситуацию(Сообщение)
            else:vk.method("messages.send", {"peer_id": id, "message": "Я не понял тебя!", "random_id": get_random_id()})


            time.sleep(0.05)
    except Exception as E:
        time.sleep(1)