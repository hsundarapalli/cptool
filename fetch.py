#!/usr/bin/python3
from urllib.request import urlopen
import sys
import json
from parser import html_parser

# try to get the html file first
config_file        = "config.json"
conf               = json.load(open(config_file))
configs            = conf["contest_details"]
online_judge       = configs["online_judge"]
contest_number     = configs["contest_number"]

temp_file          = "temp.json"

with open(temp_file, "w") as f:
	f.write("{\n")
	problem_letter = 'A'
	while True :
		url = 'http://codeforces.com/contest/' + contest_number + '/problem/' + problem_letter
		problem = urlopen(url)
		if problem.geturl() != url:
			break
		text = problem.read()
		parser = html_parser(problem_letter);
		parser.feed(text.decode('utf-8'))
		assert len(parser.sample_inputs) == len(parser.sample_outputs)
		f.write('"' + problem_letter +'"'+ ": " + str(parser.no_of_sample_tests) + ",\n")
		parser.generate_test_files()
		problem_letter = chr(ord(problem_letter)+1)
	f.write("\n}")

