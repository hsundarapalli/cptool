import argparse
import os
import json
from colors import *
from test_editor_loader import *
from configurations import *

#------------tempconfig-----------------
test_num_file   = "test_num.json"
test_num        = json.load(open(test_num_file))


def open_file(values):
    problem_letter = values[0]
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

def test(values):
    problem_letter = values[0]
    file_name      = problem_letter + '.cpp'
    tests_num      = int(test_num[problem_letter])
    # compile the source code
    os.system("g++ " + file_name)
    run_tests(tests_num, problem_letter)

def fetch(values):
    update_contest_details("contest_number", values[0])
    os.system("python3 fetch.py")

    

def make_action(fun, *args, **kwargs):
    class customAction(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            fun(values)
            setattr(args, self.dest, values)
    return customAction