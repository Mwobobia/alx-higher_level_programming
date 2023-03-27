#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as identifier:
        print("Exception: {}".format(identifier), file=sys.stderr)
        return False
    return True
