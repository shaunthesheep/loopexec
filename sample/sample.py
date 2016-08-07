#!/usr/bin/python
from loopexec import ExecChecker
from time import sleep


def main():
    the_list = range(100)

    # checker initialization
    ec = ExecChecker(len(the_list))
    for _ in the_list:

        # operations inside the loop
        sleep(.3)

        # checker update at the end of the loop
        ec.update()


if __name__ == "__main__":
    main()
