## Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk
from partb2 import preprocess

''' 
this function has no arguments and output the filename that contains keyword
after the word is stemmed 
'''
def find_keyword_file():
	# sort out all documents under cricket
	directory = '/Users/czlam/GitHub/assignment-1-CZLam7/cricket'
	os.chdir(directory)
	documents = os.listdir()
	
	from nltk.stem.porter import PorterStemmer
	ps = PorterStemmer()
	
	# list at most five keywords from command line arguments
	# make all the keywords stemmed
	if(len(sys.argv) <=6):
		arguments = sys.argv[1:len(sys.argv)]
	else:
		arguments = sys.argv[1:6]
	arguments = list(set(arguments))
	arguments = [ps.stem(keyword) for keyword in arguments]
	keywords_file = []
	
	# find the document that has exactly all keywords 
	for document in documents:
		if document.endswith(".txt"):
			text = preprocess(document).split()
			stemmed_words = [ps.stem(word) for word in text]
			key_found = []
			for word in stemmed_words:
				if (word in arguments and word not in key_found):
					key_found.append(word)
				else:
					pass
			if(len(key_found) == len(arguments)):
				keywords_file.append(document)
		else:
			pass
		
	print(keywords_file)
	return (keywords_file)

''' 
this function takes array of filename as input and output a list of 
document ID of the filenames.
'''
def change_fileID(keywords_file):
	# change directory and read the csv file
	directory = '/Users/czlam/GitHub/assignment-1-CZLam7'
	os.chdir(directory)
	file_ID = pd.read_csv("partb1.csv", encoding='ISO-8859-1')
	filename_list = list(file_ID['filename'])
	fileID_list = list(file_ID['documentID'])
	
	keywords_fileID = []
	for filename in keywords_file:
		if filename in filename_list:
			file_index = filename_list.index(filename)
			documentID = fileID_list[file_index]
			keywords_fileID.append(documentID)
	
	return (keywords_fileID)
	
		
		
def main():
	print(change_fileID(find_keyword_file()))


if __name__ == '__main__':
	main()