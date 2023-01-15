#!/usr/bin/python3
if __name__ == "__main__":
    """print the sum of all arguments."""

    import sys

    args = sys.argv[1:]
    result = sum(int(arg) for arg in args)
    print(result)
