import sys
from tornado import httpserver, ioloop, web, options
from asynchronization import async_function

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world! My name is Eagle.")

if __name__ == "__main__":
	async_function.test_func()
	handlers = [
		(r"/", MainHandler),
	]

	app = tornado.web.Application(handlers)
	http_server = httpserver.HTTPServer(app)
    http_server.listen(9012)
    ioloop.IOLoop.current().start()
