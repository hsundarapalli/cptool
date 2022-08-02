#!/usr/bin/python3
import argparse
import os
import configurations
import json
from utilities import *


config_file        = "config.json"
conf               = json.load(open(config_file))
configs            = conf["cli_config"]
cppversion         = configs["cppversion"]
debug              = configs["debug"]
display_author     = configs["display_author"]
author_name        = configs["author_name"]

# ------------Create the parser-----------------------------
root_parser = argparse.ArgumentParser(
    description = 'Command line tool for competitive programming')

root_parser.add_argument("--version",
                    action = "version", 
                    version = "%(prog)s 2.1.171.3")
root_parser.add_argument("--open",nargs=0,
                    action = make_action(open_file))
root_parser.add_argument("--test",
                    ) #problem_letter + '.cpp'

# ------------modes supported-------------------------------
mode = root_parser.add_subparsers(
                    title = "mode of operation")
#setup/ config mode
config_parser = mode.add_parser("config",
                    parents = [root_parser], 
                    description = 'Customize your configurations', 
                    add_help = False)

#contest mode
contest_parser = mode.add_parser("contest",
                    parents = [root_parser], 
                    description = 'Entered the contest mode', 
                    add_help = False)
# contains fetch, submit


#----------------------------------------------------------
#setup/ config mode
config_parser.add_argument("--username", 
                    default = author_name, 
                    help = "Tell me your name !!")
config_parser.add_argument("--cppversion", 
                    choices = ["c++20", "c++14", "c++17", "c++11"], 
                    default = cppversion, 
                    help = "select the version of the c++ compiler")
config_parser.add_argument("--debug", 
                    choices = ["true", "false"], 
                    default = debug, 
                    help = "enable or disable debug mode")
config_parser.add_argument("--autdet", 
                    choices = ["true", "false"], 
                    default = display_author, 
                    help = "enable or disable author details")

contest_parser.add_argument("contest_number", 
					type = int,
					nargs = 1, 
                    help = "enter the contest number")
contest_parser.add_argument("fetch", 
                    )#action = FooAction



overloads = config_parser.parse_args()
cppversion         = overloads.cppversion
debug              = overloads.debug
display_author     = overloads.autdet
author_name        = overloads.username
configs["cppversion"]     = cppversion
configs["debug"]          = debug              
configs["display_author"] = display_author
configs["author_name"]    = author_name
with open("config.json", "w") as jsonFile:
    json.dump(conf, jsonFile)



# add arguments to the modes

