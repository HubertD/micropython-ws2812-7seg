from machine import Pin
from dseg7display import Dseg7Display
import uhttpd
import http_file_handler
import http_api_handler


class DigitHandler:
    def __init__(self):
        self.number = 0
        self.r = 10
        self.g = 10
        self.b = 10
        self.pin = Pin(2)
        self.pin.init(self.pin.OUT)
        self.display = Dseg7Display(self.pin)
        self.display.set_number(self.number, self.r, self.g, self.b)
        self.display.write()

    def get(self, req):
        return {'num': self.number, 'r': self.r, 'g': self.g, 'b': self.b}

    def post(self, req):
        params = req['body']
        if 'num' in params:
            self.number = int(params['num'])
        if 'r' in params:
            self.r = max(min(int(params['r']), 255), 0)
        if 'g' in params:
            self.g = max(min(int(params['g']), 255), 0)
        if 'b' in params:
            self.b = max(min(int(params['b']), 255), 0)
        self.display.set_number(self.number, self.r, self.g, self.b)
        self.display.write()
        return self.get(req)


server = uhttpd.Server([
    ('/api', http_api_handler.Handler([(['set'], DigitHandler()), ])),
    ('/', http_file_handler.Handler('/www'))
])
server.run()
