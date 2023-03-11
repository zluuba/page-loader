from page_loader.core import download
from page_loader.log import get_logger
from page_loader import parser
import page_loader.core
import sys


logger = get_logger(__name__)


def main():
    try:
        url, output = parser.parse_args()
        saved_page_path = download(url, output)
        print(f"Page was downloaded as '{saved_page_path}'")
        sys.exit(0)
    except (Exception, page_loader.core.AppError) as error:
        print(f"Sorry, but app cannot run, error: {error}")
        sys.exit(1)


if __name__ == '__main__':
    main()
