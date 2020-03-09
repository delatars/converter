import logging
from http.server import ThreadingHTTPServer

from converter.server.app import setup_app


logger = logging.getLogger("web_server")


def start_web_server(bind):
    host, port = bind.split(":")
    with ThreadingHTTPServer((host, int(port)), RequestHandlerClass=setup_app()) as http_server:
        try:
            logger.info(f"Currency converter webserver started on: {bind}")
            http_server.serve_forever()
        except KeyboardInterrupt:
            logger.info(f"Shutdown server.")
            http_server.server_close()
