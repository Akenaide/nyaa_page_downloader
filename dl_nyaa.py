#!/usr/bin/python3

__author__ = 'KMS'

# -----------------------------------------------------------------------------
#   Imports
# -----------------------------------------------------------------------------
import click
import os
from urllib.request import urlopen, urlretrieve
import uuid
from html.parser import HTMLParser

# -----------------------------------------------------------------------------
#   Globals
# -----------------------------------------------------------------------------


class MyHTMLParser(HTMLParser):
    def __init__(self):
      super().__init__(self)
      self.file_link_dict = dict()

    def handle_starttag(self, tag, attrs):
        # print("tag %r \n attrs %r" % (tag, attrs))
        title = ('title', 'Download')
        if tag == "a":
            if title in attrs:
                for attr_name, attr_value in attrs:
                    if attr_name == 'href':
                        self.file_link_dict["%s.torrent" % str(uuid.uuid4())] = attr_value
                        print(attr_value)

    def get_link_dict(self):
      return self.file_link_dict

# -----------------------------------------------------------------------------
#   Main
#------------------------------------------------------------------------------

def download_file(file_link_dict):
  """ Take a list and download items then run each downloaded file
  """
  for key, link in file_link_dict.items():
    fname = os.path.join(os.path.expandvars("%TEMP%"), key)
    urlretrieve(link, fname)
    os.startfile(fname)

@click.command()
@click.option('-f', '--file-name', 'lc_file_name', default='nyaa.html', help="give Html file")
@click.option('-u', '--url', 'lc_url', default=None, help="give url")
@click.option('-d', '--download', 'download', default=False, is_flag=True, help="want to download directly")
def main(lc_file_name, lc_url, download):
    if lc_url is None:
        with open(lc_file_name, 'r') as f:
            html_text = "".join(f.readlines())
    else:
        request = urlopen(lc_url)
        html_text = str(request.readlines())

    html_parser = MyHTMLParser()

    file_link_dict = html_parser.feed(html_text)

    if download:
      download_file(html_parser.get_link_dict())

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------
#    End of file
#------------------------------------------------------------------------------
