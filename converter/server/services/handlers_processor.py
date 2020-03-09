from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from converter.server.responses import error
from converter.server.errors import ERROR_NOT_IMPLEMENTED


class HandlersProcessor(BaseHTTPRequestHandler):

    def __init__(self, routers_obj):
        self.routers = routers_obj
        self.app = {}
        self.path = ""
        self.query = ""

    def __call__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def parse_request(self):
        result = super().parse_request()
        if not result:
            return False
        http_method, path, _ = self.requestline.split()
        uri = urlparse(path)
        self.http_method = http_method
        self.path = uri.path
        self.query = parse_qs(uri.query)
        return True

    def _process_response(self, response):
        self.send_response(response.status)
        for header in response.headers:
            self.send_header(header[0], header[1])
        self.end_headers()
        self.wfile.write(response.body)

    def do_GET(self):
        response = self.routers._process_request(self)
        self._process_response(response)

    def do_POST(self):
        self._process_response(error(ERROR_NOT_IMPLEMENTED))

    def do_DELETE(self):
        self._process_response(error(ERROR_NOT_IMPLEMENTED))

    def do_HEAD(self):
        self._process_response(error(ERROR_NOT_IMPLEMENTED))

    def do_OPTIONS(self):
        self._process_response(error(ERROR_NOT_IMPLEMENTED))

    def do_PUT(self):
        self._process_response(error(ERROR_NOT_IMPLEMENTED))

    def do_PATCH(self):
        self._process_response(error(ERROR_NOT_IMPLEMENTED))
