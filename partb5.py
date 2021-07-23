## Part B Task 5
import os
import sys
import operator

from numpy import dot
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfTransformer
from partb2 import preprocess
from partb4 import find_keyword_file
from partb4 import change_fileID
file_contains_keyword = find_keyword_file()
from nltk.stem.porter import PorterStemmer

file_contains_keyword = find_keyword_file()
transformer = TfidfTransformer()
ps = PorterStemmer()

def main():
	directory = '/Users/czlam/GitHub/assignment-1-CZLam7/cricket'
	os.chdir(directory)
	documents = os.listdir()
	
	if file_contains_keyword == []:
		print("documentID  score")
		sys.exit()
		
	# stemmed the words and store in a list, total_words
	# concetenate string from all text files into total_texts
	total_words = []
	total_texts =  ""
	for document in documents:
		if document in file_contains_keyword:
			text = preprocess(document).split()
			stemmed_words = [ps.stem(word) for word in text]
			total_words.append(stemmed_words)
			for word in stemmed_words:
				total_texts += word
				total_texts += " "
	
	# create a dictionary with word from all text as key
	word_frequency = {}
	for line in total_words:
		for word in line:
			if word not in word_frequency:
				word_frequency[word] = 0
				
	doc_tfidf = frequency_words(total_words, word_frequency)
	doc_qunit = query_vector(word_frequency)	
	dic_ranking = rank_document_similarity(doc_qunit, doc_tfidf)
	print("documentID  score")
	for items in dic_ranking:
		print('{:11s}'.format(items), end=' ')
		print(dic_ranking[items])

'''
this function input total_words array and dictionary(word_frequency), and sort 
out the TF-IDF and return TF-IDF for all texts
'''
def frequency_words(total_words, word_frequency):
	frequency_words = []
	
	for lines in total_words:
		word_frequency_copy = word_frequency.copy()
		for word in lines:
			if word in word_frequency_copy:
				word_frequency_copy[word] += 1
		frequency_words.append(list(word_frequency_copy.values()))
	
	if frequency_words == []:
		frequency_words = [[]]
	
	tfidf = transformer.fit_transform(frequency_words)
	transformer.idf_
	doc_tfidf = tfidf.toarray()
	return (doc_tfidf)


'''
this function input dictionary (word_frequency) and return the query vector
'''
def query_vector(word_frequency):
	if(len(sys.argv) <=6):
			arguments = sys.argv[1:len(sys.argv)]
	else:
		arguments = sys.argv[1:6]
	arguments = list(set(arguments))
	arguments = [ps.stem(keyword) for keyword in arguments]
	frequency_keywords = []
	for keyword in arguments:
		if keyword in word_frequency:
			word_frequency[keyword] += 1
	frequency_keywords.append(list(word_frequency.values()))
	q_unit = transformer.fit_transform(frequency_keywords)
	transformer.idf_
	doc_qunit = q_unit.toarray()[0]
	return(doc_qunit)

''' 
this function returns the dot product of two vectors divide by normalised value
of two vectors
'''
def cosine_sim(v1, v2):
	return dot(v1, v2)/(norm(v1) * norm(v2))
	
'''
this function input doc_qunit array, doc_tfidf array, then output the dictionary
contain documentID as key and rank document similarity
as value
'''
def rank_document_similarity(doc_qunit, doc_tfidf):
	sims = [round(cosine_sim(doc_qunit, doc_tfidf[d_id]), 4) for d_id in 
	range(doc_tfidf.shape[0])]
	fileID = change_fileID(file_contains_keyword)
	dic_ranking = dict(zip(fileID, sims))
	dic_ranking= dict(sorted(dic_ranking.items(), key=operator.itemgetter(1), 
		reverse = True))
	return (dic_ranking)

if __name__ == '__main__':
	main()
		