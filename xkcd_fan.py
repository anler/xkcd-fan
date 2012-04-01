"Fetch a random image from xkcd website"
import sys
import os
import re
import argparse
import mimetypes
import urllib.request

COMIC_REGEXP = re.compile('id="comic">\s*<img src="([^"]+)" '\
                          'title="([^"]+)" alt="([^"]+)"')
RANDOM_COMIC_URL = "http://dynamic.xkcd.com/random/comic/"



def get_page(url):
    """Returns the content of the requested url as unicode"""
    response = urllib.request.urlopen(url)
    charset = response.info().get_content_charset()
    page = response.read().decode(charset)

    return page


def random_comic():
    """Returns the url of a random comic"""
    comic_url = comic_title = comic_alt = None
    page = get_page(RANDOM_COMIC_URL)
    match = COMIC_REGEXP.search(page)
    if match:
        comic_url, comic_title, comic_alt = match.groups()

    return comic_url, comic_title, comic_alt


def get_comic(url):
    """Fetches the comic image behind a url

    Returns a tuple where elements are (image, mime-type)
    """
    response = urllib.request.urlopen(url)
    mimetype = response.getheader('content-type')
    image = response.read()

    return image, mimetype


def save_random_comic(dest):
    """Downloads the comic and saves it in dest"""
    url, title, alt = random_comic()
    image, mimetype = get_comic(url)
    extension = mimetypes.guess_extension(mimetype) or ""
    filename = os.path.join(dest, alt + extension)
    with open(filename, "wb") as f:
        f.write(image)


def main():
    def valid_directory(path):
        if not os.path.isdir(path):
            msg = "%r is not an existing directory" % path
            raise argparse.ArgumentTypeError(msg)
        return path

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dest", type=valid_directory,
                        help="Destination directory")
    args = parser.parse_args()

    save_random_comic(args.dest)


if __name__ == '__main__':
    sys.exit(main())
