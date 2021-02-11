from framework.templates import render


def index_page(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('index.html', secret=secret)

def about_page(request):
    return '200 OK', "About"
