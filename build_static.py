import os
import shutil
import re
import subprocess
from app import PROJECTS_LIST


def convert_video_for_web(input_path, output_path):
    """Конвертирует видео в веб-совместимый формат"""
    try:
        # Создаем папку для выходного файла если нет
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        cmd = [
            'ffmpeg', '-i', input_path,
            '-c:v', 'libx264',
            '-profile:v', 'high',
            '-level', '4.0',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-movflags', '+faststart',
            '-y', output_path
        ]

        # Запускаем конвертацию
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            return True
        else:
            print(f"❌ Ошибка конвертации {input_path}: {result.stderr}")
            # Копируем оригинал если конвертация не удалась
            shutil.copy2(input_path, output_path)
            return False

    except Exception as e:
        print(f"❌ Ошибка при конвертации видео: {e}")
        # Копируем оригинал как fallback
        shutil.copy2(input_path, output_path)
        return False


def build_static_site():
    print("🔨 Сборка статического сайта для GitHub Pages (корневой деплой)...")

    # Создаем папку docs если её нет
    output_dir = 'docs'
    os.makedirs(output_dir, exist_ok=True)

    # Копируем статические файлы (CSS, изображения)
    if os.path.exists(f'{output_dir}/static'):
        shutil.rmtree(f'{output_dir}/static')

    if os.path.exists('static'):
        # Сначала копируем всю структуру
        shutil.copytree('static', f'{output_dir}/static')
        print("✅ Статические файлы скопированы")

        # Затем обрабатываем видео
        video_dir = 'static/video/projects'
        output_video_dir = f'{output_dir}/static/video/projects'

        if os.path.exists(video_dir):
            for video_file in os.listdir(video_dir):
                if video_file.lower().endswith('.mp4'):
                    input_path = os.path.join(video_dir, video_file)
                    output_path = os.path.join(output_video_dir, video_file)

                    print(f"🔄 Обработка видео: {video_file}")
                    if convert_video_for_web(input_path, output_path):
                        print(f"✅ Видео {video_file} обработано")
    else:
        print("❌ Папка static не найдена")
        return

    # Копируем SEO файлы
    seo_files = ['sitemap.xml', 'robots.txt', 'yandex_657470568b79074b.html']
    for seo_file in seo_files:
        if os.path.exists(seo_file):
            shutil.copy2(seo_file, f'{output_dir}/')
            print(f"✅ {seo_file} скопирован")

    # Базовый HTML шаблон с SEO для корневого домена
    base_html = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="yandex-verification" content="657470568b79074b" />
    <title>{title}</title>

    <!-- SEO Мета-теги -->
    <meta name="description" content="Инженер АСУТП, КИПиА с опытом работы с 2010 года. Проектирование систем автоматизации, программирование ПЛК, SCADA системы, промышленная автоматизация.">
    <meta name="keywords" content="АСУТП, КИПиА, инженер, автоматизация, ПЛК, SCADA, CODESYS, промышленная автоматизация, Зайцев Денис">
    <meta name="author" content="Зайцев Денис Александрович">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://denisasutp.github.io">

    <!-- Структурированные данные -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Person",
      "name": "Зайцев Денис Александрович",
      "jobTitle": "Инженер АСУТП, КИПиА",
      "description": "Инженер АСУТП, КИПиА с опытом работы с 2010 года в области промышленной автоматизации",
      "birthDate": "1987",
      "telephone": "+7 (983) 543-97-95",
      "email": "Denis.Zaitsev.1987@yandex.ru",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Барнаул",
        "addressRegion": "Алтайский край",
        "addressCountry": "RU"
      }},
      "url": "https://denisasutp.github.io",
      "knowsAbout": [
        "АСУТП", "КИПиА", "ПЛК", "SCADA", "CODESYS", "МЭК 61131-3", 
        "Modbus", "Profinet", "Ethernet/IP", "Python", "Android разработка"
      ]
    }}
    </script>

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
            <p>&copy; 2025 Зайцев Денис Александрович</p>
            <p>Телефон: +7 (983) 543-97-95 | Email: Denis.Zaitsev.1987@yandex.ru</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Яндекс.Метрика -->
    <script type="text/javascript">
        (function(m,e,t,r,i,k,a){{
            m[i]=m[i]||function(){{(m[i].a=m[i].a||[]).push(arguments)}};
            m[i].l=1*new Date();
            for (var j = 0; j < document.scripts.length; j++) {{if (document.scripts[j].src === r) {{ return; }}}}
            k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
        }})(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=105093615', 'ym');

        ym(105093615, 'init', {{ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", accurateTrackBounce:true, trackLinks:true}});
    </script>
    <noscript><div><img src="https://mc.yandex.ru/watch/105093615" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
    <!-- /Яндекс.Метрика -->

</body>
</html>'''

    # Создаем index.html
    index_content = '''
    <div class="row align-items-center">
        <div class="col-md-4 text-center">
            <img src="static/img/photo.jpg" alt="Зайцев Денис Александрович - Инженер АСУТП, КИПиА" class="img-fluid rounded-circle mb-4 profile-photo">
        </div>
        <div class="col-md-8">
            <h1>Зайцев Денис Александрович</h1>
            <p class="lead">Инженер АСУТП, КИПиА с опытом работы с 2010 года</p>

            <div class="mt-4">
                <h2>Контактная информация</h2>
                <ul class="list-unstyled">
                    <li><strong>Год рождения:</strong> 1987</li>
                    <li><strong>Телефон:</strong> +7 (983) 543-97-95</li>
                    <li><strong>Email:</strong> Denis.Zaitsev.1987@yandex.ru</li>
                    <li><strong>Локация:</strong> Алтайский край, город Барнаул</li>
                </ul>
            </div>

            <div class="mt-4">
                <h2>Ключевые компетенции</h2>
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
    <h1>Опыт работы и Образование</h1>
    <div class="row">
        <div class="col-md-6">
            <div class="card mb-4">
                <div class="card-header bg-primary text-white">
                    <h2>Образование</h2>
                </div>
                <div class="card-body">
                    <h3>Политехнический колледж</h3>
                    <p>Специальность: Автоматизация технологических процессов и производств</p>
                    <h4 class="mt-3">Дополнительное образование:</h4>
                    <ul>
                        <li>Диплом автослесаря</li>
                        <li>Диплом автоэлектрика</li>
                    </ul>
                </div>
            </div>
            <div class="card mb-4">
                <div class="card-header bg-success text-white">
                    <h2>Водительское удостоверение</h2>
                </div>
                <div class="card-body">
                    <p>Категории: B, C</p>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card mb-4">
                <div class="card-header bg-info text-white">
                    <h2>Опыт работы</h2>
                </div>
                <div class="card-body">
                    <p><strong>С 2010 года</strong> в области АСУТП и КИПиА</p>
                    <p><strong>Отрасли:</strong> промышленные и пищевые производства</p>
                    <h4 class="mt-3">Основные направления:</h4>
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
            <h2>Технические навыки</h2>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <h3>Оборудование и приборы:</h3>
                    <ul>
                        <li>ПЛК ОВЕН, Delta, Schneider Electric и все что под CODESYS</li>
                        <li>Программируемые реле, ПЧ, Модули ввода/вывода, ПИД регуляторы, Даталоггеры, Анализаторы, Счетчики, Таймеры и.т.д</li>
                        <li>КИП (датчики температуры, давления, расхода, уровня и.т.д)</li>
                        <li>Промышленные роботы манипуляторы (FANUC, Delta, QJAR)</li>
                        <li>Промышленные протоколы (Modbus RTU/TCP, Profinet, Ethernet/IP, EtherCAT, SERCOS III, OPC, CANopen)</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h3>Программное обеспечение:</h3>
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

    # Создаем projects.html с поддержкой медиа
    projects_content = '''<h1>Выполненные проекты</h1>
    <div class="row">'''

    for project in PROJECTS_LIST:
        projects_content += f'''
        <div class="col-md-6 mb-4">
            <div class="card h-100">
                <div class="card-body">
                    <h2 class="card-title">{project['title']}</h2>
                    <h3 class="card-subtitle mb-2 text-muted">Год: {project['year']}</h3>
                    <p class="card-text">{project['description']}</p>'''

        # Добавляем изображения
        if 'images' in project and project['images']:
            projects_content += '''
                    <div class="mt-3">
                        <h4>Фотографии проекта:</h4>
                        <div class="project-gallery">'''

            for image in project['images']:
                projects_content += f'''
                            <img src="static/img/projects/{image}" 
                                 alt="Фото проекта {project['title']}" 
                                 class="img-thumbnail me-2 mb-2 project-image"
                                 style="max-width: 150px; cursor: pointer;"
                                 onclick="openModal('static/img/projects/{image}')">'''

            projects_content += '''
                        </div>
                    </div>'''

        # Добавляем видео
        if 'videos' in project and project['videos']:
            projects_content += '''
                    <div class="mt-3">
                        <h4>Видео проекта:</h4>
                        <div class="project-videos">'''

            for video in project['videos']:
                projects_content += f'''
                            <video controls class="img-thumbnail me-2 mb-2 project-video" style="max-width: 200px;">
                                <source src="static/video/projects/{video}" type="video/mp4">
                                Ваш браузер не поддерживает видео тег.
                            </video>'''

            projects_content += '''
                        </div>
                    </div>'''

        projects_content += f'''
                    <div class="mt-3">
                        <h4>Используемые технологии:</h4>
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
    <!-- Модальное окно для просмотра изображений -->
    <div class="modal fade" id="imageModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body text-center">
                    <img id="modalImage" src="" alt="" class="img-fluid">
                </div>
            </div>
        </div>
    </div>
    <div class="alert alert-info mt-4">
        <h3>Готов к новым вызовам!</h3>
        <p class="mb-0">Если у вас есть интересный проект в области АСУТП, КИПиА или автоматизации - свяжитесь со мной для обсуждения сотрудничества.</p>
    </div>
    <script>
    function openModal(imageSrc) {
        document.getElementById('modalImage').src = imageSrc;
        var myModal = new bootstrap.Modal(document.getElementById('imageModal'));
        myModal.show();
    }
    </script>'''

    # Сохраняем файлы
    with open(f'{output_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(base_html.format(title='Зайцев Денис Александрович - Инженер АСУТП, КИПиА', content=index_content))
    print("✅ index.html создан")

    with open(f'{output_dir}/experience.html', 'w', encoding='utf-8') as f:
        f.write(base_html.format(title='Опыт и Навыки - Зайцев Денис', content=experience_content))
    print("✅ experience.html создан")

    with open(f'{output_dir}/projects.html', 'w', encoding='utf-8') as f:
        f.write(base_html.format(title='Проекты - Зайцев Денис', content=projects_content))
    print("✅ projects.html создан с поддержкой медиа")

    # Создаем файл .nojekyll для GitHub Pages
    with open(f'{output_dir}/.nojekyll', 'w') as f:
        f.write('')
    print("✅ .nojekyll создан")

    print("\n🎉 Статический сайт создан в папке docs/")
    print("📁 Для GitHub Pages используйте папку: /docs")
    print("🌐 Сайт будет доступен по адресу: https://denisasutp.github.io")
    print("🔍 SEO оптимизация добавлена!")
    print("✅ Яндекс.Вебмастер сможет найти meta-тег на главной странице!")
    print("📊 Яндекс.Метрика добавлена и будет отслеживать посетителей!")
    print("🎬 Видео оптимизированы для веб-воспроизведения!")


if __name__ == '__main__':
    build_static_site()