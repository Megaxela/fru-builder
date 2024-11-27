from __future__ import unicode_literals
from os import listdir
from os.path import isdir, join, splitext
from shutil import copy2, copytree

from pytest import fixture
from yaml import load, FullLoader


def copy_tree(src, dst, symlinks=False, ignore=None):
    for item in listdir(src):
        s = join(src, item)
        d = join(dst, item)
        if isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            copy2(s, d)


class StaticFixture:
    def __init__(self, tmpdir, test_dir):
        self.__tmpdir = tmpdir
        self.__test_dir = test_dir

        if isdir(self.__test_dir):
            copy_tree(self.__test_dir, str(self.__tmpdir))

    def read_file(self, filename: str, mode="r"):
        with open(join(self.__tmpdir, filename), mode=mode) as f:
            return f.read()

    def read_yaml(self, filename: str):
        return load(self.read_file(filename), Loader=FullLoader)


@fixture
def static(tmpdir, request):
    """
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.
    """
    filename = request.module.__file__
    test_dir, _ = splitext(filename)

    return StaticFixture(tmpdir=tmpdir, test_dir=test_dir)
