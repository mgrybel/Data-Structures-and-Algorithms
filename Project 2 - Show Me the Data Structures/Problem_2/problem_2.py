# Problem 2: File Recursion

import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if os.path.isfile(path) and suffix in path:
        return [path]
    elif os.path.isdir(path):
        result = []
        for directory in os.listdir(path):
          files = find_files(suffix, os.path.join(path, directory))
          if files is not None:
            result += files
        return result


# Test cases

print("Find all files and all directories under the testdir directory:")
print(find_files('', 'testdir'))

print("\nFind all directories under the testdir directory and all files beneath it that end with '.c':")
print(find_files('.c', 'testdir'))

print("\nAn empty directory")
print(find_files('.c', 'testdir/subdir4'))

print("\nA non-existent directory")
print(find_files('.c', 'abcd'))

print("\nA non-existent suffix")
print(find_files('.xyz', 'testdir'))

print("\nThe inputted path is a file that has the required suffix - '.h'")
print(find_files('.h', 't1.h'))

print("\nThe inputted path is a file that has the required suffix - '.h'")
print(find_files('.h', 'testdir/t1.h'))