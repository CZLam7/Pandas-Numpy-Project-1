# Part B Task 2
import re
import os
import sys

import nltk

def preprocess(filename):
	f = open(filename, 'r')
	
	modified_text = ""
	
	newline = '\n'
	extraSpace = '\s{2,}'

	for string in f:
		# return small case and replace new line with one blackspace
		string = string.casefold()
		new = re.sub(newline, " ", string)  
		
		# repalce non-alphabetic characters except spacing character
		for word in new:
			for char in word:
				if not(char.isalpha()):
					if not(char == " "):
						new = new.replace(char, "")
				
		modified_text += " "
		modified_text += new

	modified_text = re.sub(extraSpace, " ", modified_text)  
	return(modified_text[1:])
	
directory = '/Users/czlam/GitHub/assignment-1-CZLam7/cricket'
os.chdir(directory)

def main():
	filename = sys.argv[1][-7:]
	print(preprocess(filename))

if __name__ == '__main__':
	main()
