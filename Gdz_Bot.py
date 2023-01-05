# -*- coding: utf-8 -*-

import vk_api
import time
import json
import random
import datetime

vk = vk_api.VkApi(token="Your token")
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

     [get_button(label="5️⃣ Класс", color="positive"),
     get_button(label="6️⃣ Класс", color="positive")],
     [get_button(label="7️⃣ Класс", color="positive"),
     get_button(label="8️⃣ Класс", color="positive")],
     [get_button(label="9️⃣ Класс", color="positive"),
     get_button(label="🔟 Класс", color="positive")]
    ]
}


keyboard_back = {
    "one_time": True,
    "buttons": [
     [get_button(label="Назад", color="primary")]
    ]
}
keyboard_instruction = {
    "one_time": True,
    "buttons": [

     [get_button(label="Инструкция", color="primary"),
     get_button(label="Разработчик👨‍💻", color="primary")],
     [get_button(label="Вернуться к выбору класса⬅", color="negative")]
    ]
}
# Список предметов 10 класс
keyboard_10kl = {
    "one_time": False,
    "buttons": [
     [get_button(label="Англ.яз-10", color="primary"),
     get_button(label="Алгебра-10", color="primary")],
     #get_button(label="Биология-9", color="primary")],
     #[get_button(label="География-10", color="primary")],
     #get_button(label="Информатика-9", color="primary")],
     #[get_button(label="Физика-9", color="primary"),
     #get_button(label="Химия-9", color="primary")],
    [get_button(label="Вернуться к выбору класса⬅", color="negative"),
    get_button(label="Администратор👨‍💻", color="default")]
    ]
}

# Список предметов 9 класса
keyboard_9kl = {
    "one_time": False,
    "buttons": [

     [get_button(label="Алгебра-9", color="primary"),
     get_button(label="Англ.яз-9", color="primary")],
     [get_button(label="Биология-9", color="primary"),
     get_button(label="Геометрия-9", color="primary")],
     [get_button(label="Информатика-9", color="primary"),
     get_button(label="Физика-9", color="primary")],
     [get_button(label="Химия-9", color="primary")],
    [get_button(label="Вернуться к выбору класса⬅", color="negative"),
    get_button(label="Администратор👨‍💻", color="default")]


    ]
}
# Список предметов 8 класса
keyboard_8kl = {
    "one_time": False,
    "buttons": [

     [get_button(label="Алгебра-8", color="primary"),
     get_button(label="Англ.яз-8", color="primary")],
     [get_button(label="Биология-8", color="primary"),
     get_button(label="Геометрия-8", color="primary")],
     [get_button(label="Информатика-8", color="primary"),
     get_button(label="История-8", color="primary")],
     [get_button(label="Обществознание-8", color="primary"),
     get_button(label="Русский язык-8", color="primary")],
     [get_button(label="Физика-8", color="primary"),
      get_button(label="Химия-8", color="primary")],
     [get_button(label="Вернуться к выбору класса⬅", color="negative"),
      get_button(label="Администратор👨‍💻", color="default")]


    ]
}
# Список предметов 7 класса
keyboard_7kl = {
    "one_time": False,
    "buttons": [

      [get_button(label="Алгебра-7", color="primary"),
       get_button(label="Англ.яз-7", color="primary")],
       [get_button(label="Биология-7", color="primary"),
       get_button(label="Геометрия-7", color="primary")],
      [get_button(label="География-7", color="primary"),
       get_button(label="История-7", color="primary")],
       [get_button(label="Информатика-7", color="primary")],
     [get_button(label="Русский язык-7", color="primary"),
      get_button(label="Физика-7", color="primary")],
     [get_button(label="Вернуться к выбору класса⬅", color="negative"),
      get_button(label="Администратор👨‍💻", color="default")]


    ]
}


# Список предметов 6 класса
keyboard_6kl = {
    "one_time": False,
    "buttons": [
    [get_button(label="Англ.яз-6", color="primary"),
     get_button(label="Математика-6", color="primary")],
     [get_button(label="История-6", color="primary"),
     get_button(label="Русс.яз-6", color="primary")],
    [get_button(label="Вернуться к выбору класса⬅", color="negative"),
    get_button(label="Администратор👨‍💻", color="default")]


    ]
}
# Список предметов 5 класса
keyboard_5kl = {
    "one_time": False,
    "buttons": [
    [get_button(label="Англ.яз-5", color="primary"),
     get_button(label="Математика-5", color="primary")],
     [get_button(label="Биология-5", color="primary"),
     get_button(label="История-5", color="primary")],
     [get_button(label="Русс.яз-5", color="primary")],
    [get_button(label="Вернуться к выбору класса⬅", color="negative"),
    get_button(label="Администратор👨‍💻", color="default")]


    ]
}

# Предметы 10 класса
keyboard_math_10 = {
    "one_time": False,
    "buttons": [
    [get_button(label="Учебник; Мордкович, Денищева", color="positive")],
    [get_button(label="Сменить предмет-10", color="negative"),
    get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]
    ]
}

keyboard_English_10 = {
    "one_time": False,
    "buttons": [

     [get_button(label='Starlight : Students book', color="positive")],
     [get_button(label="Сменить предмет-10", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
     [get_button(label="Оставить отзыв📝", color="default")]
    ]
}

keyboard_geo_10 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Холина", color="positive")],
     [get_button(label="Сменить предмет-10", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}






# Предметы 5 класса
keyboard_math_5 = {
    "one_time": False,
    "buttons": [
    [get_button(label="Мерзляк,Полонский,Якир;Дрофа", color="positive")],
    [get_button(label="Учебник; Виленкин, Жохов;", color="positive")],
    [get_button(label="Учебник; С.М. Никольский, М.К. Потапов", color="positive")],
    [get_button(label="Р.Т : И.В. Ященко,Г.И. Вольфсон.", color="positive")],
    [get_button(label="Учебник;Зубарева,Мордкович.", color="positive")],
    [get_button(label="Сменить предмет-5", color="negative"),
    get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]
    ]
}

keyboard_English_5 = {
    "one_time": False,
    "buttons": [

     [get_button(label='Spotlight:Students book', color="positive")],
     [get_button(label='Starlight:Students book', color="positive")],
     [get_button(label='Учебник : Л. М. Лапицкая;А. И. Калишевич', color="positive")],
     [get_button(label="Сменить предмет-5", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
     [get_button(label="Оставить отзыв📝", color="default")]
    ]
}

keyboard_bio_5 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Рабочая тетрадь:Сонин", color="positive")],
     [get_button(label="Рабочая тетрадь:Бодрова", color="positive")],
     [get_button(label="Сменить предмет-5", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
     [get_button(label="Оставить отзыв📝", color="default")]
    ]
}

keyboard_Russian_5 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник;часть 1, 2 Ладыженская", color="positive")],
     [get_button(label="Учебник;Шмелёва", color="positive")],
    [get_button(label="Сменить предмет-5", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]
    ]
}

keyboard_Historic_5 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Рабочая тетрадь; Древний мир", color="positive")],
    [get_button(label="Сменить предмет-5", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}



# Предметы 7 класс
keyboard_math_7 = {
    "one_time": False,
    "buttons": [
    [get_button(label="Учебник; Мерзляк, Полонский, Якир;", color="positive")],
    [get_button(label="Учебник; Г.В.Дорофеев С.Б.Суворова", color="positive")],
    [get_button(label="Учебник; Г. К. Муравин, К. С. Муравин", color="positive")],
    [get_button(label="Учебник; Колягин, Ткачева", color="positive"),
     get_button(label="Учебник; Мордкович А.Г..", color="positive")],
     [get_button(label="Сменить предмет-7", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_English_7 = {
    "one_time": False,
    "buttons": [

     [get_button(label='Starlight; Student"s book;', color="positive")],
     [get_button(label='Starlight; Work book;', color="positive")],
     [get_button(label='Учебник Rainbow english;', color="positive")],
     [get_button(label='Spotlight : student"s book.', color="positive")],
     [get_button(label="Сменить предмет-7", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
     [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_bio_7 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Р.Т; Захаров, Сонин Дрофа", color="positive")],
     [get_button(label="Сменить предмет-7", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
[get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_geo_7 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Душина И.В.", color="positive")],
     [get_button(label="Сменить предмет-7", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_geom_7 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Л.С.Атанасян", color="positive")],
     #[get_button(label="Р.Т. Л.С.Атанасян", color="positive")],
     [get_button(label="Сменить предмет-7", color="negative"),
    get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_physics_7 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Важеевская Н.Е.; Пурышева Н.С.;", color="positive")],
     [get_button(label="Учебник: Перышкин А.В.", color="positive")],
     [get_button(label="Сменить предмет-7", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_Raz_Historic_7 = {
    "one_time": False,
    "buttons": [

     [get_button(label="История России-7", color="primary")],
     [get_button(label="История Нового времени-7", color="primary")],
     [get_button(label="Сменить предмет-7", color="negative")],
    ]
}

keyboard_Russ_Historic_7 = {
    "one_time": False,
    "buttons": [
     [get_button(label="Р.Т; Данилов, Косулина", color="positive")],
     [get_button(label="Учебник; 1,2части; Арсентьев; Данилов;", color="positive")],
        [get_button(label="Сменить раздел-7", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]
    ]
}

keyboard_New_Time_Historic_7 = {
    "one_time": False,
    "buttons": [
     [get_button(label="Р.Т; ч1 и 2 Юдовская, Ванюшкина", color="positive")],
        [get_button(label="Сменить раздел-7", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]
    ]
}

keyboard_Russian_7 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Баранов, Ладыженская", color="positive")],
     [get_button(label="Учебник; Разумовская", color="positive")],
    [get_button(label="Сменить предмет-7", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_IT_7 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Р.Т; Л.Л.Босова", color="positive")],
    [get_button(label="Сменить предмет-7", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}






# Предметы 6 класса
keyboard_English_6 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Starlight st.book", color="positive")],
     [get_button(label="Starlight T.Booklet", color="positive")],
    [get_button(label="Учебник; Комарова Ю.А.", color="positive")],
    [get_button(label="Enjoy English : Биболетова", color="positive")],
    [get_button(label="Учебник : Афанасьева О.В.,Михеева И.В.", color="positive")],
     [get_button(label="Сменить предмет-6", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
     [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_math_6 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Мерзляк А.Г; Полонский В.Б.", color="positive"),
     get_button(label="Учебник; Никольский С.М.", color="positive")],
     [get_button(label="Учебник : Виленкин Н.Я.", color="positive"),
    get_button(label="Учебник : Зубарева, Мордкович", color="positive")],
     [get_button(label="Учебник : Г.В.Дорофеев,И.Ф.Шарыгин", color="positive")],
     [get_button(label="Учебник : Г.В.Дорофеев,Л. Г. Петерсон", color="positive")],
     [get_button(label="Учебник : Истомина", color="positive")],
     [get_button(label="Сменить предмет-6", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_Historic_6 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник;Н.М. Арсеньтьев;1 и 2ч.", color="positive")],
     [get_button(label="Р.Т.; И.А.Артасов; А.А.Данилов", color="positive")],
    [get_button(label="Сменить предмет-6", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_Russian_6 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Ладыженская; 1 и 2 ч.", color="positive"),
    get_button(label="Учебник; Быстрова, кибирева;", color="positive")],
    [get_button(label="Учебник; А.Д. Шмелёв, Э.А. Флоренская", color="positive")],
    [get_button(label="Учебник; Львова, Львов", color="positive")],
    [get_button(label="Р.Т.; Е.А.Ефремова", color="positive"),
    get_button(label="Р.Т.; Г.А.Богданова", color="positive")],
    [get_button(label="Сменить предмет-6", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}






# Клавиатуры предметов 9 класса
# Алгебра
keyboard_math_9 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Мерзляк А.Г ; Поляков В.М", color="positive")],
     [get_button(label="Мерзляк А.Г ; Полонский В.Б ; Якир М.С", color="positive")],
     [get_button(label="Ю.Н. Макарычев, Н.Г. Миндюк, К.И. Нешков", color="positive")],
     [get_button(label="Сменить предмет-9", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}
# Биология
keyboard_bio_9 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Р.Т к учебнику С.Г Мамонтов; Сонин ", color="positive")],
     [get_button(label="Сменить предмет-9", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

# Геометрия
keyboard_geom_9 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Л.С.Атанасян", color="positive")],
     [get_button(label="Р.Т. Л.С.Атанасян", color="positive")],
     [get_button(label="Сменить предмет-9", color="negative"),
    get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

# Информатика
keyboard_IT_9 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Л.Л.Босова", color="positive")],
    [get_button(label="Сменить предмет-9", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}
# Физика
keyboard_physics_9 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Пурышева Н.С.; Важевская Н.Е.", color="positive")],
        [get_button(label="Сменить предмет-9", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}
# Химия
keyboard_chemistry_9 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Г.Е. Рудзитис; Ф.Г. Фельдман", color="positive")],
    [get_button(label="Сменить предмет-9", color="negative"),
    get_button(label="Добавить учебник📚", color="primary")],
     [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_English_9 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник : Enjoy English", color="positive")],
     [get_button(label="ГИА-2014 : Е.А.Фоменко;", color="positive")],
     [get_button(label="ОГЭ-2017 : К.А.Громова; О.В.Вострикова", color="positive")],
     [get_button(label="Сменить предмет-9", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
     [get_button(label="Оставить отзыв📝", color="default")]


    ]
}











# Клавиатуры предметов 8 класса
keyboard_math_8 ={
"one_time": False,
    "buttons": [

     [get_button(label=" Мерзляк, Полонский, Якир ", color="positive")],
     [get_button(label="Дидакт.материалы; Мерзляк, Полонский", color="positive")],
     [get_button(label="Учебник : Г.В.Дорофеева,С.Б.Суворов.", color="positive")],
      [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_bio_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Р.Т Сонин, Агафонова Дрофа", color="positive")],
    [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_geom_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Атанасян; Просвещение", color="positive")],
     [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}
keyboard_IT_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Л.Л. Босова учебник", color="positive")],
     [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_Historic_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Р.Т. Нового времени часть 1, 2 Юдовская", color="positive")],
        [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_Raz_Historic_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="История России-8", color="primary")],
     [get_button(label="История Нового времени-8", color="primary")],
     [get_button(label="Сменить предмет-8", color="negative")],
    ]
}

keyboard_Russ_Historic_8 = {
    "one_time": False,
    "buttons": [
     [get_button(label="Р.Т. Артасов, Данилов, Косулина", color="positive")],
        [get_button(label="Сменить раздел-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_New_Time_Historic_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Р.Т.часть 1, 2 Юдовская", color="positive")],
    [get_button(label="Сменить раздел-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_obchestvo_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Л.Н.Боголюбов, А.Ю.Лазебникова", color="positive")],
        [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_physics_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Пурышева Н.С.", color="positive")],
     [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_Russian_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Ладыженская, Тростенцова.", color="positive")],
     [get_button(label="Учебник: Разумовская М.М.", color="positive")],
    [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_chemistry_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Учебник; Рудзитис, Фельдман", color="positive")],
     [get_button(label="Учебник; Габриелян О.С.", color="positive")],
    [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
    [get_button(label="Оставить отзыв📝", color="default")]


    ]
}

keyboard_English_8 = {
    "one_time": False,
    "buttons": [

     [get_button(label="Starlight students book", color="positive")],
     [get_button(label="Сменить предмет-8", color="negative"),
     get_button(label="Добавить учебник📚", color="primary")],
     [get_button(label="Оставить отзыв📝", color="default")]


    ]
}











conver = ['Начать', 'update', 'Update', 'Добавить учебник📚','update2','Администратор👨‍💻','Оставить отзыв📝', 'Назад', 'Разработчик👨‍💻']

clas = ['5️⃣ Класс', '6️⃣ Класс', '7️⃣ Класс', '8️⃣ Класс', '9️⃣ Класс', '🔟 Класс']

But_9kl = ['Алгебра-9', 'Биология-9', 'Геометрия-9', 'Информатика-9', 'Физика-9', 'Химия-9', 'Вернуться к выбору класса⬅', 'Сменить предмет-9', 'Англ.яз-9']
But_8kl = ['Алгебра-8', 'Англ.яз-8', 'Биология-8', 'Геометрия-8', 'Информатика-8', 'История-8', 'Обществознание-8', 'Русский язык-8','Физика-8', 'Химия-8', 'В главное меню', 'Сменить предмет-8', 'История России-8', 'История Нового времени-8', 'Сменить раздел-8']
But_6kl = ['Англ.яз-6', 'Математика-6', 'История-6', 'Русс.яз-6', 'В главное меню', 'Сменить предмет-6']
But_7kl = ['Сменить предмет-7', 'Алгебра-7', 'Биология-7', 'Геометрия-7', 'География-7', 'История-7', 'Физика-7', 'Англ.яз-7', 'Сменить раздел-7', 'История России-7', 'История Нового времени-7', 'Русский язык-7', 'Информатика-7']
But_5kl = ['Математика-5', 'Англ.яз-5', 'Биология-5', 'История-5', 'Русс.яз-5', 'Сменить предмет-5']
But_10kl = ['Сменить предмет-10', 'Англ.яз-10', 'Алгебра-10', 'География-10']

author_9 = ['Мерзляк А.Г ; Поляков В.М', 'Мерзляк А.Г ; Полонский В.Б ; Якир М.С', 'Р.Т к учебнику С.Г Мамонтов; Сонин', 'Учебник; Л.С.Атанасян', 'Р.Т. Л.С.Атанасян', 'Учебник; Л.Л.Босова', 'Учебник; Пурышева Н.С.; Важевская Н.Е.', 'Учебник; Г.Е. Рудзитис; Ф.Г. Фельдман', 'Ю.Н. Макарычев, Н.Г. Миндюк, К.И. Нешков', 'Учебник : Enjoy English', 'ГИА-2014 : Е.А.Фоменко;', 'ОГЭ-2017 : К.А.Громова; О.В.Вострикова']
author_8 = ['Мерзляк, Полонский, Якир', 'Р.Т Сонин, Агафонова Дрофа', 'Дидакт.материалы; Мерзляк, Полонский', 'Атанасян; Просвещение', 'Л.Л. Босова учебник', 'Р.Т.часть 1, 2 Юдовская', 'Учебник; Л.Н.Боголюбов, А.Ю.Лазебникова', 'Учебник; Пурышева Н.С.', 'Учебник; Ладыженская, Тростенцова.', 'Учебник; Рудзитис, Фельдман', 'Starlight students book', 'Р.Т. Артасов, Данилов, Косулина', 'Учебник: Разумовская М.М.', 'Учебник : Г.В.Дорофеева,С.Б.Суворов.', 'Учебник; Габриелян О.С.']
author_6 = ['Starlight st.book', 'Starlight T.Booklet', 'Мерзляк А.Г; Полонский В.Б.', 'Учебник;Н.М. Арсеньтьев;1 и 2ч.', 'Р.Т.; И.А.Артасов; А.А.Данилов', 'Учебник; Ладыженская; 1 и 2 ч.', 'Р.Т.; Е.А.Ефремова', 'Учебник; Никольский С.М.', 'Учебник; Комарова Ю.А.', 'Учебник : Виленкин Н.Я.', 'Учебник; А.Д. Шмелёв, Э.А. Флоренская', 'Учебник; Быстрова, кибирева;', 'Учебник : Г.В.Дорофеев,И.Ф.Шарыгин', 'Р.Т.; Г.А.Богданова', 'Enjoy English : Биболетова', 'Учебник : Зубарева, Мордкович','Учебник : Г.В.Дорофеев,Л. Г. Петерсон', 'Учебник : Афанасьева О.В.,Михеева И.В.', 'Учебник; Львова, Львов', 'Учебник : Истомина']
author_7 = ['Учебник; Баранов, Ладыженская', 'Учебник; Мерзляк, Полонский, Якир;', 'Учебник; Душина И.В.', 'Р.Т; Данилов, Косулина', 'Р.Т; ч1 и 2 Юдовская, Ванюшкина', 'Учебник; Важеевская Н.Е.; Пурышева Н.С.;', 'Р.Т; Захаров, Сонин Дрофа', 'Starlight; Student"s book;', 'Starlight; Work book;', 'Учебник; 1,2части; Арсентьев; Данилов;', 'Учебник; Г.В.Дорофеев С.Б.Суворова', 'Учебник Rainbow english;', 'Учебник; Г. К. Муравин, К. С. Муравин', 'Учебник; Разумовская', 'Учебник: Перышкин А.В.', 'Spotlight : student"s book.', 'Р.Т; Л.Л.Босова', 'Учебник; Колягин, Ткачева', 'Учебник; Мордкович А.Г..']
author_5 = ['Мерзляк,Полонский,Якир;Дрофа', 'Учебник; Виленкин, Жохов;', 'Spotlight:Students book', 'Starlight:Students book', 'Рабочая тетрадь:Сонин', 'Рабочая тетрадь; Древний мир', 'Учебник;часть 1, 2 Ладыженская', 'Учебник; С.М. Никольский, М.К. Потапов', 'Учебник : Л. М. Лапицкая;А. И. Калишевич', 'Учебник;Шмелёва', 'Р.Т : И.В. Ященко,Г.И. Вольфсон.', 'Рабочая тетрадь:Бодрова', 'Учебник;Зубарева,Мордкович.']
author_10 = ['Starlight : Students book', 'Учебник; Мордкович, Денищева', 'Учебник; Холина']





keyboard = json.dumps(keyboard,  ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

keyboard_instruction = json.dumps(keyboard_instruction,  ensure_ascii=False).encode('utf-8')
keyboard_instruction = str(keyboard_instruction.decode('utf-8'))

keyboard_back = json.dumps(keyboard_back,  ensure_ascii=False).encode('utf-8')
keyboard_back = str(keyboard_back.decode('utf-8'))

keyboard_9kl = json.dumps(keyboard_9kl,  ensure_ascii=False).encode('utf-8')
keyboard_9kl = str(keyboard_9kl.decode('utf-8'))

keyboard_8kl = json.dumps(keyboard_8kl,  ensure_ascii=False).encode('utf-8')
keyboard_8kl = str(keyboard_8kl.decode('utf-8'))

keyboard_7kl = json.dumps(keyboard_7kl,  ensure_ascii=False).encode('utf-8')
keyboard_7kl = str(keyboard_7kl.decode('utf-8'))

keyboard_6kl = json.dumps(keyboard_6kl,  ensure_ascii=False).encode('utf-8')
keyboard_6kl = str(keyboard_6kl.decode('utf-8'))

keyboard_5kl = json.dumps(keyboard_5kl,  ensure_ascii=False).encode('utf-8')
keyboard_5kl = str(keyboard_5kl.decode('utf-8'))

keyboard_10kl = json.dumps(keyboard_10kl,  ensure_ascii=False).encode('utf-8')
keyboard_10kl = str(keyboard_10kl.decode('utf-8'))




# Объявление клавиатур предметов 9 класса
keyboard_math_9 = json.dumps(keyboard_math_9,  ensure_ascii=False).encode('utf-8')
keyboard_math_9 = str(keyboard_math_9.decode('utf-8'))

keyboard_bio_9 = json.dumps(keyboard_bio_9,  ensure_ascii=False).encode('utf-8')
keyboard_bio_9 = str(keyboard_bio_9.decode('utf-8'))

keyboard_geom_9 = json.dumps(keyboard_geom_9,  ensure_ascii=False).encode('utf-8')
keyboard_geom_9 = str(keyboard_geom_9.decode('utf-8'))

keyboard_IT_9 = json.dumps(keyboard_IT_9,  ensure_ascii=False).encode('utf-8')
keyboard_IT_9 = str(keyboard_IT_9.decode('utf-8'))

keyboard_physics_9 = json.dumps(keyboard_physics_9,  ensure_ascii=False).encode('utf-8')
keyboard_physics_9 = str(keyboard_physics_9.decode('utf-8'))

keyboard_chemistry_9 = json.dumps(keyboard_chemistry_9,  ensure_ascii=False).encode('utf-8')
keyboard_chemistry_9 = str(keyboard_chemistry_9.decode('utf-8'))

keyboard_English_9 = json.dumps(keyboard_English_9,  ensure_ascii=False).encode('utf-8')
keyboard_English_9 = str(keyboard_English_9.decode('utf-8'))




# Объявление клавиатур предметов 8 класса
keyboard_math_8 = json.dumps(keyboard_math_8,  ensure_ascii=False).encode('utf-8')
keyboard_math_8 = str(keyboard_math_8.decode('utf-8'))

keyboard_geom_8 = json.dumps(keyboard_geom_8,  ensure_ascii=False).encode('utf-8')
keyboard_geom_8 = str(keyboard_geom_8.decode('utf-8'))

keyboard_bio_8 = json.dumps(keyboard_bio_8,  ensure_ascii=False).encode('utf-8')
keyboard_bio_8 = str(keyboard_bio_8.decode('utf-8'))

keyboard_IT_8 = json.dumps(keyboard_IT_8,  ensure_ascii=False).encode('utf-8')
keyboard_IT_8 = str(keyboard_IT_8.decode('utf-8'))

keyboard_Historic_8 = json.dumps(keyboard_Historic_8,  ensure_ascii=False).encode('utf-8')
keyboard_Historic_8 = str(keyboard_Historic_8.decode('utf-8'))

keyboard_Russ_Historic_8 = json.dumps(keyboard_Russ_Historic_8,  ensure_ascii=False).encode('utf-8')
keyboard_Russ_Historic_8 = str(keyboard_Russ_Historic_8.decode('utf-8'))

keyboard_Raz_Historic_8 = json.dumps(keyboard_Raz_Historic_8,  ensure_ascii=False).encode('utf-8')
keyboard_Raz_Historic_8 = str(keyboard_Raz_Historic_8.decode('utf-8'))

keyboard_New_Time_Historic_8 = json.dumps(keyboard_New_Time_Historic_8,  ensure_ascii=False).encode('utf-8')
keyboard_New_Time_Historic_8 = str(keyboard_New_Time_Historic_8.decode('utf-8'))

keyboard_obchestvo_8 = json.dumps(keyboard_obchestvo_8,  ensure_ascii=False).encode('utf-8')
keyboard_obchestvo_8 = str(keyboard_obchestvo_8.decode('utf-8'))

keyboard_physics_8 = json.dumps(keyboard_physics_8,  ensure_ascii=False).encode('utf-8')
keyboard_physics_8 = str(keyboard_physics_8.decode('utf-8'))

keyboard_Russian_8 = json.dumps(keyboard_Russian_8,  ensure_ascii=False).encode('utf-8')
keyboard_Russian_8 = str(keyboard_Russian_8.decode('utf-8'))

keyboard_chemistry_8 = json.dumps(keyboard_chemistry_8,  ensure_ascii=False).encode('utf-8')
keyboard_chemistry_8 = str(keyboard_chemistry_8.decode('utf-8'))

keyboard_English_8 = json.dumps(keyboard_English_8,  ensure_ascii=False).encode('utf-8')
keyboard_English_8 = str(keyboard_English_8.decode('utf-8'))


# Объявление клавиатур предметов 6 класса
keyboard_English_6 = json.dumps(keyboard_English_6,  ensure_ascii=False).encode('utf-8')
keyboard_English_6 = str(keyboard_English_6.decode('utf-8'))

keyboard_math_6 = json.dumps(keyboard_math_6,  ensure_ascii=False).encode('utf-8')
keyboard_math_6 = str(keyboard_math_6.decode('utf-8'))

keyboard_Historic_6 = json.dumps(keyboard_Historic_6,  ensure_ascii=False).encode('utf-8')
keyboard_Historic_6 = str(keyboard_Historic_6.decode('utf-8'))

keyboard_Russian_6 = json.dumps(keyboard_Russian_6,  ensure_ascii=False).encode('utf-8')
keyboard_Russian_6 = str(keyboard_Russian_6.decode('utf-8'))





# объявление клавиатур 7 класса
keyboard_math_7 = json.dumps(keyboard_math_7,  ensure_ascii=False).encode('utf-8')
keyboard_math_7 = str(keyboard_math_7.decode('utf-8'))

keyboard_geom_7 = json.dumps(keyboard_geom_7,  ensure_ascii=False).encode('utf-8')
keyboard_geom_7 = str(keyboard_geom_7.decode('utf-8'))

keyboard_bio_7 = json.dumps(keyboard_bio_7,  ensure_ascii=False).encode('utf-8')
keyboard_bio_7 = str(keyboard_bio_7.decode('utf-8'))

keyboard_English_7 = json.dumps(keyboard_English_7,  ensure_ascii=False).encode('utf-8')
keyboard_English_7 = str(keyboard_English_7.decode('utf-8'))

keyboard_physics_7 = json.dumps(keyboard_physics_7,  ensure_ascii=False).encode('utf-8')
keyboard_physics_7 = str(keyboard_physics_7.decode('utf-8'))

keyboard_geo_7 = json.dumps(keyboard_geo_7,  ensure_ascii=False).encode('utf-8')
keyboard_geo_7 = str(keyboard_geo_7.decode('utf-8'))

keyboard_Russ_Historic_7 = json.dumps(keyboard_Russ_Historic_7,  ensure_ascii=False).encode('utf-8')
keyboard_Russ_Historic_7 = str(keyboard_Russ_Historic_7.decode('utf-8'))

keyboard_Raz_Historic_7 = json.dumps(keyboard_Raz_Historic_7,  ensure_ascii=False).encode('utf-8')
keyboard_Raz_Historic_7 = str(keyboard_Raz_Historic_7.decode('utf-8'))

keyboard_New_Time_Historic_7 = json.dumps(keyboard_New_Time_Historic_7,  ensure_ascii=False).encode('utf-8')
keyboard_New_Time_Historic_7 = str(keyboard_New_Time_Historic_7.decode('utf-8'))

keyboard_Russian_7 = json.dumps(keyboard_Russian_7,  ensure_ascii=False).encode('utf-8')
keyboard_Russian_7 = str(keyboard_Russian_7.decode('utf-8'))

keyboard_IT_7 = json.dumps(keyboard_IT_7,  ensure_ascii=False).encode('utf-8')
keyboard_IT_7 = str(keyboard_IT_7.decode('utf-8'))

# Объявление клавиатур 5 класса
keyboard_math_5 = json.dumps(keyboard_math_5,  ensure_ascii=False).encode('utf-8')
keyboard_math_5 = str(keyboard_math_5.decode('utf-8'))

keyboard_bio_5 = json.dumps(keyboard_bio_5,  ensure_ascii=False).encode('utf-8')
keyboard_bio_5 = str(keyboard_bio_5.decode('utf-8'))

keyboard_English_5 = json.dumps(keyboard_English_5,  ensure_ascii=False).encode('utf-8')
keyboard_English_5 = str(keyboard_English_5.decode('utf-8'))

keyboard_Russian_5 = json.dumps(keyboard_Russian_5,  ensure_ascii=False).encode('utf-8')
keyboard_Russian_5 = str(keyboard_Russian_5.decode('utf-8'))

keyboard_Historic_5 = json.dumps(keyboard_Historic_5,  ensure_ascii=False).encode('utf-8')
keyboard_Historic_5 = str(keyboard_Historic_5.decode('utf-8'))

# Объявление клавиатур 10 класса
keyboard_English_10 = json.dumps(keyboard_English_10,  ensure_ascii=False).encode('utf-8')
keyboard_English_10 = str(keyboard_English_10.decode('utf-8'))

keyboard_math_10 = json.dumps(keyboard_math_10,  ensure_ascii=False).encode('utf-8')
keyboard_math_10 = str(keyboard_math_10.decode('utf-8'))

keyboard_geo_10 = json.dumps(keyboard_geo_10,  ensure_ascii=False).encode('utf-8')
keyboard_geo_10 = str(keyboard_geo_10.decode('utf-8'))

















while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            message = messages["items"][0]["last_message"]["text"]


            if message == conver[0]:
                vk.method("messages.send", {"peer_id": id, "message": "Привет,я Gdz Бот.🤖 \nЯ помогу тебе найти бесплатное гдз.🔎\nБудет что-то непонятно напиши мне 'Инструкция'.\nДля начала выбери класс на специальной клавиатуре👇", "keyboard": keyboard, "random_id": get_random_id()})
                vk.method("messages.send", {"peer_id": id, "message": "Также я тебе советую подписаться на меня, что бы не пропускать обновления❗🔄\n👉https://vk.com/gdz_bot_ulsk","random_id": get_random_id()})


            #Обновление клавиатур
            elif message == conver[1]:vk.method("messages.send", {"peer_id": id, 'message': 'Выбери класс нажав на кнопку ниже👇🎛', "keyboard": keyboard,  "random_id": get_random_id()})
            elif message == conver[2]:vk.method("messages.send", {"peer_id": id, 'message': 'Выбери класс нажав на кнопку ниже👇🎛', "keyboard": keyboard, "random_id": get_random_id()})
            elif message == conver[4]:vk.method("messages.send", {"peer_id": id, 'message': 'Клавиатура обновлена', "keyboard": keyboard_8kl, "random_id": get_random_id()})
            # Кнопка администратор
            elif message == conver[5]:vk.method("messages.send", {"peer_id": id, 'message': 'Администратор👨‍💻 \nhttps://vk.com/id405770357', "random_id": get_random_id()})
            # Оставить отзыв
            elif message == conver[6]:vk.method("messages.send", {"peer_id": id, 'message': 'Понравилась работа бота❓🔥\nОставь нам отзыв✍📝\nили предложения\n👉https://vk.com/gdz_bot_ulsk?w=app6326142_-175414149',"random_id": get_random_id()})



            # Кнопка добавить учебник
            elif message == conver[3]:vk.method("messages.send", {"peer_id": id, 'message': 'Заполни анкету📝 \nна добавление учебника перейдя по этой ссылке!\nИ уже через 24 часа у нас появится этот учебник📓\n👉https://vk.com/gdz_bot_ulsk?w=app5708398_-175414149', "random_id": get_random_id()})

            # Инструкция
            elif message == 'Инструкция':vk.method("messages.send", {"peer_id": id, 'message': 'Я - твой помощник по поиску бесплатного ГДЗ❗\n \nРазработал меня @id405770357\n \nЕсли нет нужного тебе автора или предмета в меню, значит, разработчик его ещё не добавил, но обязательно добавит!\nТы можешь это ускорить, нажав на кнопку "Добавить учебник".\n \nВ непонятной тебе ситуации напиши мне "Update".\n \nЕсли меню исчезнет, то нажми на значок квадратика с точками внутри.🎛 \nТакже для отображения меню у тебя должна быть последняя версия официального приложения ВК.\n \nЕсли захочешь поменять предмет, нажми на кнопку “сменить предмет“.\nЕсли захочешь сменить класс, нажми на кнопу “Вернуться к выбору класса“.\n \nТакже ты всегда можешь оставить нам отзыв или предложения✍\n👉https://vk.com/gdz_bot_ulsk?w=app6326142_-175414149\nБлагодаря вашим отзывам и предложениям мы стремимся делать работу бота более качественной и понятной для пользователей.🤗 ', "keyboard": keyboard_back, "random_id": get_random_id()})
            elif message == 'инструкция':vk.method("messages.send", {"peer_id": id, 'message': 'Я - твой помощник по поиску бесплатного ГДЗ❗\n \nРазработал меня @id405770357\n \nЕсли нет нужного тебе автора или предмета в меню, значит, разработчик его ещё не добавил, но обязательно добавит!\nТы можешь это ускорить, нажав на кнопку "Добавить учебник".\n \nВ непонятной тебе ситуации напиши мне "Update".\n \nЕсли меню исчезнет, то нажми на значок квадратика с точками внутри.🎛 \nТакже для отображения меню у тебя должна быть последняя версия официального приложения ВК.\n \nЕсли захочешь поменять предмет, нажми на кнопку “сменить предмет“.\nЕсли захочешь сменить класс, нажми на кнопу “Вернуться к выбору класса“.\n \nТакже ты всегда можешь оставить нам отзыв или предложения✍\n👉https://vk.com/gdz_bot_ulsk?w=app6326142_-175414149\nБлагодаря вашим отзывам и предложениям мы стремимся делать работу бота более качественной и понятной для пользователей.🤗 ', "keyboard": keyboard_back,"random_id": get_random_id()})

            elif message == conver[7]:vk.method("messages.send", {"peer_id": id,'message': 'Выбери то что нужно', "keyboard": keyboard_instruction, "random_id": get_random_id()})
            elif message == conver[8]:vk.method("messages.send", {"peer_id": id,'message': 'По различным вопросам\n👉 @id405770357', "keyboard": keyboard_back, "random_id": get_random_id()})




            # Если перешли по кнопке 5, 6, 7, 8, 9 класс
            elif message == clas[4]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_9kl, "random_id": get_random_id()})
            elif message == clas[3]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_8kl, "random_id": get_random_id()})
            elif message == clas[1]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_6kl, "random_id": get_random_id()})
            elif message == clas[2]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_7kl, "random_id": get_random_id()})
            elif message == clas[0]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_5kl, "random_id": get_random_id()})
            elif message == clas[5]: vk.method("messages.send", {"peer_id": id, 'message': 'Раздел находится в разработке', "keyboard": keyboard, "random_id": get_random_id()})

            # Кнопка возвращающая пользователя на экран "выбор класса"
            elif message == But_9kl[6]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери класс👇', "keyboard": keyboard, "random_id": get_random_id()})

            # Сменить предмет 5, 6, 7, 8,9
            elif message == But_9kl[7]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_9kl, "random_id": get_random_id()})
            elif message == But_8kl[11]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_8kl, "random_id": get_random_id()})
            elif message == But_6kl[5]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_6kl, "random_id": get_random_id()})
            elif message == But_7kl[0]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_7kl, "random_id": get_random_id()})
            elif message == But_5kl[5]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_5kl, "random_id": get_random_id()})
            elif message == But_10kl[0]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя предмет📗👇', "keyboard": keyboard_10kl, "random_id": get_random_id()})
            # сменить раздел истории 8 класс
            elif message == But_8kl[14]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя раздел👇', "keyboard": keyboard_Raz_Historic_8, "random_id": get_random_id()})
            elif message == But_7kl[8]: vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя раздел👇', "keyboard": keyboard_Raz_Historic_7, "random_id": get_random_id()})

            # Переход по кнопкам "Предметы" 9 класс
            elif message == But_9kl[0]: vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_math_9, "random_id": get_random_id()})
            elif message == But_9kl[1]: vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_bio_9, "random_id": get_random_id()})
            elif message == But_9kl[2]: vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_geom_9, "random_id": get_random_id()})
            elif message == But_9kl[3]: vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_IT_9, "random_id": get_random_id()})
            elif message == But_9kl[4]: vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_physics_9, "random_id": get_random_id()})
            elif message == But_9kl[5]: vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_chemistry_9, "random_id": get_random_id()})
            elif message == But_9kl[8]: vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_English_9, "random_id": get_random_id()})

            # Переход по кнопкам "Предметы" 8 Класс
            elif message == But_8kl[0]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_math_8, "random_id": get_random_id()})
            elif message == But_8kl[1]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_English_8, "random_id": get_random_id()})
            elif message == But_8kl[2]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_bio_8, "random_id": get_random_id()})
            elif message == But_8kl[3]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_geom_8, "random_id": get_random_id()})
            elif message == But_8kl[4]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_IT_8, "random_id": get_random_id()})
            elif message == But_8kl[5]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужный тебе раздел, нажав на кнопку ниже👇', "keyboard": keyboard_Raz_Historic_8, "random_id": get_random_id()})
            elif message == But_8kl[6]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_obchestvo_8, "random_id": get_random_id()})
            elif message == But_8kl[7]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_Russian_8, "random_id": get_random_id()})
            elif message == But_8kl[8]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_physics_8, "random_id": get_random_id()})
            elif message == But_8kl[9]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_chemistry_8, "random_id": get_random_id()})
            elif message == But_8kl[12]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_Russ_Historic_8, "random_id": get_random_id()})
            elif message == But_8kl[13]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_New_Time_Historic_8, "random_id": get_random_id()})


            # переход по кнопкам 'Предметы ' 6 класс
            elif message == But_6kl[0]:vk.method("messages.send",{"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_English_6, "random_id": get_random_id()})
            elif message == But_6kl[1]:vk.method("messages.send",{"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_math_6, "random_id": get_random_id()})
            elif message == But_6kl[2]:vk.method("messages.send",{"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_Historic_6, "random_id": get_random_id()})
            elif message == But_6kl[3]:vk.method("messages.send",{"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_Russian_6, "random_id": get_random_id()})

            # переход по кнопкам "Предметы" 7 класс
            elif message == But_7kl[1]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_math_7, "random_id": get_random_id()})
            elif message == But_7kl[2]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_bio_7, "random_id": get_random_id()})
            elif message == But_7kl[3]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_geom_7, "random_id": get_random_id()})
            elif message == But_7kl[4]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_geo_7, "random_id": get_random_id()})
            elif message == But_7kl[5]:vk.method("messages.send", {"peer_id": id, 'message': 'Выбери интересующий тебя раздел👇', "keyboard": keyboard_Raz_Historic_7, "random_id": get_random_id()})
            elif message == But_7kl[6]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_physics_7, "random_id": get_random_id()})
            elif message == But_7kl[7]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_English_7, "random_id": get_random_id()})
            elif message == But_7kl[11]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_Russian_7, "random_id": get_random_id()})
            elif message == But_7kl[12]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇', "keyboard": keyboard_IT_7, "random_id": get_random_id()})

            elif message == But_7kl[9]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_Russ_Historic_7, "random_id": get_random_id()})
            elif message == But_7kl[10]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_New_Time_Historic_7, "random_id": get_random_id()})

            # Переход по кнопкам "Предметы" 5 класс
            elif message == But_5kl[0]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_math_5, "random_id": get_random_id()})
            elif message == But_5kl[1]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_English_5, "random_id": get_random_id()})
            elif message == But_5kl[2]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_bio_5, "random_id": get_random_id()})
            elif message == But_5kl[3]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_Historic_5, "random_id": get_random_id()})
            elif message == But_5kl[4]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_Russian_5, "random_id": get_random_id()})

            # Переход по кнопкам "Предметы" 10 класс
            elif message == But_10kl[1]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_English_10, "random_id": get_random_id()})
            elif message == But_10kl[2]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_math_10, "random_id": get_random_id()})
            elif message == But_10kl[3]:vk.method("messages.send", {"peer_id": id, 'message': 'Теперь выбери нужного автора, нажав на кнопку ниже👇',"keyboard": keyboard_geo_10, "random_id": get_random_id()})






            # Алгебра и математика - учебники 5, 6, 7, 8,9 класс
            elif message == author_9[0]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz.ltd/9-class/algebra/Merzljak-uglublennyj-uroven/', "random_id": get_random_id()})
            elif message == author_9[1]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdzplus.ru/9-klass/algebra/merzlyak/', "random_id": get_random_id()})
            elif message == author_8[0]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/algebra/8_klass/reshebnik-po-algebre-8-klass-merzlyak-polonskii-923', "random_id": get_random_id()})
            elif message == author_8[1]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/biologiya/8_klass/rabochaya-tetrad-po-biologii-8-klass-sonin-999', "random_id": get_random_id()})
            elif message == author_8[2]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/algebra/8_klass/didakticheskie-materialy-po-algebre-8-klass-merzlyak-polonskii-598', "random_id": get_random_id()})

            elif message == author_6[2]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/matematika/6_klass/reshebnik-po-matematike-6-klass-fgos-merzlyak-polonskii-131', "random_id": get_random_id()})

            elif message == author_6[7]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz.ru/class-6/matematika/reshebnik-nikolskiy-s-m-2013/', "random_id": get_random_id()})

            elif message == author_7[1]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/algebra/7_klass/reshebnik-merzlyak-polonskii-yakir-89', "random_id": get_random_id()})

            elif message == author_9[8]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://euroki.app/gdz/algebra/9class/makarychev', "random_id": get_random_id()})

            elif message == author_5[0]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/matematika/5_klass/reshebnik-po-matematike-5-klass-fgos-merzlyak-polonskii-676', "random_id": get_random_id()})

            elif message == author_5[1]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/matematika/5_klass/reshebnik-po-matematike-5-klass-vilenkin-fgos-409', "random_id": get_random_id()})

            elif message == author_7[10]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdzotputina.club/7-klass/algebra/dorofeev', "random_id": get_random_id()})

            elif message == author_10[1]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/algebra/10_klass/reshebnik-po-algebre-10-klass-mordkovich-denischeva-fgos-657?utm_source=euroki&utm_campaign=lastbooks', "random_id": get_random_id()})

            elif message == author_7[12]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdzputina.net/7-klass-algebra-muravin-g-k', "random_id": get_random_id()})

            elif message == author_6[9]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz.ru/class-6/matematika/vilenkin-13-23/', "random_id": get_random_id()})

            elif message == author_5[7]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz.ru/class-5/matematika/nikolskiy/', "random_id": get_random_id()})

            elif message == author_6[12]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/matematika/6_klass/reshebnik-po-matematike-6-klass-dorofeev-sharygin-fgos-prosveschenie-630', "random_id": get_random_id()})

            elif message == author_6[15]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/matematika/6_klass/reshebnik-po-matematike-6-klass-zubareva-mordkovich-fgos-899', "random_id": get_random_id()})

            elif message == author_8[13]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/algebra/8_klass/dorofeev-suvorova-717', "random_id": get_random_id()})

            elif message == author_6[16]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz-putina.cc/28-6klass/40-matematika/dorofeev-peterson.html', "random_id": get_random_id()})

            elif message == author_7[17]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/algebra/7_klass/reshebnik-po-algebre-7-klass-kolyagin-tkacheva-fgos-883', "random_id": get_random_id()})
                
            elif message == author_6[19]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttp://reshator.com/6-klass/matematika/istomina/', "random_id": get_random_id()})

            elif message == author_7[18]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz.ru/class-7/algebra/mordkovich-14/', "random_id": get_random_id()})

            elif message == author_5[10]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://znayka.pro/vpr-vserossijskaya-proverochnaya-rabota/5-klass-vpr/vpr-matematika-5-klass-tipovye-zadaniya-25-variantov-otvety-volfson-g-i-manujlov-d-a/', "random_id": get_random_id()})

            elif message == author_5[12]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdzplus.me/5-klass/matematika/zubareva/', "random_id": get_random_id()})


            # Биология рабочие тетради все классы
            elif message == author_9[2]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/biologiya/9_klass/rabochaya-tetrad-po-biologii-9-klass-tsibulevskii-735', "random_id": get_random_id()})

            elif message == author_7[6]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/biologiya/7_klass/rabochaya-tetrad-po-biologii-7-klass-sonin-816', "random_id": get_random_id()})

            elif message == author_5[4]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/biologiya/5_klass/rabochaya_tetrad_po_biologii_n_i_sonin_21', "random_id": get_random_id()})

            elif message == author_5[11]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/biologiya/5_klass/rabochaya-tetrad-po-biologii--5-klass-bodrova-32', "random_id": get_random_id()})

            # география 7 класс
            elif message == author_7[2]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://megaresheba.ru/gdz/geografia/7-klass/dushina-smoktunovich', "random_id": get_random_id()})

            elif message == author_10[2]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://megaresheba.ru/gdz/geografia/7-klass/dushina-smoktunovich', "random_id": get_random_id()})



            # Геометрия общ. учебник 7- 9 классы
            elif message == author_8[3]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/geometriya/8_klass/reshebnik-po-geometrii-8-klass-atanasyan-536', "random_id": get_random_id()})
            elif message == author_9[3]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/geometriya/8_klass/reshebnik-po-geometrii-8-klass-atanasyan-536', "random_id": get_random_id()})
            elif message == author_9[4]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/geometriya/9_klass/rabochaja_tetrad_geometrija', "random_id": get_random_id()})

            # информатика 8, 9 классы
            elif message == author_8[4]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdzotputina.club/8-klass/informatika/bosova',"random_id": get_random_id()})
            elif message == author_9[5]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://5urokov.ru/gdz/bosova_9_uch',"random_id": get_random_id()})

            elif message == author_7[16]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz-putina.cc/50-7klass/59-inphormatika/bosova-fgos-seven.html',"random_id": get_random_id()})


            # История 7,8 класс
            elif message == author_8[5]:vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/istoriya/8_klass/rabochaya-tetrad-po-istorii-8-klass-chast-1-udovskaya-vanushkina_849',"random_id": get_random_id()})
            elif message == author_6[3]:vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz-putina.info/6-klass/istoriya-6/gdz-po-istorii-6-klass-arsentev-danilov-stefanovich-tokareva/',"random_id": get_random_id()})
            elif message == author_6[4]:vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/istoriya/6_klass/rabochaya-tetrad-po-istorii-rossii-6-klass-artasov-fgos-702',"random_id": get_random_id()})
            elif message == author_8[11]:vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/istoriya/8_klass/rabochaya-tetrad-po-istorii-rossii-8-klass-artasov-fgos-663',"random_id": get_random_id()})

            elif message == author_7[4]:vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/istoriya/7_klass/rabochaya_tetrad_po_istorii_7_klass_chast_1_udovskaya_vanushkina_538',"random_id": get_random_id()})
            elif message == author_7[3]:vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/istoriya/7_klass/rabochaya-tetrad-po-istorii-rossii-7-klass-danilov-fgos-761',"random_id": get_random_id()})
            elif message == author_7[9]:vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://yagdz.com/7-klass/istoriya-7/gdz-po-istorii-7-klass-arsentev-danilov-kurukin-tokareva/',"random_id": get_random_id()})
            elif message == author_5[5]:vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/istoriya/5_klass/rabochaya_tetrad_po_istorii_chast_1_goder_850',"random_id": get_random_id()})


            # Обществознание 8 класс
            elif message == author_8[6]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz-putina.info/8-klass/obshhestvoznanie-8/gdz-8-bogolyubova-uchebnik/',"random_id": get_random_id()})

            # Физика 8,9 классы
            elif message == author_8[7]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://shkololo.ru/gdz-fizika/8-klass-purysheva#task', "random_id": get_random_id()})
            elif message == author_9[6]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdzotputina.club/9-klass/fizika/purisheva', "random_id": get_random_id()})

            elif message == author_7[5]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz.ru/class-7/fizika/purisheva-2011/', "random_id": get_random_id()})

            elif message == author_7[14]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz.ru/class-7/fizika/peryshkin-7/', "random_id": get_random_id()})



            # Русский язык 8 класс
            elif message == author_8[8]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://www.euroki.org/gdz/ru/russkiy/8_klass/ladyzhenskaya-786', "random_id": get_random_id()})

            elif message == author_6[5]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://www.euroki.org/gdz/ru/russkiy/6_klass/reshebnik-po-russkomu-yazyku-6-klass-fgos-baranov-ladyzhenskaya-124', "random_id": get_random_id()})

            elif message == author_6[6]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://www.euroki.org/gdz/ru/russkiy/6_klass/rabochaya_tetrad_po_russkomu_yazyku_6_klass_e_a__efremova_402', "random_id": get_random_id()})

            elif message == author_7[0]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://www.euroki.org/gdz/ru/russkiy/7_klass/baranov-278', "random_id": get_random_id()})

            elif message == author_5[6]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://www.euroki.org/gdz/ru/russkiy/5_klass/reshebnik-po-russkomu-yazyku-5-klass-fgos-ladyzhenskaya-baranov-600', "random_id": get_random_id()})

            elif message == author_7[13]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://www.euroki.org/gdz/ru/russkiy/7_klass/reshebnik-po-russkomu-yazyku-7-klass-razumovskaya-fgos-490', "random_id": get_random_id()})

            elif message == author_8[12]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://gdz.ru/class-8/russkii_yazik/razumovskaya-11/', "random_id": get_random_id()})

            elif message == author_6[10]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://gdz-putina.info/6-klass/russkij-yazik-6/gdz-po-russkomu-yazyku-6-klass-shmelyov-florenskaya-savchuk-shmelyova/', "random_id": get_random_id()})

            elif message == author_6[11]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://yagdz.com/6-klass/russkij-yazyk-6/gdz-po-russkomu-yazyku-6-klass-bystrova-1-i-2-chast/', "random_id": get_random_id()})

            elif message == author_6[13]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://gdz-putina.info/6-klass/russkij-yazik-6/gdz-po-russkomu-yazyku-6-klass-rabochaya-tetrad-bogdanova/', "random_id": get_random_id()})

            elif message == author_6[18]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttp://reshator.com/6-klass/russkij-jazik/lvova-lvov/', "random_id": get_random_id()})

            elif message == author_5[9]:
                vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓: \nhttps://yagdz.com/5-klass/russkij-yazyk-5/gdz-po-russkomu-yazyku-5-klass-shmelyova/', "random_id": get_random_id()})

            # Химия 8, 9 классы
            elif message == author_8[14]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://gdz.ru/class-8/himiya/gabrielyan-8/', "random_id": get_random_id()})
            elif message == author_8[9]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/himiya/8_klass/reshebnik-po-himii-8-klass-rudzitis-feldman-fgos-20', "random_id": get_random_id()})
            elif message == author_9[7]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз  🆓: \nhttps://www.euroki.org/gdz/ru/himiya/9_klass/reshebnik-po-himii-9-klass-rudzitis-fgos-616?utm_source=euroki&utm_campaign=lastbooks', "random_id": get_random_id()})


            # Английский язык все классы
            elif message == author_8[10]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://vk.com/doc35399697_437841256?hash=d957a4c79c1c9d0040&dl=1305721d5bfd94326e', "random_id": get_random_id()})
            elif message == author_6[0]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://www.euroki.org/gdz/ru/angliyskiy/6_klass/gdz-po-angliiskomu-7-klass-starlait-students-book-baranova-570?utm_source=euroki&utm_campaign=lastbooks', "random_id": get_random_id()})
            elif message == author_6[1]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://5urokov.ru/load/gdz_6_klass/anglijskij_jazyk/reshebnik_gdz_test_booklet_starlight_6_klass_otvety_k_kontrolnym_zadanijam_baranova_duli/13-1-0-530#', "random_id": get_random_id()})
            elif message == author_6[8]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://gdzhaha.com/gdz/326-anglijskij-yazyk-6-klass-komarov.html', "random_id": get_random_id()})
            elif message == author_7[7]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://www.euroki.org/gdz/ru/angliyskiy/7_klass/gdz-po-angliiskomu-yazyku-7-klass-starlait-baranova-81', "random_id": get_random_id()})
            elif message == author_7[8]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://www.euroki.org/gdz/ru/angliyskiy/7_klass/rabochaya-tetrad-po-angliiskomu-7-klass-starlait-621?utm_source=euroki&utm_campaign=komplekt', "random_id": get_random_id()})
            elif message == author_5[2]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://www.euroki.org/gdz/ru/angliyskiy/5_klass/ju_e_vaulina_spotlight_fgos', "random_id": get_random_id()})
            elif message == author_5[3]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttp://gdzgdz.ru/gdz/gdz-reshebnik-po-anglijskomu-yazyku-za-5-klass-baranova-km-starlight-5-zvezdnyj-anglijskij-5-klass', "random_id": get_random_id()})
            elif message == author_7[11]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttp://reshator.com/7-klass/anglijskij-jazyk/rainbow/', "random_id": get_random_id()})
            elif message == author_10[0]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttp://gdzgdz.ru/gdz/gdz-reshebnik-Starlight-10-zvezdnyj-anglijskij-baranova-km', "random_id": get_random_id()})
            elif message == author_9[9]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://gdz.ru/class-9/english/biboletova/', "random_id": get_random_id()})
            elif message == author_5[8]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://gdzputina.net/5-klass-anglijskij-yazyk-lapickaya', "random_id": get_random_id()})
            elif message == author_7[15]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://www.euroki.org/gdz/ru/angliyskiy/7_klass/e_vaulina_d_duli_v_jevans_o_podoljanko_6_fgos', "random_id": get_random_id()})
            elif message == author_6[14]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://www.euroki.org/gdz/ru/angliyskiy/6_klass/reshebnik-po-angliiskomu-yazyku--6-klass-enjoy-english-biboletova-fgos-664', "random_id": get_random_id()})
            elif message == author_6[17]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://gdzhaha.com/gdz/34-gdz-anglijskij-yazyk-rainbow-english-6-klass-afanaseva.html', "random_id": get_random_id()})

            elif message == author_9[10]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://docviewer.yandex.ru/view/812544447/?*=8QuS2XrsnLwYe8WyX1QV5XZhkLB7InVybCI6Imh0dHA6Ly9zYzJlNTc1MDg2ODhjOWIzYS5qaW1jb250ZW50LmNvbS9kb3dubG9hZC92ZXJzaW9uLzE0MjM0MDAxNjMvbW9kdWxlLzcyMTQ1OTcxNzUvbmFtZS9mb21lbmtvX2VfYV9kb2xnb3BvbHNrYXlhX2lfYl9jaGVybmlrb3ZhX25fdl9hbmdsaWlza2lpX3lhenkucGRmIiwidGl0bGUiOiJmb21lbmtvX2VfYV9kb2xnb3BvbHNrYXlhX2lfYl9jaGVybmlrb3ZhX25fdl9hbmdsaWlza2lpX3lhenkucGRmIiwidWlkIjoiODEyNTQ0NDQ3IiwieXUiOiIxMzk0MTc4OTUxNTQ1NjcwOTY4Iiwibm9pZnJhbWUiOnRydWUsInRzIjoxNTUxODg4NDg1ODQwLCJzZXJwUGFyYW1zIjoibGFuZz1lbiZuYW1lPWZvbWVua29fZV9hX2RvbGdvcG9sc2theWFfaV9iX2NoZXJuaWtvdmFfbl92X2FuZ2xpaXNraWlfeWF6eS5wZGYmdG09MTUzNjkxMTIxNCZ0bGQ9cnUmdGV4dD0lRDElODMlRDElODclRDAlQjUlRDAlQjElRDAlQkQlRDAlQkUlMjAlRDElODIlRDElODAlRDAlQjUlRDAlQkQlRDAlQjglRDElODAlRDAlQkUlRDAlQjIlRDAlQkUlRDElODclRDAlQkQlRDElOEIlRDAlQjUlMjAlRDAlQjIlRDAlQjAlRDElODAlRDAlQjglRDAlQjAlRDAlQkQlRDElODIlRDElOEIlMjAlRDAlQjclRDAlQjAlRDAlQjQlRDAlQjAlRDAlQkQlRDAlQjglRDAlQjklMjAlRDAlQjMlRDAlQkUlRDElODElRDElODMlRDAlQjQlRDAlQjAlRDElODAlRDElODElRDElODIlRDAlQjIlRDAlQjUlRDAlQkQlRDAlQkQlRDAlQkUlRDAlQjklMjAlRDAlQjglRDElODIlRDAlQkUlRDAlQjMlRDAlQkUlRDAlQjIlRDAlQkUlRDAlQjkmdXJsPWh0dHAlM0ElMkYlMkZzYzJlNTc1MDg2ODhjOWIzYS5qaW1jb250ZW50LmNvbSUyRmRvd25sb2FkJTJGdmVyc2lvbiUyRjE0MjM0MDAxNjMlMkZtb2R1bGUlMkY3MjE0NTk3MTc1JTJGbmFtZSUyRmZvbWVua29fZV9hX2RvbGdvcG9sc2theWFfaV9iX2NoZXJuaWtvdmFfbl92X2FuZ2xpaXNraWlfeWF6eS5wZGYmdHlwZT10b3VjaCZscj0xOTUmbWltZT1wZGYmbDEwbj1ydSZzaWduPWZmNDYxMWU0MTcwM2E2NjNmNDBjYjFiNTAxZTdmNWNkJmtleW5vPTAifQ%3D%3D&lang=en', "random_id": get_random_id()})
            elif message == author_9[11]: vk.method("messages.send", {"peer_id": id, 'message': 'Отлично, вот ссылка на бесплатное гдз 🆓 : \nhttps://fileskachat.com/view/41444_b367ada28864d2737e6686d2baaccd42.html', "random_id": get_random_id()})



            else:
                vk.method("messages.send", {"peer_id": id, "message": "Не понимаешь\nкак пользоваться❓\nНажми на кнопку 'Инструкция' и подробно ознакомься с ней.🕵️‍️", "keyboard": keyboard_instruction, "random_id": get_random_id()})

            time.sleep(0.05)


            print('"',message, '"'," от пользователя :", id, ';','Время - ', time.ctime())
            print(' ')



            vk_mess = message
            filename = messages["items"][0]["last_message"]["from_id"]
            file = open('{0}.txt'.format(filename),'a',encoding='utf-8')
            file.write('"' + message + '"' + ' - ' + 'Время : ' + time.ctime() + '\n')
            file.write('\n')
            file.close()



    except Exception as E:
        time.sleep(1)