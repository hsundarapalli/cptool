from html.parser import HTMLParser

class html_parser(HTMLParser): 
	problem_letter     = None
	no_of_sample_tests = 0
	test_buffer        = []
	sample_inputs      = []
	sample_outputs     = []
	got_a_test_case    = False
	turn               = 0     # 0 if inputs are reading 
							   # 1 if outpts are reading
	def __init__(self, problem_letter):	
		self.problem_letter = problem_letter
		HTMLParser.__init__(self) 
	def handle_starttag(self, tag, attrs):
	    if tag == "pre":
	    	self.got_a_test_case = True

	def handle_endtag(self, tag):
		if tag == "pre":
			self.got_a_test_case      = False
			
			if self.turn == 1:
				self.sample_outputs.append(self.test_buffer)
			elif self.turn == 0:
				self.sample_inputs.append(self.test_buffer)
			self.test_buffer = []

			self.turn                 += 1
			self.turn                 %= 2
			self.no_of_sample_tests   += 1 * self.turn

	def handle_data(self, data):
		if self.got_a_test_case:
			self.test_buffer.append(data);
			test_case = data.split("\n")
			

	def generate_test_files(self):
		for test_count in range(self.no_of_sample_tests):
			with open("in" + self.problem_letter + str(test_count + 1) + ".txt", "w") as f:
				for lines in self.sample_inputs[test_count]:
					f.write(lines + "\n")
			with open("out" + self.problem_letter + str(test_count + 1) + ".txt", "w") as f:
				for lines in self.sample_outputs[test_count]:
					f.write(lines + "\n")
		print("Problem " + self.problem_letter + " feteched successfully !!") 