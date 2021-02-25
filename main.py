import views
from framework.application import Application, DebugApplication, FakeApplication

urls = {
    '/': views.main_view,
    '/create-course/': views.create_course,
    '/create-category/': views.create_category,
}


def secret_controller(request):
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]

application = Application(urls, front_controllers)
# debug_application = DebugApplication(urls,front_controllers)
# fake_application = FakeApplication(urls, front_controllers)
