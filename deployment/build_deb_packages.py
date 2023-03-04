#!/usr/bin/env python
# coding=utf-8

import argparse
import PackageBuilder

# =============================================================================


BUILD_INFO_FILENAME = "../LocalTimeServer_file_list.json"


# =============================================================================


class ValidateVersionNumber(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        parts = values.split(".")
        if len(parts) != 3:
            parser.error(f"Please enter a valid version number in <major>.<minor>.<maintenance> format")
        for part in parts:
            if not part.isdigit():
                parser.error(f"Please enter a valid version number in <major>.<minor>.<maintenance> format")
        setattr(namespace, self.dest, values)
        return


# =============================================================================


def arg_parser():
    """
    parse arguments

    :return: the parsed command line arguments
    """
    parser = argparse.ArgumentParser(description="makes LocalTimeServer a package for the specified target",
                                     add_help=False)
    parser.add_argument("-v", "--version", type=str, help="version#, i.e. x.y.z", required=True, action=ValidateVersionNumber)
    parser.add_argument("-?", "--help", help="show help message and quit", action="help")
    args = parser.parse_args()
    return args


def main():
    args = arg_parser()
    try:
        builder = PackageBuilder.PackageBuilder("LocalTimeServer", BUILD_INFO_FILENAME, args.version)
        builder.build_debian()
    except Exception as ex:
        print(f"Error: {ex}")
    return


if __name__ == '__main__':
    main()
