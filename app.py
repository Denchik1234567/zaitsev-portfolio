from flask import Flask, render_template
import os


#  Проверка что изменилось
# git status
# Собираем статическую версию
# python build_static.py
# Заливаем на GitHub
# git add .
# git commit -m "Описание изменений"
# git push

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Данные для страницы проектов с поддержкой медиа
PROJECTS_LIST = [

    {
        'title': 'Разработка ПО на Python',
        'year': 2023,
        'description': 'Разработка ПО для конфигурирования преобразователей частоты компании КИППРИБОР.',
        'technologies': ['Python', 'Modbus RTU', 'RS-485'],
        'images': ["AFDConfig.png"],
        'videos': []
    },

    {
        'title': 'Разработка щита управления роторным дозатором',
        'year': 2021,
        'description': 'Проектирование и внедрение щита управления, разработка электросхем, программирование ПЛК Festo, программирование панели оператора Festo.',
        'technologies': ['Modbus RTU', 'RS-485'],
        'images': [],
        'videos': ["Karusel1.mp4"]
    },

    {
        'title': 'Разработка системы мониторинга параметров аптечного склада',
        'year': 2020,
        'description': 'Проектирование и внедрение щита, разработка электросхем, конфигурирование системы OWEN CLOUD.',
        'technologies': ['OWEN CLOUD', 'Modbus RTU', 'RS-485', "Датчики температуры и влажности"],
        'images': ["Oven1.png", "Oven2.png", "Oven3.png"],
        'videos': []
    },

    {
        'title': 'Система мониторинга энергоресурсов на пищевом производстве',
        'year': 2020,
        'description': 'Разработка ПО для сбора данных с счетчиков и датчиков, визуализация и формирование отчетов.',
        'technologies': ['Мастер-Скада', 'Меркурий', 'RS-485'],
        'images': [],
        'videos': []
    },

    {
        'title': 'Модернизация камер тепловлажностной обработки бетона на производстве ЖБИ',
        'year': 2019,
        'description': 'Проектирование и внедрение щита управления системой, разработка электросхем, программирование ПЛК Delta, конфигурирование модулей ОВЕН.',
        'technologies': ['ПЛК Delta', 'CAD', 'Modbus TCP', 'Модули ввода/вывода', "Мониторинг"],
        'images': ['Tvo1.png', 'Tvo2.png'],
        'videos': []
    },

    {
        'title': 'Модернизация установки для производства каркасов из арматуры на производстве ЖБИ',
        'year': 2019,
        'description': 'Проектирование и внедрение щита управления станком, разработка электросхем, программирование ПЛК Delta, программирование панели оператора Delta.',
        'technologies': ['ПЛК Delta', "Панель оператора Delta", 'CAD', 'Modbus TCP', 'Преобразователь частоты', "Синхронизация по энкодерам"],
        'images': ['Svai1.png', 'Svai2.png', 'Svai3.png', 'Svai4.png', 'Svai5.png'],
        'videos': []
    },

    {
        'title': 'Модернизация системы транспортировки битона на производстве ЖБИ',
        'year': 2018,
        'description': 'Разработка и внедрение системы управления кюбельной тележкой, разработка электросхем, программирование ПЛК Delta, создание интерфейса оператора в Мастер-Скада.',
        'technologies': ['ПЛК Delta', 'CAD', 'Modbus RTU', 'Power Line Communication', 'Преобразователь частоты'],
        'images': ['foto_kub1.jpg', 'foto_kub2.jpg'],
        'videos': ['vid_kub1.mp4']
    },

    {
        'title': 'Модернизация системы управления микроклиматом (птицеводство)',
        'year': 2013,
        'description': 'Разработка и внедрение системы контроля и регулирования уровня вентиляции, CO2, температуры и влажности в птичнике, замена устаревших датчиков, программирование ПЛК OWEN, интеграция с SCADA-системой.',
        'technologies': ['СПК107', 'Мастер-Скада', 'Modbus TCP'],
        'images': ['Ukpf1.png',  'Ukpf2.png'],  # Добавляем изображения
        'videos': []  # Добавляем видео
    },
]

# Основные маршруты (без .html)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS_LIST)

# Дополнительные маршруты с .html для удобства
@app.route('/index.html')
def index_html():
    return render_template('index.html')

@app.route('/experience.html')
def experience_html():
    return render_template('experience.html')

@app.route('/projects.html')
def projects_html():
    return render_template('projects.html', projects=PROJECTS_LIST)

@app.route('/projects_debug')
def projects_debug():
    return render_template('projects_debug.html', projects=PROJECTS_LIST)

if __name__ == '__main__':
    app.run(debug=True)