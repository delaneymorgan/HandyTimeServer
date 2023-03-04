#!/usr/bin/env python
# coding=utf-8

import argparse
import json
import os
import shutil

# =============================================================================


BUILD_INFO_FILEPATH = "../LocalTimeServer_file_list.json"


# =============================================================================


class RaspbianInstaller(object):
    def __init__(self, package_name, build_info_filepath, opt_target):
        with open(build_info_filepath, "r") as json_file:
            json_text = json_file.read()
        self.package_name = package_name
        self.build_info = json.loads(json_text)
        self.opt_target = opt_target
        return

    def install(self):
        current_folder = os.path.abspath(os.path.dirname(__file__))
        raspbian_tmp = os.path.join(current_folder, "raspbian_tmp")
        shutil.rmtree(raspbian_tmp, ignore_errors=True)
        src_folder = os.path.abspath(os.path.join(current_folder, f'../{self.package_name}'))
        deployment_dir = self.build_info["install_prefix_path"][1:]
        lts_target_folder = os.path.join(raspbian_tmp, deployment_dir)

        for this_file in self.build_info["app_files"]:
            src_file = os.path.abspath(os.path.join(src_folder, this_file))
            dest_file = os.path.abspath(os.path.join(lts_target_folder, this_file))
            dest_folder = os.path.dirname(dest_file)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            shutil.copy(src_file, dest_file)

        # copy raspbian_tmp to destination
        dest_path = os.path.join("opt", self.opt_target)
        shutil.copytree(raspbian_tmp, dest_path)

        # copy systemd service to /lib/systemd/system
        raspbian_template = os.path.join(current_folder, f"raspbian_{self.package_name}")
        service_filepath = os.path.join(raspbian_template, f"{self.package_name}.service")
        dest_path = os.path.join("lib", "systemd", "system")
        shutil.copy(service_filepath, dest_path)

        shutil.rmtree(raspbian_tmp, ignore_errors=True)
        return


# =============================================================================


def arg_parser():
    """
    parse arguments

    :return: the parsed command line arguments
    """
    parser = argparse.ArgumentParser(description="installs LocalTimeServer into Raspbian", add_help=False)
    parser.add_argument("-?", "--help", help="show help message and quit", action="help")
    args = parser.parse_args()
    return args


def main():
    _ = arg_parser()
    try:
        installer = RaspbianInstaller("LocalTimeServer", BUILD_INFO_FILEPATH, "damco")
        installer.install()
    except Exception as ex:
        print(f"Error: {ex}")
    return


if __name__ == '__main__':
    main()
