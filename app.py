from flask import Flask, render_template
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Данные для страницы проектов
PROJECTS_LIST = [
    {
        'title': 'Модернизация системы КИПиА на молокозаводе',
        'year': 2022,
        'description': 'Разработка и внедрение системы контроля температуры и давления в линии пастеризации. Замена устаревших датчиков, настройка ПЛК Siemens, интеграция с SCADA-системой.',
        'technologies': ['Siemens S7-1500', 'WinCC OA', 'Profibus', 'Python (скрипты обработки данных)']
    },
    {
        'title': 'Автоматизация фасовочной линии на кондитерском производстве',
        'year': 2020,
        'description': 'Проектирование АСУТП для новой фасовочной линии. Разработка электросхем в NanoCAD, программирование ПЛК Omron, создание интерфейса оператора.',
        'technologies': ['Omron CP1E', 'CAD', 'Modbus TCP', 'Собственный UI на Python']
    },
    {
        'title': 'Система мониторинга энергоэффективности',
        'year': 2019,
        'description': 'Разработка ПО для сбора данных с счетчиков и датчиков, визуализации в веб-интерфейсе и формирования отчетов.',
        'technologies': ['Python (Django)', 'PostgreSQL', 'Modbus RTU', 'Android (приложение для техников)']
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

if __name__ == '__main__':
    app.run(debug=True)