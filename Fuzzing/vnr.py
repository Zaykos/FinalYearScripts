#! /usr/bin/python3
# main function
import sys
from tools import main

ver = "1.0"  # &

try:
    url = sys.argv[1]
    urlht = "http://" + url
except:
    exit()


def _main(url, urlht, ver):
    main.main(url, urlht, ver)


if __name__ == '__main__':
    _main(url, urlht, ver)
