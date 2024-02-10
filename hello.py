import http.server
import socketserver
from http import HTTPStatus
from pdm_hello_world.hello_world import hello

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        hello_world = hello('World')
        self.wfile.write(f'{hello_world}'.encode())


if __name__ == '__main__':
    httpd = socketserver.TCPServer(('', 8000), Handler)
    httpd.serve_forever()
