from framework.templates import render


def index_page(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('index.html', secret=secret)


def about_page(request):
    return '200 OK', "About"


def contact_view(request):
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Пришло сообщение от {email}, по теме {title}, с текстом {text}')
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')
