#!/usr/bin/python3
import argparse
import os
import configurations
import json
import utilities

config_file        = "config.json"
conf               = json.load(open(config_file))
configs            = conf["cli_config"]
cppversion         = configs["cppversion"]
debug              = configs["debug"]
display_author     = configs["display_author"]

# ------------Create the parser-----------------------------
root_parser = argparse.ArgumentParser(
    description = 'Command line tool for competitive programming')

root_parser.add_argument("--version",
                    action = "version", 
                    version = "%(prog)s 2.1.171.3")
root_parser.add_argument("--solve",
                    action = solve,)
root_parser.add_argument("--test",
                    action = test,)

# ------------modes supported-------------------------------

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
					nargs = 0, 
                    action = fetch_problems)



overloads = config_parser.parse_args()
cppversion         = overloads.cppversion
debug              = overloads.debug
display_author     = overloads.autdet
configs["cppversion"]     = cppversion
configs["debug"]          = debug              
configs["display_author"] = display_author
with open("config.json", "w") as jsonFile:
    json.dump(conf, jsonFile)



# add arguments to the modes

root_parser.parse_args()