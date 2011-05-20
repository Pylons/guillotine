

class Guillotine(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if environ.get('REQUEST_METHOD') != 'HEAD':
            return self.app(environ, start_response)
        environ = environ.copy()
        environ['REQUEST_METHOD'] = 'GET'
        self.app(environ, start_response)
        return []


def make_middleware(app, global_conf, **config):
    return Guillotine(app)

