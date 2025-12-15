from http.server import HTTPServer,BaseHTTPRequestHandler
request_count=0
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global request_count
        request_count+=1
        print(f"Request_count:{request_count}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Number of requests recieved:{request_count}".encode())
server=HTTPServer(("localhost",8000),MyServer)
print("Server running at http://localhost:8000")
server.serve_forever()
