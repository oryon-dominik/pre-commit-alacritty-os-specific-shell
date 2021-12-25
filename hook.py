#!/usr/bin/env python
# coding: utf-8

"""This hook sets alacritty shell.program os-specific. Usecase: cross-os dotfiles repos."""

__version__ = '1.0.0'


import argparse
import platform

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument('--windows', action='store_true', dest='windows', default=True)
    parser.add_argument('--posix', action='store_true', dest='posix', default=False)
    args = parser.parse_args(argv)
    
    # TODO: read the alacritty.yml and switch shell.program between args.windows and args.posix depending on the detected os
    # program: 'C:\Program Files\PowerShell\7\pwsh.exe'
    # program: /bin/fish
    # winpty_backend: true

    print("Debug hook!", platform.system(), args)
