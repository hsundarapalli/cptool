#!/usr/bin/python3
import argparse
import os
import configurations
import json
#-------programming languages-------
config_file        = "config.json"
conf               = json.load(open(config_file))
configs            = conf["cli_config"]
cppversion         = configs["cppversion"]
debug              = configs["debug"]
display_author     = configs["display_author"]
# Create the parser
root_parser = argparse.ArgumentParser(
    description = 'Command line tool for competitive programming')

# adding command line arguments 
root_parser.add_argument("--version",
                    action = "version", 
                    version = "%(prog)s 2.1.171.3")

sub_com = root_parser.add_subparsers(
                    title = "configurations")

config_parser = sub_com.add_parser("config",
                    parents = [root_parser], 
                    description = 'config_parser', 
                    add_help = False)

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

cppversion         = config_parser.parse_args().cppversion
debug              = config_parser.parse_args().debug
display_author     = config_parser.parse_args().autdet

print(debug)
configs["cppversion"]     = cppversion
configs["debug"]          = debug              
configs["display_author"] = display_author

with open("config.json", "w") as jsonFile:
    json.dump(conf, jsonFile)