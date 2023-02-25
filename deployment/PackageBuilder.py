import json
import os
import shutil


class PackageBuilder:
    def __init__(self, package_name, build__info_filepath, version):
        with open(build__info_filepath, "r") as json_file:
            json_text = json_file.read()
        self.package_name = package_name
        self.build_info = json.loads(json_text)
        self.version = version
        return

    def build_debian(self):
        """
        build the package
        """
        current_folder = os.path.abspath(os.path.dirname(__file__))
        deb_folder = os.path.join(current_folder, "deb_tmp")
        shutil.rmtree(deb_folder, ignore_errors=True)
        template_folder = os.path.join(current_folder, f"deb_{self.package_name}")
        shutil.copytree(template_folder, deb_folder)
        control_file = os.path.join(deb_folder, "DEBIAN/control")
        version_cmd = r'sed -i s/\<version>\>/{}/g {}'.format(self.version, control_file)
        os.system(version_cmd)
        src_folder = os.path.abspath(os.path.join(current_folder, f'../{self.package_name}'))
        deployment_dir = self.build_info["install_prefix_path"][1:]
        lts_target_folder = os.path.join(deb_folder, deployment_dir)

        for this_file in self.build_info["app_files"]:
            src_file = os.path.abspath(os.path.join(src_folder, this_file))
            dest_file = os.path.abspath(os.path.join(lts_target_folder, this_file))
            dest_folder = os.path.dirname(dest_file)
            if not os.path.exists(dest_file):
                os.makedirs(dest_folder)
            shutil.copy(src_file, dest_file)

        pkg_cmd = f"dpkg -b {deb_folder} {self.package_name}-{self.version}.deb"
        os.system(pkg_cmd)
        shutil.rmtree(deb_folder, ignore_errors=True)
        return
