#!/usr/bin/python3
from urllib.request import urlopen
import sys
import json
from parser import problem_parser

# try to get the html file first
config_file        = "config.json"
conf               = json.load(open(config_file))
configs            = conf["contest_details"]
online_judge       = configs["online_judge"]
contest_number     = configs["contest_number"][0]

temp_file          = "temp.json"

problem_letter = 'A'
while True:
	url = 'http://codeforces.com/contest/' + contest_number + '/problem/' + problem_letter
	problem = urlopen(url)
	if problem.geturl() != url:
		break
	print(problem.geturl())
	print("Fetching problem", problem_letter)
	text = problem.read()
	#print(text.decode('utf-8'))
	parser = problem_parser()
	parser.feed(text.decode('utf-8'))
	print(parser.input)
	print(parser.output)
	if len(parser.input) != len(parser.output):
		print("Error with problem", problem_letter)
	else:
		test_count = 0
		for test_case in parser.input:
			inp = open("in" + problem_letter + str(test_count + 1) + ".txt", 'w')
			inp.write(test_case)
			inp.close()
			test_count += 1
		test_count = 0
		for test_case in parser.output:
			out = open("out" + problem_letter + str(test_count + 1) + ".txt", 'w')
			out.write(test_case)
			out.close()
			test_count += 1
		print("Fetch successful")
		problem_letter = chr(ord(problem_letter)+1)


# with open(temp_file, "w") as f:
# 	f.write("{\n")
# 	problem_letter = 'A'
# 	while True :
# 		print("fetch", problem_letter)
# 		url = 'http://codeforces.com/contest/' + contest_number + '/problem/' + problem_letter
# 		problem = urlopen(url)
# 		if problem.geturl() != url:
# 			break
# 		text = problem.read()
# 		parser = html_parser(problem_letter);
# 		parser.feed(text.decode('utf-8'))
# 		assert len(parser.sample_inputs) == len(parser.sample_outputs)
# 		f.write('"' + problem_letter +'"'+ ": " + '"' + str(parser.no_of_sample_tests) + '"'+ ",\n")
# 		parser.generate_test_files()
# 		problem_letter = chr(ord(problem_letter)+1)
# 	f.write('"hari"' + ":" + '"1"' + "\n}")

