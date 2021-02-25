import views
from framework.application import Application

urls = {
    '/': views.main_view,
    '/create-course/': views.create_course,
    '/create-category/': views.create_category,
    '/copy-course/': views.copy_course,
    '/category-list/': views.category_list,

}


def secret_controller(request):
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]

application = Application(urls, front_controllers)
