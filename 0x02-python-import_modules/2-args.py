#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total_arguments = len(argv) - 1

    if total_arguments == 0:
        print("0 arguments.")
    elif total_arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total_arguments))
    for i in range(total_arguments):
        print("{}: {}".format(i + 1, argv[i + 1]))
