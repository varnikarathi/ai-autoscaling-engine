from http.server import HTTPServer,BaseHTTPRequestHandler
import time
request_count=0
start_time=time.time()
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global request_count
        #to ignore browser noise(favicon.ico)
        if self.path=="/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return 
        request_count+=1
        elapsed_time=time.time()-start_time
        rps=request_count/elapsed_time if elapsed_time>0 else 0
        print(f"Request_count:{request_count} rps:{rps:.2f}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Number of requests recieved:{request_count}\n Requests per second:{rps:.2f}".encode())
        with open("metrics.txt","a") as f:
            f.write(f"{elapsed_time},{request_count},{rps:.2f}\n")
server=HTTPServer(("localhost",8000),MyServer)
print("Server running at http://localhost:8000")
server.serve_forever()
