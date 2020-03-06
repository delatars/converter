from http.server import ThreadingHTTPServer

from converter.server.app import setup_app


def start_web_server():
    with ThreadingHTTPServer(("0.0.0.0", 8888), RequestHandlerClass=setup_app()) as http_server:
        http_server.serve_forever()


if __name__ == '__main__':
    start_web_server()
