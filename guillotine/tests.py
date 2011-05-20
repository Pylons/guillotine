import unittest


class GuillotineTests(unittest.TestCase):

    def test_GET(self):
        from guillotine import Guillotine
        mw = Guillotine(dummy_app)
        environ = {'REQUEST_METHOD': 'GET'}
        start_response_called = {}
        def start_response(status, headers):
            start_response_called['status'] = status
            start_response_called['headers'] = headers
        app_iter = mw(environ, start_response)
        self.assertEqual(app_iter, ['Hi.'])
        self.assertEqual(start_response_called['status'], '200 OK')
        self.assertEqual(start_response_called['headers'], (
            ('Content-type', 'text/plain'),
            ('Content-length', '3')))

    def test_HEAD(self):
        from guillotine import Guillotine
        mw = Guillotine(dummy_app)
        environ = {'REQUEST_METHOD': 'HEAD'}
        start_response_called = {}
        def start_response(status, headers):
            start_response_called['status'] = status
            start_response_called['headers'] = headers
        app_iter = mw(environ, start_response)
        self.assertEqual(app_iter, [])
        self.assertEqual(start_response_called['status'], '200 OK')
        self.assertEqual(start_response_called['headers'], (
            ('Content-type', 'text/plain'),
            ('Content-length', '3')))


def dummy_app(environ, start_response):
    start_response('200 OK', (('Content-type', 'text/plain'),
                              ('Content-length', '3')))
    return ['Hi.']
