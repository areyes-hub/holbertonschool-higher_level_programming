#!/usr/bin/python3
"""
API module
"""
import http.server
import socketserver
import json


class Server(http.server.BaseHTTPRequestHandler):
    """simple server"""
    def do_GET(self):
        if  self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(bytes(json.dumps(data), "utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple \
API built with http.server"}
            self.wfile.write(bytes(json.dumps(info), "utf-8"))
        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(
                "<html><head><title></title><body><p>Hello, this is a \
                    simple API!</p></body></head></html>", "utf-8"
                ))
        else:
            self.send_response(404, "Not Found")
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(
                "<html><body><h1>Endpoint not found</h1></body></html>", \
                    "utf-8"
                ))

def run_server(port):
    with socketserver.TCPServer(("", port), Server) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server(8000)
