from app import app, PROJECTS_LIST
import os
import shutil


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

    # Настраиваем Flask для работы вне контекста запроса
    app.config['SERVER_NAME'] = 'localhost:5000'
    app.config['APPLICATION_ROOT'] = '/'
    app.config['PREFERRED_URL_SCHEME'] = 'http'

    with app.app_context():
        try:
            # Генерируем главную страницу
            with open('docs/index.html', 'w', encoding='utf-8') as f:
                f.write(render_template_safe('index.html'))
            print("✅ index.html создан")

            # Генерируем страницу опыта
            with open('docs/experience.html', 'w', encoding='utf-8') as f:
                f.write(render_template_safe('experience.html'))
            print("✅ experience.html создан")

            # Генерируем страницу проектов
            with open('docs/projects.html', 'w', encoding='utf-8') as f:
                f.write(render_template_safe('projects.html', projects=PROJECTS_LIST))
            print("✅ projects.html создан")

        except Exception as e:
            print(f"❌ Ошибка при создании HTML: {e}")
            return

    # Создаем файл .nojekyll для GitHub Pages
    with open('docs/.nojekyll', 'w') as f:
        f.write('')
    print("✅ .nojekyll создан")

    print("\n🎉 Статический сайт создан в папке docs/")
    print("📁 Для GitHub Pages используйте папку: /docs")
    print("🌐 Сайт будет доступен по адресу: https://your-username.github.io/your-repository-name/")


def render_template_safe(template_name, **context):
    """Безопасный рендеринг шаблона с заменой Flask путей на статические"""
    from flask import render_template

    # Рендерим шаблон
    html = render_template(template_name, **context)

    # Заменяем Flask пути на статические
    html = html.replace("{{ url_for('static', filename='", "static/")
    html = html.replace("') }}", "")
    html = html.replace("{{ url_for('index') }}", "index.html")
    html = html.replace("{{ url_for('experience') }}", "experience.html")
    html = html.replace("{{ url_for('projects') }}", "projects.html")

    return html


if __name__ == '__main__':
    build_static_site()