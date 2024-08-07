from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b'Post error')


simple_server = HTTPServer(("localhost", 8001), SimpleHTTPRequestHandler)

simple_server.serve_forever()
