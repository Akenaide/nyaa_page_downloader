__author__ = 'KMS'

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print("tag %r \n attrs %r" % (tag, attrs))
        title = ('title', 'Download')
        if tag == "a":
            if title in attrs:
                for attr_name, attr_value in attrs:
                    if attr_name == 'href':
                        print(attr_value)


def main():
    fname = "file.htm"
    with open(fname, 'r', encoding='utf-8') as f:
        fname_text = "".join(f.readlines())
    parser = MyHTMLParser()
    parser.feed(fname_text)

if __name__ == "__main__":
    main()