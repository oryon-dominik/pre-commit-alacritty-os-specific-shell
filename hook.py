#!/usr/bin/env python
# coding: utf-8

import argparse


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--windows', action='store_true', dest='windows', default=True)
    parser.add_argument('--posix', action='store_true', dest='posix', default=False)
    args = parser.parse_args(argv)
    print("Debug hook!", args)
