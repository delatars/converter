import argparse

from converter.loggers import init_loggers
from converter.web_server import start_web_server


def parse_args():
    parser = argparse.ArgumentParser(prog="Currency converter web server")
    bind = "127.0.0.1:8000"
    parser.add_argument(
        "-b", "--bind", type=str, default=bind,
        help=f"The socket to bind. (default: {bind})",
    )
    parser.add_argument("--debug", action="store_true", help=f"Debug mode")
    parser.set_defaults(debug=False)
    return parser.parse_args()


def main():
    args = parse_args()
    init_loggers(args.debug)
    start_web_server(args.bind)


if __name__ == '__main__':
    main()
