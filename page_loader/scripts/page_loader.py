from page_loader.core import download
from page_loader import parser
# import sys


def main():
    url, output = parser.parse_args()
    # try:
    saved_page_path = download(url, output)
    print(f"Page was downloaded as '{saved_page_path}'")
    # except SomeError:             # define hand-made error
    #     sys.exit("Sorry, but app cannot run, error: {error}")


if __name__ == '__main__':
    main()
