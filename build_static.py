import os
import shutil
import re


def build_static_site():
    print("🔨 Сборка статического сайта для GitHub Pages...")

    # Создаем папку docs если её нет
    os.makedirs('docs', exist_ok=True)

    # Копируем статические файлы (CSS, изображения)
    if os.path.exists('docs/static'):
        shutil.rmtree('docs/static')

    if os.path.exists('static'):
        shutil.copytree('static', 'docs/static')
        print("✅ Статические файлы скопированы")
    else:
        print("❌ Папка static не найдена")
        return

    # Данные проектов
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

    # Базовый HTML шаблон
    base_html = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="index.html">Зайцев Д.А.</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="index.html">Главная</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="experience.html">Опыт и Навыки</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="projects.html">Проекты</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <main class="container my-5">
        {content}
    </main>

    <footer class="bg-dark text-light py-4 mt-5">
        <div class="container text-center">
            <p>&copy; 2024 Зайцев Денис Александрович</p>
            <p>Телефон: +7 (XXX) XXX-XX-XX | Email: your.email@example.com</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''

    # Создаем index.html
    index_content = '''
    <div class="row align-items-center">
        <div class="col-md-4 text-center">
            <img src="static/img/photo.jpg" alt="Зайцев Денис Александрович" class="img-fluid rounded-circle mb-4 profile-photo">
        </div>
        <div class="col-md-8">
            <h1>Зайцев Денис Александрович</h1>
            <p class="lead">Инженер АСУТП, КИПиА с опытом работы с 2010 года</p>

            <div class="mt-4">
                <h3>Контактная информация</h3>
                <ul class="list-unstyled">
                    <li><strong>Год рождения:</strong> 1987</li>
                    <li><strong>Телефон:</strong> +7 (XXX) XXX-XX-XX</li>
                    <li><strong>Email:</strong> your.email@example.com</li>
                    <li><strong>Локация:</strong> Алтайский край, город Барнаул</li>
                </ul>
            </div>

            <div class="mt-4">
                <h3>Ключевые компетенции</h3>
                <div class="d-flex flex-wrap gap-2">
                    <span class="badge bg-primary">АСУТП</span>
                    <span class="badge bg-primary">КИПиА</span>
                    <span class="badge bg-success">ПЛК</span>
                    <span class="badge bg-success">CODESYS</span>
                    <span class="badge bg-success">МЭК 61131-3</span>
                    <span class="badge bg-success">SCADA</span>
                    <span class="badge bg-info">САПР</span>
                    <span class="badge bg-info">Проектирование</span>
                    <span class="badge bg-warning">Android</span>
                    <span class="badge bg-warning">Python</span>
                </div>
            </div>
        </div>
    </div>'''

    # Создаем experience.html
    experience_content = '''
    <h2 class="mb-4">Опыт работы и Образование</h2>
    <div class="row">
        <div class="col-md-6">
            <div class="card mb-4">
                <div class="card-header bg-primary text-white">
                    <h5>Образование</h5>
                </div>
                <div class="card-body">
                    <h6>Политехнический колледж</h6>
                    <p>Специальность: Автоматизация технологических процессов и производств</p>
                    <h6 class="mt-3">Дополнительное образование:</h6>
                    <ul>
                        <li>Диплом автослесаря</li>
                        <li>Диплом автоэлектрика</li>
                    </ul>
                </div>
            </div>
            <div class="card mb-4">
                <div class="card-header bg-success text-white">
                    <h5>Водительское удостоверение</h5>
                </div>
                <div class="card-body">
                    <p>Категории: B, C</p>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card mb-4">
                <div class="card-header bg-info text-white">
                    <h5>Опыт работы</h5>
                </div>
                <div class="card-body">
                    <p><strong>С 2010 года</strong> в области АСУТП и КИПиА</p>
                    <p><strong>Отрасли:</strong> промышленные и пищевые производства</p>
                    <h6 class="mt-3">Основные направления:</h6>
                    <ul>
                        <li>Проектирование систем АСУТП и КИПиА</li>
                        <li>Программирование ПЛК</li>
                        <li>Панели оператора</li>
                        <li>Работа с SCADA-системами</li>
                        <li>Проектирование в САПР</li>
                        <li>Разработка ПО на Python</li>
                        <li>Создание приложений под Android</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header bg-warning">
            <h5>Технические навыки</h5>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h6>Оборудование и приборы:</h6>
                    <ul>
                        <li>ПЛК ОВЕН, Delta, Schneider Electric и все что под CODESYS</li>
                        <li>Программируемые реле, ПЧ, Модули ввода/вывода, ПИД регуляторы, Даталоггеры, Анализаторы, Счетчики, Таймеры и.т.д</li>
                        <li>КИП (датчики температуры, давления, расхода, уровня и.т.д)</li>
                        <li>Промышленные роботы манипуляторы (FANUC, Delta, QJAR)</li>
                        <li>Промышленные протоколы (Modbus RTU/TCP, Profinet, Ethernet/IP, EtherCAT, SERCOS III, OPC, CANopen)</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h6>Программное обеспечение:</h6>
                    <ul>
                        <li>CODESYS 2.3</li>
                        <li>CODESYS 3.5</li>
                        <li>Owen Logic</li>
                        <li>Arduino IDE</li>
                        <li>Python (опыт разработки ПО)</li>
                        <li>Android (опыт разработки ПО)</li>
                        <li>САПР (E3 Serios)</li>
                        <li>Master-SCADA, SIMPLE-SCADA, OPC Server</li>
                        <li>SolidWorks</li>
                        <li>И многое другое ПО для конфигурирования и параметрирования устройств</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>'''

    # Создаем projects.html
    projects_content = '''<h2 class="mb-4">Выполненные проекты</h2>
    <div class="row">'''

    for project in PROJECTS_LIST:
        projects_content += f'''
        <div class="col-md-6 mb-4">
            <div class="card h-100">
                <div class="card-body">
                    <h5 class="card-title">{project['title']}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">Год: {project['year']}</h6>
                    <p class="card-text">{project['description']}</p>
                    <div class="mt-3">
                        <h6>Используемые технологии:</h6>
                        <div class="d-flex flex-wrap gap-1">'''

        for tech in project['technologies']:
            projects_content += f'<span class="badge bg-secondary">{tech}</span>'

        projects_content += '''
                        </div>
                    </div>
                </div>
            </div>
        </div>'''

    projects_content += '''
    </div>
    <div class="alert alert-info mt-4">
        <h5>Готов к новым вызовам!</h5>
        <p class="mb-0">Если у вас есть интересный проект в области АСУТП, КИПиА или автоматизации - свяжитесь со мной для обсуждения сотрудничества.</p>
    </div>'''

    # Сохраняем файлы
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(base_html.format(title='Зайцев Денис Александрович - Инженер АСУТП, КИПиА', content=index_content))
    print("✅ index.html создан")

    with open('docs/experience.html', 'w', encoding='utf-8') as f:
        f.write(base_html.format(title='Опыт и Навыки - Зайцев Денис', content=experience_content))
    print("✅ experience.html создан")

    with open('docs/projects.html', 'w', encoding='utf-8') as f:
        f.write(base_html.format(title='Проекты - Зайцев Денис', content=projects_content))
    print("✅ projects.html создан")

    # Создаем файл .nojekyll для GitHub Pages
    with open('docs/.nojekyll', 'w') as f:
        f.write('')
    print("✅ .nojekyll создан")

    print("\n🎉 Статический сайт создан в папке docs/")
    print("📁 Для GitHub Pages используйте папку: /docs")
    print("🌐 Сайт будет доступен по адресу: https://your-username.github.io/your-repository-name/")


if __name__ == '__main__':
    build_static_site()