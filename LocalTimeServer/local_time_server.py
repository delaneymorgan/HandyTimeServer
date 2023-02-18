#!/usr/bin/env python
# coding=utf-8

from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse
import importlib.metadata
import json
import time
import LocalTimeServer


# =============================================================================


class MyServer(BaseHTTPRequestHandler):
    # noinspection PyPep8Naming
    def do_GET(self):
        tm = time.localtime()
        my_time = dict(year=tm[0], month=tm[1], dom=tm[2], hour=tm[3], min=tm[4], sec=tm[5], dow=tm[6], doy=tm[7],
                       is_dst=tm[8])
        json_text = json.dumps(my_time)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json_text, "utf-8"))
        return

    # noinspection PyShadowingBuiltins
    def log_message(self, format: str, *args: any) -> None:
        # DO NOTHING - NO NEED TO SPAM LOGS
        return


# =============================================================================


def arg_parser():
    """
    parse arguments

    :return: the parsed command line arguments
    """
    version = importlib.metadata.version("LocalTimeServerPkg")
    parser = argparse.ArgumentParser(description='LocalTimerServer - '
                                                 'a simple web-service providing local time on request in JSON format.',
                                     add_help=False)
    parser.add_argument("-h", "--host", help="host name", required=True)
    parser.add_argument("-p", "--port", type=int, help="port#", required=True)
    parser.add_argument("--version", action="version", version=f"{LocalTimeServer.__name__} {version}")
    parser.add_argument("-?", "--help", help="show help message and quit", action="help")
    args = parser.parse_args()
    return args


# =============================================================================


def main():
    args = arg_parser()
    web_server = HTTPServer((args.host, args.port), MyServer)
    print(f"{LocalTimeServer.__name__} started http://{args.host}:{args.port}")
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
    print(f"{LocalTimeServer.__name__} stopped")
    return


if __name__ == '__main__':
    main()
