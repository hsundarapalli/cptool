#!/usr/bin/python3
from urllib.request import urlopen
import sys
import json
from parser import problem_parser
from configurations import *


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

		update_test_case_num(prob_let, str(test_count))
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

