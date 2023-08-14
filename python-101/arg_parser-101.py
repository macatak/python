#!/usr/bin/python3

'''
example command
python3 arg_parser-101.py  1 foo test_me

REQUIREMENTS
    Python3
'''

import argparse, sys

# argument parser
parser = argparse.ArgumentParser(description="Generic message displayed with the '-h' switch")

# add arguments
# format is parser.add_argument("<argument name>", help="<help message to display>")
parser.add_argument("arg1", help="This is help for argument 1")
parser.add_argument("arg2", help="This is help for argument 2")
parser.add_argument("arg3", help="This is help for argument 3")

# get the arguments
args = parser.parse_args()

# access the arguments
# format is args.<argument name>
print("argument 1 : {}".format(args.arg1))
print("argument 2 : {}".format(args.arg2))
print("argument 3 : {}".format(args.arg3))