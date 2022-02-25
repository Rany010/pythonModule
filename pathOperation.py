#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import glob
import os


class PathOperation:
    def __init__(self):
        self.info = "path operation class"

    def get_file_name(self, path):
        return os.path.basename(path)

    def get_file_path(self, path):
        return os.path.dirname(path)

    def path_splicing(self, path1, path2, path3, file_name):
        return os.path.join(path1, path2, path3, file_name)

    def file_folder_exists(self, path):
        return os.path.exists(path)

    def is_file(self, path):
        return os.path.isfile(path)

    def is_folder(self, path):
        return os.path.isdir(path)

    def get_file_size(self, file_path):
        return os.path.getsize(file_path)

    def get_create_time(self, file_path):
        return os.path.getctime(file_path)

    def get_access_time(self, file_path):
        return os.path.getatime(file_path)

    def get_revise_time(self, file_path):
        return os.path.getmtime(file_path)

    def get_curr_dir(self):
        return os.getcwd()

    def set_curr_dir(self, new_path):
        return os.chdir(new_path)

    def get_all_file_path(self, recursion_path):
        all_file_path = []
        for(dir_path, dir_names, filenames) in os.walk(recursion_path):
            for fn in filenames:
                all_file_path.append(os.path.join(dir_path, fn))

        return all_file_path

    def get_all_file_path(self, path):
        all_file_path = []
        for f in os.listdir(path):
            if os.path.isdir(f):
                all_file_path.append(os.path.join(path, f))

    def get_all_file(self, path):
        all_file = []
        for f in os.listdir(path):
            if os.path.isfile(f):
                all_file.append(f)

        return all_file

    # cmd = "/home/test/*/.py"
    # cmd = "../../.png"
    def get_suffix_file_path(self, cmd):
        return glob.glob(cmd)


pathOperation_singleton = PathOperation()
