import os
import re
import pytest


class InvalidSuffixError(Exception):
    pass


def find_files(suffix, start_dir):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      start_dir(str): starting path of the file system to traverse

    Returns:
       a list of paths
    """
    if not re.match(r'\.[a-zA-Z0-9]+$', suffix):
        raise InvalidSuffixError('You must provide a valid suffix which starts with a period and follows with'
                                 'alphanumeric characters.')
    result = []

    def traverse(path):
        files = os.listdir(path)

        for file in files:
            name = path + os.path.sep + file
            if os.path.isdir(name):
                traverse(name)
            elif name.endswith(suffix):
                result.append(name)

    traverse(start_dir)

    return result


def test_find_files():
    result = find_files('.c', './testdir')
    assert result.sort() == ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c',
                             './testdir/subdir5/a.c', './testdir/t1.c'].sort()

def test_find_files_with_bad_start_name():
    with pytest.raises(FileNotFoundError):
        find_files('.c', './some_bad_dir_name')

def test_find_files_with_bad_suffix():
    with pytest.raises(InvalidSuffixError):
        find_files('._some_BAD_F1L3_EXT3NSION', './testdir')