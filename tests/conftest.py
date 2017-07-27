"""Integration tests configuration file."""
import os

from PerformanceAndroid.tests.conftest import pytest_configure  # pylint: disable=unused-import


def test1():
    PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    return PATH




if __name__=='__main__':
    print(test1())