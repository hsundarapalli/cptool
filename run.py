#!/usr/bin/python3
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
