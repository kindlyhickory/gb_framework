import quopri


class Application:
    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode('  UTF-8')

    def add_route(self, url):
        def inner(view):
            self.urls[url] = view

        return inner

    @staticmethod
    def parse_input_data(data: str):
        result = {}
        if data:
            params = data.split('&')
            for item in params:
                key, value = item.split('=')
                result[key] = value
        return result

    def parse_wsgi_input_data(self, data):
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = self.parse_input_data(data_str)
        return result

    @staticmethod
    def get_wsgi_input_data(env):
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def __init__(self, urls, front_controllers):
        self.urls = urls
        self.front_controllers = front_controllers

    def __call__(self, env, start_response):
        path = env['PATH_INFO']
        print(env)
        if not path.endswith('/'):
            path = path + '/'

        method = env['REQUEST_METHOD']

        data = self.get_wsgi_input_data(env)
        data = self.parse_wsgi_input_data(data)

        query_string = env['QUERY_STRING']
        print(f'query_string {query_string}')
        request_params = self.parse_input_data(query_string)
        print(f'request_params {request_params}')

        if path in self.urls:
            view = self.urls[path]
            request = {}
            request['method'] = method
            request['data'] = data
            request['request_params'] = request_params
            for controller in self.front_controllers:
                controller(request)
            code, text = view(request)
            start_response(code, [('Content-type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]
