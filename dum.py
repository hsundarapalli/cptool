# myls.py
# Import the argparse library
import argparse

import os
import sys

# Create the parser
parser = argparse.ArgumentParser(description='List the content of a folder')

# add an argument
parser.add_argument("posarg", type = int);
parser.add_argument("-f", "--foo");
print(parser.parse_args());
print(parser.parse_args().foo)