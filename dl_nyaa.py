#!/usr/bin/env python
__author__ = 'KMS'
from __future__ import absolute_import

# -----------------------------------------------------------------------------
#   Imports
# -----------------------------------------------------------------------------
import argparse
import sys
from html.parser import HTMLParser

# -----------------------------------------------------------------------------
#   Globals
# -----------------------------------------------------------------------------

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print("tag %r \n attrs %r" % (tag, attrs))
        title = ('title', 'Download')
        if tag == "a":
            if title in attrs:
                for attr_name, attr_value in attrs:
                    if attr_name == 'href':
                        print(attr_value)


def mk_parser():
    """ commandline parser """
    parser = argparse.ArgumentParser(description= "Take a nyaa.se page and download torrents in this page")
    #parser.add_argument('--verbose', '-v', action='store_true', default=False)
    parser.add_argument('--no-verify', '-n', action='store_true', default=False)
    #parser.add_argument('offset', type=int, nargs='?', default=0)
    return parser
# -----------------------------------------------------------------------------
#   Main
#------------------------------------------------------------------------------


def main():
    args = sys.argv[1:]
    parser = mk_parser()
    options = parser.parse_args(args)
    fname = "file.htm"
    with open(fname, 'r', encoding='utf-8') as f:
        fname_text = "".join(f.readlines())
    parser = MyHTMLParser()
    parser.feed(fname_text)

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
#    End of file
#------------------------------------------------------------------------------