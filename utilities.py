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
contest_details    = conf["contest_details"]
contest_number     = contest_details["contest_number"]
#------------tempconfig-----------------
test_num_file   = "test_num.json"
test_num        = json.load(open(test_num_file))

def prRed(skk): print("\033[1m\033[91m{}\033[00m" .format(skk))
 
 
def prGreen(skk): print("\033[1m\033[92m{}\033[00m" .format(skk))
 
 
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk))
 
 
def prLightPurple(skk): print("\033[94m{}\033[00m" .format(skk))
 
 
def prPurple(skk): print("\033[1m\033[95m{}\033[00m" .format(skk))
 
 
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk))
 
 
def prLightGray(skk): print("\033[97m{}\033[00m" .format(skk))
 
 
def prBlack(skk): print("\033[98m{}\033[00m" .format(skk))

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
    file.write("int main(){\n")
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

def cat(x):
    os.system("cat " + x)
def inout(x, y, z):
    prPurple("Input: ")
    cat(x)
    prPurple("Expected Output: ")
    cat(y)
    prPurple("Your Output: ")
    cat(z)
    print()

def run_tests(tests_num, problem_letter):
    for test_count in range(tests_num):
        output_file_name      = problem_letter + 'out.txt'
        input_file_name  = "in" + problem_letter + str(test_count + 1) + ".txt"
        os.system("./a.out < " + input_file_name + " > " + output_file_name) 
        exp_output_file_name  = "out" + problem_letter + str(test_count + 1) + ".txt"
        inout(input_file_name, exp_output_file_name, output_file_name)
        output_file = open(output_file_name, 'r')
        o = output_file.read()
        exp_output_file = open(exp_output_file_name, 'r')
        e = exp_output_file.read()
        o = o.replace("\n", " ").split()
        e = e.replace("\n", " ").split()
        if(o == e) :
            prGreen("test " + str(test_count + 1) +" case passed")
        else :
            prRed("test " + str(test_count + 1) +" case failed")
        print("\n\n")

def test():
    problem_letter = input("enter the problem letter: ")
    file_name      = problem_letter + '.cpp'
    tests_num      = int(test_num[problem_letter])
    # compile the source code
    os.system("g++ " + file_name)
    run_tests(tests_num, problem_letter)

def fetch():
    os.system("python3 fetch.py")

def set_contest_num():  
    contest_number = input("enter the problem letter: ")
    
# def reset_contest_num():
#     conf["contest_details"]["contest_number"] = contest_number1
#     with open("config.json", "w") as jsonFile:
#         json.dump(conf, jsonFile)

def make_action(fun, *args, **kwargs):
    class customAction(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            fun()
            setattr(args, self.dest, values)
    return customAction