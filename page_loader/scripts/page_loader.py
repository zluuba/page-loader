from page_loader.core import download
from page_loader import parser


def main():
    url, output = parser.parse_args()
    return download(url, output)


if __name__ == '__main__':
    main()
