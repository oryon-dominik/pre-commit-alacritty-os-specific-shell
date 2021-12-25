#!/usr/bin/env python
# coding: utf-8

"""This hook sets alacritty shell.program os-specific. Usecase: cross-os dotfile repos."""

__version__ = '1.0.0'


import argparse
import logging
import platform

from pathlib import Path


logging.basicConfig(format='{asctime} - {name} - {levelname} {message}', style='{', level=logging.DEBUG)
log = logging.getLogger(__name__)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    parser.add_argument('--windows', dest='windows', default="")
    parser.add_argument('--posix', dest='posix', default="")
    args = parser.parse_args(argv)

    log.debug(f'args: WINDOWS: {args.windows} POSIX: {args.posix}')

    for filename in args.filenames:
        path = Path(filename)
        if path.exists():
            log.debug(f"Processing File {filename}.")

            # READ
            with open(path, 'r') as file:
                lines = file.readlines()
                for ix, line in enumerate(lines):
                    if line.startswith('  program: '):
                        match platform.system():
                            case "Windows":
                                windows = args.windows or 'C:/Program Files/PowerShell/7/pwsh.exe'
                                lines[ix] = f"  program: '{windows}'\n"
                            case _:  # pretend it's posix for all other cases
                                posix = args.posix or '/bin/fish'
                                lines[ix] = f"  program: '{posix}'\n"

            with open(path, 'w', newline='\n') as file:
                file.writelines(lines)

        else:
            log.error(f"File {filename} does not exist.")
