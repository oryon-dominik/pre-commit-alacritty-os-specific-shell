#!/usr/bin/env python
# coding: utf-8

"""This hook sets alacritty shell.program os-specific. Usecase: cross-os dotfiles repos."""

__version__ = '1.0.0'


import argparse
import platform
import yaml


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    # TODO: add paths with args..
    # parser.add_argument('--windows', action='store_true', dest='windows', default=True)
    # parser.add_argument('--posix', action='store_true', dest='posix', default=False)
    args = parser.parse_args(argv)


    for file in args.filenames:
        with open(file, 'wb') as stream:
            alacritty_config = yaml.safe_load(stream)
            match platform.system():
                case "Windows":
                    alacritty_config['shell']['program'] = 'C:/Program Files/PowerShell/7/pwsh.exe'
                case _:  # pretend it's posix for all other cases
                    alacritty_config['shell']['program'] = '/bin/fish'

    print("Debug hook!", platform.system())
