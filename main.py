#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os

from fileOperation import fileOperation_singleton


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def debug():
    print(fileOperation_singleton.info)

    print(os.getcwd())

    fileOperation_singleton.create_folder("tmp")

    fileOperation_singleton.create_file("tmp/test.txt")

    fileOperation_singleton.create_folder("tmp2")

    fileOperation_singleton.copy_folder("tmp", "tmp2")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('hello world')

    debug()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
