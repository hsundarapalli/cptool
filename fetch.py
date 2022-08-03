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

test_num          = "test_num.json"

##
# problem_letter = 'A'

# while True:
# 	url = 'http://codeforces.com/contest/' + contest_number + '/problem/' + problem_letter
# 	problem = urlopen(url)
# 	if problem.geturl() != url:
# 		break
# 	print("Fetching problem", problem_letter)
# 	text = problem.read()
# 	#print(text.decode('utf-8'))
# 	parser = problem_parser()
# 	parser.feed(text.decode('utf-8'))
# 	if len(parser.input) != len(parser.output):
# 		print("Error with problem", problem_letter)
# 	else:
# 		test_count = 0
# 		for test_case in parser.input:
# 			inp = open("in" + problem_letter + str(test_count + 1) + ".txt", 'w')
# 			inp.write(test_case)
# 			inp.close()
# 			test_count += 1
# 		test_count = 0
# 		for test_case in parser.output:
# 			out = open("out" + problem_letter + str(test_count + 1) + ".txt", 'w')
# 			out.write(test_case)
# 			out.close()
# 			test_count += 1
# 		print("Fetch successful")
# 		problem_letter = chr(ord(problem_letter[0])+1)

test_num_dict = {}

def check(prob_let):

	url     = 'http://codeforces.com/contest/' + contest_number + '/problem/' + prob_let
	problem = urlopen(url)

	if problem.geturl() != url:
		return False

	print("Fetching problem ", prob_let)
	text    = problem.read()
	parser  = problem_parser()
	parser.feed(text.decode('utf-8'))

	if len(parser.input) != len(parser.output):
		print("Error with problem", problem_letter)
	else:
		test_count = 0
		for test_case in parser.input:
			inp = open("in" + prob_let + str(test_count + 1) + ".txt", 'w')
			inp.write(test_case)
			inp.close()
			test_count += 1

		test_count = 0
		for test_case in parser.output:
			out = open("out" + prob_let + str(test_count + 1) + ".txt", 'w')
			out.write(test_case)
			out.close()
			test_count += 1

		test_num_dict[prob_let] = str(test_count)
	return True



def ok(prob_let):
	found = check(prob_let)
	if found:
		return True
	else:
		sub_count = 1
		#check for the subproblems
		while check(prob_let + str(sub_count)):
			sub_count +=1
			found = True

	return found

problem_letter = 'A'

while True:

	if ok(problem_letter):
		problem_letter = chr(ord(problem_letter)+1)
	else :
		print("Fetching Complete")
		break
print(test_num_dict)
with open("test_num.json", "w") as outfile:
    json.dump(test_num_dict, outfile)
# write the test case details to the json file 
