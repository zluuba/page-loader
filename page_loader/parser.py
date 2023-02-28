import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog='page-loader',
        description='Download pages from network and save them to the local drive.'
    )

    parser.add_argument('-o', '--output', help='set path for saving downloaded file',
                        default='')
    parser.add_argument('URL')

    args = parser.parse_args()
    return args.output, args.URL
