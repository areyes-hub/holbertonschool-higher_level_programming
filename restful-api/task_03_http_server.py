#!/usr/bin/python3
"""
API module
"""
import http.server
import socketserver
import json


class Server(http.server.BaseHTTPRequestHandler):
    """
    simple server class
    """
    def do_GET(self):
        if self.path == "/data":
            self.send_response(200, "OK")
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200, "OK")
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple \
API built with http.server"}
            self.wfile.write(json.dumps(info).encode("utf-8"))
        elif self.path == "/":
            self.send_response(200, "OK")
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                "<html><body><p>Hello, this is a \
                    simple API!</p></body></html>".encode("utf-8")
                )
        elif self.path == "/status":
            self.send_response(200, "OK")
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                "<html><body><p>OK\
                </p></body></html>".encode("utf-8"))
        else:
            self.send_response(404, "Not Found")
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(
                "<html><body><p>Endpoint not found</p></body></html>".
                encode("utf-8")
                )


def run_server(port):
    with socketserver.TCPServer(("", port), Server) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()


run_server(8000)
