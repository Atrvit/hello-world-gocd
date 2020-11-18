import http.server
import os
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'GoCD -> Hello world! Heroku!')


try:
    port = os.environ["PORT"]
    httpd = socketserver.TCPServer(('0.0.0.0', int(port)), Handler)
except:
    httpd = socketserver.TCPServer(('0.0.0.0', 8080), Handler)

httpd.serve_forever()


# python3 server.py
# 127.0.0.1 - - [11/Apr/2017 11:36:49] "GET / HTTP/1.1" 200 -
# http :8080
'''
HTTP/1.0 200 OK
Date: Tue, 11 Apr 2017 15:36:49 GMT
Server: SimpleHTTP/0.6 Python/3.5.2
Hello world
'''
