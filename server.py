from http.server import HTTPServer, BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello! Server is running.")

server = HTTPServer(("localhost", 8000), MyServer)

print("Server running at http://localhost:8000")
server.serve_forever()
