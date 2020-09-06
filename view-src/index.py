from urllib.parse import unquote
from http.server import BaseHTTPRequestHandler

import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        try:
            url = self.path.partition('?')[2]
            response = self.fetch_page(url)
        except Exception as e:
            response = repr(e)
        self.wfile.write(response.encode())

    def fetch_page(self, url):
        url = unquote(url)
        return requests.get(url).text
