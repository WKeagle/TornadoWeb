import tornado.ioloop
import tornado.web
import sys
from asynchronization import async_function

sys.dont_write_bytecode = True

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world! My name is Eagle.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
	async_function.test_func()
    # app = make_app()
    # app.listen(8086)
    # tornado.ioloop.IOLoop.current().start()
