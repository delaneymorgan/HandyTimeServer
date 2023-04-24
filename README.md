# LocalTimeServer
A simple local time server

## Usage:

    LocalTimeServer [-l <listener>] -p <port> [--version] [-?]

The server will answer queries from the specified listener on the specified port with the current local time in JSON format.
Specify 127.0.0.1 for only listeners inside the same machine as the server.
Otherwise, the default is 0.0.0.0, for all listeners.

Enter the -? option to view command-line options.

For instance:

    LocalTimeServer -p 10123

... and in a browser, enter:

    http://<LocalTimeServer Host>:10123/

It should return something like this:

    {"year": 2023, "month": 4, "dom": 25, "hour": 8, "min": 34, "sec": 16, "dow": 1, "doy": 115, "is_dst": 0, "tick": 1682375656.844505}

## Building Python Package:

You may need to install virtual environment support for your python version:

    sudo apt install python<X.X>-venv

...where X.X is the python version on your system.
i.e. python3.10 would be python3.10-venv.
Note that LocalTimeServer requires Python 3.6 or later.

From this directory:

    python3 build .

To install the built package:

    pip3 install ./dist/LocalTimeServer-<VERSION>-py3-none-any.whl --force-reinstall

...where VERSION is the version of LocalTimeServer you have just built (see version.py).
This will install LocalTimeServer just for the current user in .local/bin.
To install system-wide, use sudo.

## Building Debian package

Firstly, install pre-requisites:

    sudo apt install build-essential binutils lintian debhelper dh-make devscripts

from the deployment folder, run:

    ./build_deb_package.py -v <version>

...where version is in a <major>.<minor>.<maintenance> format.
The produced package will have the form:

    LocalTimeServer-<version>.deb

## Installing into OS

Ubuntu/Debian:

    sudo dpkg -i LocalTimerServer-<version>.deb

Raspbian:

    sudo ./install_on_raspbian.py

## Updating Version#:

The version number is kept here:

    ./LocalTimeServer/version.py
