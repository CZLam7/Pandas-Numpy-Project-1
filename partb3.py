## Part B Task 3
import re
import sys
import pandas as pd
import nltk
import os
from partb2 import preprocess

# sort out all documents under cricket
directory = '/Users/czlam/GitHub/assignment-1-CZLam7/cricket'
os.chdir(directory)
documents = os.listdir()

from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()

# list at most five keywords from command line arguments
if(len(sys.argv) <=6):
	arguments = sys.argv[1:len(sys.argv)]
else:
	arguments = sys.argv[1:6]
arguments = list(set(arguments))

keywords_file = []

# find the document that has exactly all keywords 
for document in documents:
	if document.endswith(".txt"):
		text = preprocess(document).split()
		lemmatized_words = [lem.lemmatize(word) for word in text]
		key_found = []
		for word in lemmatized_words:
			if (word in arguments and word not in key_found):
				key_found.append(word)
			else:
				pass
		if(len(key_found) == len(arguments)):
			keywords_file.append(document)
	else:
		pass
	
# change directory and read the csv file
directory = '/Users/czlam/GitHub/assignment-1-CZLam7'
os.chdir(directory)
file_ID = pd.read_csv("partb1.csv", encoding='ISO-8859-1')

keywords_fileID = []

# find the fileID from the csv file from partb1.csv
for filename in keywords_file:
	if filename in list(file_ID['filename']):
		keywords_info = file_ID.loc[file_ID['filename'] == filename, 
		'documentID']
		keywords_fileID.append(list(keywords_info)[0])

		
print(keywords_fileID)
