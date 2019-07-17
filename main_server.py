import sys
from tornado import httpserver, ioloop, web, options
from src.asynchronization import async_function

class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world! My name is Eagle.")

if __name__ == "__main__":
	async_function.test_func()

	settings = dict(
		autoreload=True,
	)
	handlers = [
		(r"/", MainHandler),
	]

	app = web.Application(handlers, settings)
	http_server = httpserver.HTTPServer(app)
	http_server.listen(9012)
	ioloop.IOLoop.instance().current().start()
	# ioloop.IOLoop.current().start()