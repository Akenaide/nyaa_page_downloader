#!/usr/bin/python3

__author__ = 'KMS'

# -----------------------------------------------------------------------------
#   Imports
# -----------------------------------------------------------------------------
import click
import urllib
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

# -----------------------------------------------------------------------------
#   Main
#------------------------------------------------------------------------------

@click.command()
@click.option('-f', '--file-name', 'lc_file_name', default='nyaa.html', help="give Html file")
@click.option('-u', '--url', 'lc_url', default=None, help="give url")
def main(lc_file_name, lc_url):
    if lc_url is None:
        with open(lc_file_name, 'r') as f:
            html_text = "".join(f.readlines())
    else:
        request = urllib.request.urlopen(lc_url)
        html_text = str(request.readlines())

    html_parser = MyHTMLParser()
    html_parser.feed(html_text)

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
#    End of file
#------------------------------------------------------------------------------