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
        'title': 'Модернизация системы управления микроклиматом (птицеводство)',
        'year': 2013,
        'description': 'Разработка и внедрение системы контроля и регулирования уровня вентиляции, CO2, температуры и влажности в птичнике. Замена устаревших датчиков, программирование ПЛК OWEN, интеграция с SCADA-системой.',
        'technologies': ['СПК107', 'Мастер-Скада', 'Modbus TCP'],
        'images': ['Ukpf1.png',  'Ukpf2.png'],  # Добавляем изображения
        'videos': []  # Добавляем видео
    },
    {
        'title': 'Модернизация системы транспортировки битона на производстве ЖБИ',
        'year': 2018,
        'description': 'Разработка и внедрение системы управления кюбельной тележкой. Разработка электросхем, программирование ПЛК Delta, создание интерфейса оператора в Мастер-Скада.',
        'technologies': ['ПЛК Delta', 'CAD', 'Modbus RTU', 'Power Line Communication', 'Преобразователь частоты'],
        'images': ['foto_kub1.jpg', 'foto_kub2.jpg'],
        'videos': ['vid_kub1.mp4']
    },
    {
        'title': 'Система мониторинга энергоресурсов на пищевом производстве',
        'year': 2020,
        'description': 'Разработка ПО для сбора данных с счетчиков и датчиков, визуализация и формирование отчетов.',
        'technologies': ['Мастер-Скада', 'Меркурий', 'RS-485'],
        'images': [],
        'videos': []
    }
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