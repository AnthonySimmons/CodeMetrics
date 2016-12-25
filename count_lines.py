# !/usr/bin/python

import sys
import os
from optparse import OptionParser

'''
Counts the number of lines of the files in the given directory.

Usage:

    python count_lines.py -d [<DirectoryPath>] -f [<FileExtension>]

    Where:

    <DirectoryPath> - (Optional) Path to the directory whose files to count. Defaults to CWD.
    <FileExtension> - (Optional) Extension of the files to include.
'''


def get_args():
    parser = OptionParser()
    parser.add_option('-d', action='store', type='string', dest='directory', default=os.getcwd())
    parser.add_option('-f', action='store', type='string', dest='file_extension')
    parser.add_option('-v', action='store_true', dest='verbose')
    (options, args) = parser.parse_args()
    return options


def validate_args(options):
    if not os.path.isdir(options.directory):
        raise Exception("Invalid option for directory")

def get_files(directory, file_ext=None, verbose=True):
    file_list = []
    get_files_list(file_list, directory, file_ext, verbose)
    return file_list


def get_files_list(file_list, directory, file_ext=None, verbose=False):

    for element in os.listdir(directory):
        if element == '.' or element == '..':
            continue
        element_full_path = os.path.join(directory, element)
        if os.path.isfile(element_full_path):
            if file_ext is None or element.lower().endswith(file_ext):
                if verbose is True:
                    print(element_full_path)
                file_list.append(element_full_path)
        elif os.path.isdir(element_full_path):
            get_files_list(file_list, element_full_path, file_ext, verbose)


def count_lines(files, verbose=False):
    total_line_count = 0
    for file in files:
        line_count = 0
        with open(file, mode='r') as handle:
            for line in handle:
                line_count += 1
        if verbose is True:
            print("File: %s Lines: %s" % (file, line_count))
        total_line_count += line_count
    return total_line_count


def print_results(file_list, file_extension, directory, line_count):
    print("Directory: %s" % directory)
    if file_extension is not None:
        print("File Extension: %s" % file_extension)

    print("File Count: %s" % len(file_list))
    print("Line Count: %s" % line_count)


def main():
    options = get_args()
    validate_args(options)
    files = get_files(options.directory, options.file_extension, options.verbose)
    line_count = count_lines(files, options.verbose)
    print_results(files, options.file_extension, options.directory, line_count)


if __name__ == '__main__':
    main()