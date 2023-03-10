from page_loader.core import download
from page_loader import parser
import page_loader.validator
import sys


def main():
    try:
        url, output = parser.parse_args()
        saved_page_path = download(url, output)
        print(f"Page was downloaded as '{saved_page_path}'")
        sys.exit(0)
    except page_loader.validator.AppError as error:
        print(f"Sorry, but app cannot run, error: {error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
