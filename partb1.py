## Part B Task 1

import re
import pandas as pd
import os
from IPython.display import display
import sys

pattern = r'[a-zA-Z]{4}-\d{3}[a-zA-Z]?'

directory = '/Users/czlam/GitHub/assignment-1-CZLam7/cricket'
os.chdir(directory)


ID_list = []
textname_list = []
increment=0

for filename in os.listdir(directory):
	if filename.endswith(".txt"):
		f = open(filename, 'r')
		for string in f:
			if re.search(pattern, string):
				fileID = re.findall(pattern, string)
				ID_list.append(fileID[0])
				textname_list.append(filename)
				
ID = pd.Series(ID_list)
textname = pd.Series(textname_list)
document = pd.DataFrame({"filename": textname_list, "documentID": ID_list})

directory = '/Users/czlam/GitHub/assignment-1-CZLam7'
os.chdir(directory)

filename = sys.argv[1]
document.to_csv(filename)
