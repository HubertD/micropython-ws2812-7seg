from machine import Pin
from display import Display
import uhttpd
import http_file_handler
import http_api_handler


class DigitHandler:
    def __init__(self):
        self.number = 0
        self.color = (10, 10, 10)
        self.display = Display(Pin(2))
        self.display.set(self.number, self.color)

    def get(self, req):
        r, g, b = self.color
        return {'num': self.number, 'r': r, 'g': g, 'b': b}

    def post(self, req):
        params = req['body']
        r, g, b = self.color
        if 'num' in params:
            self.number = int(params['num'])
        if 'r' in params:
            r = max(min(int(params['r']), 255), 0)
        if 'g' in params:
            g = max(min(int(params['g']), 255), 0)
        if 'b' in params:
            b = max(min(int(params['b']), 255), 0)
        self.color = (r, g, b)
        self.display.set(self.number, self.color)
        return self.get(req)


server = uhttpd.Server([
    ('/api', http_api_handler.Handler([(['set'], DigitHandler()), ])),
    ('/', http_file_handler.Handler('/www'))
])
server.run()
