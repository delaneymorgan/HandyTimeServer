# HandyTimeServer
A simple handy time server

## Usage:

```shell
HandyTimeServer [-l <listener>] -p <port> [--version] [-?]
```

The server will answer queries from the specified listener on the specified port with the current local time in JSON format.
Specify 127.0.0.1 for only listeners inside the same machine as the server.
Otherwise, the default is 0.0.0.0, for all listeners.

Enter the -? option to view command-line options.

For instance:

```shell
HandyTimeServer -p 10123
```

... and in a browser, enter:

    http://<HandyTimeServer Host>:10123/

It should return something like this:

```json
{"local": {"year": 2023, "month": 4, "dom": 29, "hour": 11, "min": 53, "sec": 34, "dow": 5, "doy": 119, "is_dst": 0}, "utc": {"year": 2023, "month": 4, "dom": 29, "hour": 1, "min": 53, "sec": 34, "dow": 5, "doy": 119, "is_dst": 0}, "tick": 1682733214.5565424, "tz": {"name": "AEST", "offset": 36000}}
```

## Building Python Package:

You may need to install virtual environment support for your python version:

```shell
sudo apt install python<X.X>-venv
```

...where X.X is the python version on your system.
i.e. python3.10 would be python3.10-venv.
Note that HandyTimeServer requires Python 3.6 or later.

From this directory:

```shell
python3 build .
```

To install the built package:

```shell
pip3 install ./dist/HandyTimeServer-<VERSION>-py3-none-any.whl --force-reinstall
```

...where VERSION is the version of HandyTimeServer you have just built (see version.py).
This will install HandyTimeServer just for the current user in .local/bin.
To install system-wide, use sudo.

## Building Debian package

Firstly, install pre-requisites:

```shell
sudo apt install build-essential binutils lintian debhelper dh-make devscripts
```

from the deployment folder, run:

```shell
./build_deb_package.py -v <version>
```

...where version is in a <major>.<minor>.<maintenance> format.
The produced package will have the form:

    HandyTimeServer-<version>.deb

## Installing into OS

Ubuntu/Debian:

```shell
sudo dpkg -i HandyTimerServer-<version>.deb
```

Raspbian:

```shell
sudo ./install_on_raspbian.py
```

## Updating Version#:

The version number is kept here:

    ./HandyTimeServer/version.py
