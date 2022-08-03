import time
from datetime import date
import json
from configurations import *

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