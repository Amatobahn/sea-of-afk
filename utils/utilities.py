import sys
import subprocess

import enum


class OperatingSystem(enum.Enum):
    WINDOWS = 0
    LINUX = 1
    MACOS = 2


def operating_system():
    if sys.platform in ["linux", "linux2"]:
        return OperatingSystem.LINUX
    elif sys.platform == "darwin":
        return OperatingSystem.MACOS
    elif sys.platform == "win32":
        return OperatingSystem.WINDOWS


def is_linux():
    return operating_system().name == "LINUX"


def is_macos():
    return operating_system().name == "MACOS"


def is_unix():
    return operating_system().name in ["LINUX", "MACOS"]


def is_windows():
    return operating_system().name == "WINDOWS"


def clear_terminal():
    if is_unix():
        print("\033c")
    elif is_windows():
        subprocess.call(["cls"], shell=True)
