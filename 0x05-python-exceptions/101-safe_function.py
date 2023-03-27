#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return(fct(*args))
    except Exception as identifier:
        print("Exception: {}".format(identifier), file=sys.stderr)
        return(None)
