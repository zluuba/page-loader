import argparse
import os


def parse_args():
    default_path = os.getcwd()
    parser = argparse.ArgumentParser(
        prog='page-loader',
        description='Download web pages and save them to the local drive'
    )
    parser.add_argument('url')
    parser.add_argument('-o', '--output',
                        help=f"output directory (default: '{default_path}')",
                        default=default_path)

    args = parser.parse_args()
    return args.url, args.output
