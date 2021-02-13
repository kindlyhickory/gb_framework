import views
from framework.application import Application

urls = {
    '/main/': views.index_page,
    '/about/': views.about_page,
    '/contact/': views.contact_view,
}


def secret_controller(request):
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]

application = Application(urls, front_controllers)
