#!/usr/bin/python3
import argparse
from utilities import *

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')

parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('--bar', type=int, help='bar help')

parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

parser_a.add_argument("test", 
                    nargs = 2,
                    action = make_action(dum))

args = parser.parse_args()