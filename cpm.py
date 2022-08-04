#!/usr/bin/python3
import argparse
import os
import configurations
import json
from utilities import *
from configurations import *

# ------------Create the parser-----------------------------
root_parser = argparse.ArgumentParser(
    description = 'Command line tool for competitive programming')

root_parser.add_argument("--version",
                    action = "version", 
                    version = "%(prog)s 2.1.171.3")
root_parser.add_argument('--open', 
                    nargs = 1,
                    action = make_action(open_file))
root_parser.add_argument("--test",
                    nargs = 1,
                    action = make_action(test))
root_parser.add_argument("--run",
                    nargs = 1,
                    action = make_action(run))  
root_parser.add_argument("--username", 
                    nargs = 0,
                    action = make_action(get_username))
root_parser.add_argument("--cppversion",
                    nargs = 0,
                    action = make_action(get_cppversion)) 
# adding sub_parsers 
sub_parsers = root_parser.add_subparsers(
                    help = "mode of operation")
#----------- modes supported ----------------------
#setup/ config mode
config_parser = sub_parsers.add_parser("config",
                    help = "Configure cpm")
#contest mode
contest_parser = sub_parsers.add_parser("contest",
                    help = "Entering Contest mode")
# ------------------------------------------------
#add elements to subparsers

config_parser.add_argument("--username", 
                    nargs  =1,
                    action = make_action(update_username), 
                    help = "enable or disable debug mode")
config_parser.add_argument("--cppversion", 
                    nargs = 1,
                    choices = ["c++20", "c++14", "c++17", "c++11"], 
                    action = make_action(update_cppversion),
                    help = "choose the version of the cpp compiler")
config_parser.add_argument("--debug", 
                    nargs = 1,
                    choices = ["true", "false"], 
                    action = make_action(update_debug), 
                    help = "enable or disable debug mode")
config_parser.add_argument("--autdet",
                    nargs =1, 
                    choices = ["true", "false"], 
                    action = make_action(update_author_config),
                    help = "enable or disable author details")
config_parser.add_argument("--txteditor",
                    nargs =1, 
                    action = make_action(update_text_editor),
                    help = "update your defualt text editor for cpm")
#----------------------------------------------------------


contest_parser.add_argument("--fetch", 
                    nargs = 1,
                    action = make_action(fetch))

#--------------------------------------------------------
root_parser.parse_args()

