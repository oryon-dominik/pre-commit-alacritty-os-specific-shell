#!/usr/bin/env python
# coding: utf-8

"""This hook sets alacritty shell.program os-specific. Usecase: cross-os dotfiles repos."""

__version__ = '1.0.0'


import argparse
import logging
import platform
import yaml

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
                stream = file.read()
                alacritty_config = yaml.safe_load(stream)
                
                # MATCH
                match platform.system():
                        case "Windows":
                            alacritty_config['shell']['program'] = args.windows or 'C:/Program Files/PowerShell/7/pwsh.exe'
                        case _:  # pretend it's posix for all other cases
                            alacritty_config['shell']['program'] = args.posix or '/bin/fish'

            # WRITE
            with open(path, 'w') as file:
                yaml.dump(alacritty_config, file)

        else:
            log.error(f"File {filename} does not exist.")
