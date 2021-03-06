BOT_CONFIG = {
    'intents': {
        'new_year': {
            'examples': ['Ждёшь новый год?', 'Что попросил на новый год?', 'Новый год!', 'Ждешь нг?'],
            'responses': ['Look forward to Новый год!', 'Попросил у Морозика) Новые детали Apex', 'А как же без Нг, очень люблю кушать мандаринки!']
        },
        'hello': {
            'examples': ['Привет!', 'Хэллоу', 'Добрый день!!','Хай'],
            'responses': ['Хаю-хай', 'Здравствуйте)', 'Доброе утро!']
        },
        'brawlstars': {
            'examples': ['Играешь в бравл старс','Играешь в бс?','Как относишься к бравл старс?'],
            'responses': ['Онли мортис..)', 'Мама мной гордится, I have Леоооон', 'Основное хобби!)']
        },
        'likemusic': {
            'examples': ['Какая твоя любимая музыка', 'Что посоветуешь послушать?', 'Любимая музыка?'],
            'responses': ['Тут явно Дора!!', 'Как вариант Кизяка..!', 'Лучше Доры вообще ничего не существует)))']
        },
        'anime': {
            'examples': ['Смотришь аниме?', 'Как относишься к аниме?', 'Любимая аниме тянка?'],
            'responses': ['Обожаю Цунаде)', 'Люблю 02..!', 'Смотрю только из-за Цунаде!']
        },
        'opinion': {
            'examples': ['Жаль', 'Печально', 'Грустно','Обидно','Классно','Весело','Скучно','Радостно','Жиза'],
            'responses': ['Полностью согласен!', 'Ага..', 'Солидарен)']
        },
        'color': {
            'examples': ['Какой твой любимый цвет?', 'Какой  цвет выберешь?', 'Любимый цвет?'],
            'responses': ['Фиолетовый', 'Люблю оттенки розового!', 'Абсолютно точно БИРЮЗОВЫЙ))']
        },
        'season': {
            'examples': ['Любимое время года?', 'Какое время года предпочитаешь?'],
            'responses': ['Конечно, лето', 'Обожаю зиму!', 'Точно не весна )']
        },
        'school': {
            'examples': ['Любишь ходить в школу?', 'Как относишься к школе?','Ради чего ходишь в школу?'],
            'responses': ['Хожу онли из-за Грегора))', 'Нужно же еще как-то проводить время..)', 'Отношение к шк точно лучше,чем у многих школотронов!']
        },
        'city': {
            'examples': ['Москва', 'Балашиха', 'Дубай','Иваново'],
            'responses': ['Оооо, мы практически соседи', 'Принял']
        },
        'cars': {
            'examples': ['Какая любимая марка машины?', 'Мерс или Бэха?', 'Какую машину хочешь купить?'],
            'responses': ['Конечно, Бэха', 'Поооорш)', 'Главное не мерседес!']
        },
        'place': {
            'examples': ['Где нахощишься?', 'Где живешь?', 'Откуда родом?'],
            'responses': ['Маунтин-вью, Калифорния, США', 'Мск', 'Modern City Holl']
        },
        'typeoftransport': {
            'examples': ['У тебя есть машина?', 'Что у тебя есть?', 'Какая у тебя тачка?'],
            'responses': ['Я в такую погоду езжу на бэхе', 'Метрополитен - это здорово', 'Люблю путешествовать любыми видами транспорта','Конечно, Бэха',]
        },
        'weather': {
            'examples': ['Какая погода?', 'Как на улице?', 'Что за окном?'],
            'responses': ['Снежно', 'Солнечно', 'Холодно']
        },
        'likefood': {
            'examples': ['Какое блюдо предпочитаешь?', 'Что нравится из еды?', 'Любимая еда?'],
            'responses': ['Пиццу..)', 'Пельмеши!', 'Я бы перекусил в Маке!']
        },
        'animalslike': {
            'examples': ['Какое любимое животное?', 'Какое домашнее животное есть?', 'Любимый питомец?'],
            'responses': ['Обожаю собак!', 'У меня питомца,но мечтаю о таксе!)', 'Люблю Жирафов)']
        },
        'marks': {
            'examples': ['Какую марку предпочитаешь?', 'Где бы ты купил кроссвоки?', 'Любимая марка?'],
            'responses': ['Точно адик', 'Главное не NIKE', 'Я обожаю три полоски!)']
        },
        'subject': {
            'examples': ['Любимый предмет?', 'Как относишься к геометрии?', 'Что по урокам?'],
            'responses': ['Обожаю геометрию!', 'Сейчас сижу думаю,как буду решать..', 'Алгебра ван лав!']
        },
        'class': {
            'examples': ['Чем занимаешься?', 'Какие хобби?', 'Чем увлекаешься?'],
            'responses': ['Прогаю', 'Самокатом', 'Люблю баскет!']
        },
        'bye': {
            'examples': ['Пока!', 'Увидимся!', 'Счастливо)', "Гуд бай", "До свидания!", 'До скорых встреч', 'Спокойной ночи)'],
            'responses': ['До свидания!', 'До скорых встреч', 'Спокойной ночи)','Пока!', 'Увидимся)', 'Счастливо)', "Гуд бай..."]
        },
        'howdoyoudo': {
            'examples': ['Как дела?', 'Как жизнь????', 'Как ты?!'],
            'responses': ['Неплохо!', 'Отлично!!', 'Ужасно(((']
        }
        }
}

import json

with open("Data_Base.json", "w", encoding="utf-8") as file:
    json.dump(BOT_CONFIG, file, sort_keys = True)
