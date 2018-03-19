import sys
import argparse
from odps import parse
from odps import transform
from odps import insert


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("-d", "--download", action="store_true", help="execute download.py...")
    # parser.add_argument("-p", "--parse", action="store_true", help="execute parse.py...")
    # parser.add_argument("-c", "--convert", action="store_true", help="execute transform.py...")
    # parser.add_argument("-i", "--insert", action="store_true", help="execute insert.py...")
    parser.add_argument("-e", "--env", help="get prod.conf...")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        data_list = parse.parse([-1])
        value_list = transform.transform(data_list)
        insert.insert(value_list, "test")
    elif len(sys.argv) == 3:
        data_list = parse.parse([-1])
        value_list = transform.transform(data_list)
        insert.insert(value_list, args.env)
    else:
        print("error param!")
        sys.exit(1)
    # if args.parse:
    #     subprocess.call("python3 parse.py", shell=True)
    # if args.convert:
    #     subprocess.call("python3 transform.py", shell=True)
    # if args.insert:
    #     subprocess.call("python3 insert.py", shell=True)


if __name__ == '__main__':
    main()