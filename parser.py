from html.parser import HTMLParser
import os

class problem_parser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.reading  = False
    self.input    = []
    self.output   = []
    self.buffer   = ""

  def handle_starttag(self, tag, attrs):
    if tag == "pre":
      self.reading = True
      
  def handle_endtag(self, tag):
    if tag == "pre":
      self.reading = False
      if len(self.input) == len(self.output):
        self.input.append(self.buffer)
      else:
        self.output.append(self.buffer)
      self.buffer = ""

  def handle_data(self, data):
    if self.reading:
      self.buffer += data + '\n'  