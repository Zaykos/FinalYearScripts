#! /usr/bin/python3
#main function

ver = "1.0"#&

import sys
from mods import main

try:
    url = sys.argv[1]
    urlht = "http://"+url
except:
    exit()

def _main(url,urlht,ver):
    main.main(url,urlht,ver)

if __name__ == '__main__':
    _main(url,urlht,ver)
