#!/usr/bin/python3
"""
API module
"""
import http.server
import socketserver


class Server(http.server.BaseHTTPRequestHandler):
    """simple server"""
    def do_GET(self):
        if  self.path.endswith("/data"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(
                '{"name": "John", "age": 30, "city": "New York"}', "utf-8"
                ))
        elif self.path.endswith("/info"):
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(
            '{"version": "1.0", "description": "A simple API built with \
http.server"}', "utf-8"
                ))
        elif self.path.endswith("/"):
            self.send_response(200)
            self.send_header("Content-type", "html")
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

    def serve_forever(port):
        socketserver.TCPServer(("", port), Server).serve_forever()

if __name__ == "__main__":
    Server.serve_forever(8000)
