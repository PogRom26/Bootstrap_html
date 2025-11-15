from flask import Flask, Response

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/<path:any_path>', methods=['GET'])
def contacts_page(any_path=None):
    """
    Обрабатывает любой GET-запрос и возвращает страницу "Контакты"
    """
    try:
        # Читаем HTML-файл с контактами
        with open('contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Возвращаем HTML-контент с правильным Content-Type
        return Response(
            html_content,
            mimetype='text/html',
            status=200
        )

    except FileNotFoundError:
        return Response(
            "<h1>Ошибка 404</h1><p>Файл contacts.html не найден</p>",
            mimetype='text/html',
            status=404
        )

    except Exception as e:
        return Response(
            f"<h1>Ошибка 500</h1><p>Внутренняя ошибка сервера: {str(e)}</p>",
            mimetype='text/html',
            status=500
        )


if __name__ == '__main__':
    # Запускаем сервер на localhost:5000
    app.run(host='localhost', port=8000, debug=True)