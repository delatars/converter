import argparse
from http.server import ThreadingHTTPServer

from converter.server.app import setup_app


def start_web_server(bind):
    host, port = bind.split(":")
    with ThreadingHTTPServer((host, int(port)), RequestHandlerClass=setup_app()) as http_server:
        http_server.serve_forever()


def parse_args():
    parser = argparse.ArgumentParser(prog="Web server")
    bind = "127.0.0.1:8000"
    parser.add_argument(
        "-b", "--bind", type=str, default=bind,
        help=f"The socket to bind. (default: {bind})",
    )
    parser.add_argument("--debug", action="store_true", help=f"Debug mode")
    parser.set_defaults(debug=False)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    start_web_server(args.bind)
