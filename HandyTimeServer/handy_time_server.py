#!/usr/bin/env python3
# coding=utf-8
import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse
import json
import time
import HandyTimeServer
from HandyTimeServer.version import __version__, __description__


# =============================================================================


class MyServer(BaseHTTPRequestHandler):
    # noinspection PyPep8Naming
    def do_GET(self):
        now = time.time()
        dt_now = datetime.datetime.now()
        tm = time.localtime(now)
        utc_tm = time.gmtime(now)
        my_local = dict(year=tm[0], month=tm[1], dom=tm[2], hour=tm[3], min=tm[4], sec=tm[5], dow=tm[6], doy=tm[7],
                        is_dst=tm[8])
        my_utc = dict(year=utc_tm[0], month=utc_tm[1], dom=utc_tm[2], hour=utc_tm[3], min=utc_tm[4], sec=utc_tm[5],
                      dow=utc_tm[6], doy=utc_tm[7], is_dst=utc_tm[8])
        tz_info = datetime.datetime.now(datetime.timezone.utc).astimezone()
        tz_name = tz_info.tzinfo.tzname(dt_now)
        tz_offset = tz_info.tzinfo.utcoffset(dt_now).seconds
        my_time = dict(local=my_local, utc=my_utc, tick=now, tz=dict(name=tz_name, offset=tz_offset))
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
    parser = argparse.ArgumentParser(prog=f"{HandyTimeServer.__name__}",
                                     description=f"{HandyTimeServer.__name__} - {__description__}", add_help=False)
    parser.add_argument("-l", "--listener", help="listener name/address (default 0.0.0.0 = any listener).",
                        default="0.0.0.0")
    parser.add_argument("-p", "--port", type=int, help="port#", required=True)
    parser.add_argument("--version", action="version", version=f"{HandyTimeServer.__name__} {__version__}")
    parser.add_argument("-?", "--help", help="show help message and quit", action="help")
    args = parser.parse_args()
    return args


# =============================================================================


def main():
    args = arg_parser()
    web_server = HTTPServer((args.listener, args.port), MyServer)
    print(f"{HandyTimeServer.__name__} started http://{args.listener}:{args.port}")
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass
    web_server.server_close()
    print(f"{HandyTimeServer.__name__} stopped")
    return


if __name__ == '__main__':
    main()
