class Application:
    def __init__(self, urls, front_controllers):
        self.urls = urls
        self.front_controllers = front_controllers

    def __call__(self, env, start_response):
        path = env['PATH_INFO']
        if not path.endswith('/'):
            path = path + '/'
        if path in self.urls:
            view = self.urls[path]
            request = {}
            for controller in self.front_controllers:
                controller(request)
            code, text = view(request)
            start_response(code, [('Content-type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]