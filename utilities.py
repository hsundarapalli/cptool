import argparse
import os
import json
import time
from datetime import date

config_file        = "config.json"
conf               = json.load(open(config_file))
configs            = conf["cli_config"]
display_author     = configs["display_author"]
debug              = configs["debug"]
author_name        = configs["author_name"]
    
def add_author(file):
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    today     = date.today() 
    curr_date = today.strftime("%d.%m.%Y")
    if display_author == "true" :
        file.write("/**\n")
        file.write(" *    author:  " + author_name + "\n")
        file.write(" *    created: " + curr_date + " " + curr_time + "\n")      
        file.write("**/\n")

def add_bitsstream(file):
    file.write("#include <bits/stdc++.h>\n")
    file.write("using namespace std;\n\n")

def add_debugger(file):
    if debug == "true" : 
        file.write("#ifdef LOCAL\n")
        file.write("#include " + "debug" + ".h\n")
        file.write("#else\n")
        file.write("#define debug(...) 42\n")
        file.write("#define debnl(...) 42\n")
        file.write("#endif\n")

def add_main(file):
    file.write("int main() {\n")
    file.write("\tios_base::sync_with_stdio(false);\n")
    file.write("\tcin.tie(NULL);\n\n")
    file.write("}\n")

def open_file():
    problem_letter = input("enter the problem letter: ")
    file_name      = problem_letter + '.cpp'
    with open(file_name, 'w') as file:
        add_author(file)
        add_bitsstream(file)
        add_debugger(file)
        add_main(file)
    os.system("subl "+file_name) 

def make_action(fun, *args, **kwargs):
    class customAction(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            print(args)
            fun()
            setattr(args, self.dest, values)
    return customAction