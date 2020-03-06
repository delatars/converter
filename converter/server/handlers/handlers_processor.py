from http.server import BaseHTTPRequestHandler

from ..router_dispatcher import RoutersDispatcher


class HandlersProcessor(BaseHTTPRequestHandler):

    def __init__(self, routers_obj: RoutersDispatcher):
        self.routers = routers_obj

    def __call__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def do_GET(self):
        response = self.routers.process_request(self)
        self.send_response(response.status)
        for header in response.headers:
            self.send_header(header[0], header[1])
        self.end_headers()
        self.wfile.write(response.body)
