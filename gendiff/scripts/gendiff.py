import argparse
from gendiff.scripts.diff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='set format of output')
    args = parser.parse_args()
    difference = generate_diff(args.first_file, args.second_file, args.format)
    print(difference)


if __name__ == '__main__':
    main()

