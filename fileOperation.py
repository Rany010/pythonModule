#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import shutil


class FileOperation:
    def __init__(self):
        self.info = "file operation class"

    def create_folder(self, cmd):
        os.makedirs(cmd, exist_ok=True)

    def create_file(self, cmd):
        if os.path.exists(cmd):
            return
        os.mknod(cmd)

    def remove_file(self, cmd):
        os.remove(cmd)

    def remove_tree_file(self, cmd):
        shutil.rmtree(cmd, ignore_errors=True)

    def copy_file(self, src, des):
        shutil.copyfile(src, des)

    def copy_folder(self, src, des):
        shutil.copytree(src, des)

    def rename_file_folder(self, src, des):
        os.rename(src, des)


fileOperation_singleton = FileOperation()
