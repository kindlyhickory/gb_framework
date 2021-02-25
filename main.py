from framework.application import Application, DebugApplication, FakeApplication
from Logger import Logger
from framework.templates import render
from models import TrainingSite
from Logger import debug


def secret_controller(request):
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]
urls = {

}

application = Application(urls, front_controllers)
# debug_application = DebugApplication(urls,front_controllers)
# fake_application = FakeApplication(urls, front_controllers)


site = TrainingSite()
logger = Logger('main')


@application.add_route('/')
@debug
def main_view(request):
    logger.log('Список курсов')
    print(f'Список курсов - {site.courses}')
    return '200 OK', render('course_list.html', objects_list=site.courses)


@application.add_route('/create-course/')
@debug
def create_course(request):
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))
            course = site.create_course('record', name, category)
            site.courses.append(course)
        return '200 OK', render('create_course.html')
    else:
        categories = site.categories
        return '200 OK', render('create_course.html', categories=categories)


@application.add_route('/create-category/')
@debug
def create_category(request):
    if request['method'] == 'POST':
        data = request['data']
        name = data['name']

        name = Application.decode_value(name)
        category_id = data.get('category_id')

        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)

        site.categories.append(new_category)
        return '200 OK', render('create_category.html')
    else:
        categories = site.categories
        return '200 OK', render('create_category.html', categories=categories)


@application.add_route('/copy-course/')
@debug
def copy_course(request):
    request_params = request['request_params']
    name = request_params['name']
    old_course = site.get_course(name)
    if old_course:
        new_name = f'copy_{name}'
        new_course = old_course.clone()
        new_course.name = new_name
        site.courses.append(new_course)

    return '200 OK', render('course_list.html', objects_list=site.courses)


@application.add_route('/category-list/')
@debug
def category_list(request):
    logger.log('Список категорий')
    return '200 OK', render('category_list.html', objects_list=site.categories)
