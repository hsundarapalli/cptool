"""
Parse configuration file 
"""
import json

# cppversion": "c++17", "debug": "false", "display_author": "true", "author_name": 

config_file        = "config.json"
conf               = json.load(open(config_file))

cpm_conf            = conf["cpm_conf"]
contest_details    = conf["contest_details"]
test_case_num       = conf["test_case_num"]

cppversion        = cpm_conf["cppversion"]
debug              = cpm_conf["debug"]
display_author     = cpm_conf["display_author"]
author_name        = cpm_conf["author_name"] 
text_editor        = cpm_conf["text_editor"]

online_judge       = contest_details["online_judge"]
contest_number     = contest_details["contest_number"]

def update_json():
    with open(config_file, "w") as outfile:
        json.dump(conf, outfile)    

def update_cpm_conf(key, val):
    conf["cpm_conf"][key] = val
    update_json()

def update_contest_details(key, val):
    conf["contest_details"][key] = val
    update_json()

def update_test_case_num(key, val):
    conf["test_case_num"][key] = val
    update_json()
