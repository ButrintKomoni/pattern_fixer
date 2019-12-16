import string, argparse, sys

def pattern_create():
    parser = argparse.ArgumentParser(description='Pattern Fixer')
    parser.add_argument('-l', '--length', help='The specific length of the pattern', type=int)
    args = parser.parse_args()
    length = args.length

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    for i in range(1):
        pattern = ""
        
        for x in list(string.digits):
            for y in list(string.uppercase):
                for z in list(string.lowercase):
                    pattern = pattern + str(x) + str(y) + str(z)
        print pattern[:int(length)]

if __name__ in "__main__":
    pattern_create()
