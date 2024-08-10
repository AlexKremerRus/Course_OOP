#!/usr/bin/python3
import argparse
import sys

# print(sys.argv)

def my_sum(a, b):
    return a + b

def my_sub(a, b):
    return a - b


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Python example script")

    parser.add_argument('first_int', type=float)
    parser.add_argument('action', type=str, choices=['+', '-'])
    parser.add_argument('second_int', type=float)


    argv = parser.parse_args()
    # print(argv)
    # print(argv.first_int)


    if argv.action == '+':
        print(my_sum(argv.first_int, argv.second_int))
    elif argv.action == '-':
        print(my_sub(argv.first_int, argv.second_int))