import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

covidData = pd.read_csv("owid-covid-data-2020-monthly.csv", encoding = 'ISO-8859-1')
covidData = covidData.dropna()

# create a list for all location
location_list = []
for location in covidData['location']:
	if location not in location_list:
		location_list.append(location)
	
# create array of data based on location
location_data = []
for location in location_list:
	location_data.append(covidData.loc[covidData['location'] == location])

# plot scatter plot for case_fatality_rate vs confirmed new cases
for data in location_data:
	location_name = data['location'].values[0]
	plt.scatter(data['new_cases'], data['case_fatality_rate'], label=location_name)

plt.ylabel("case_fatality_rate")
plt.xlabel("confirmed_new_cases")
plt.title("Covid19 Dataset case fatality rate vs confirmed new cases")

plt.xlim(0, 20000000.0)
plt.ylim(0, 1.0)
plt.grid(True)
plt.legend()
plt.savefig(filename1)


# create a new column for log_new_cases withot including infinity values
new_cases = covidData['new_cases']
log_newcases = [np.log(i) if i>0 else 0 for i in new_cases]
covidData.insert(3, "log_newcases", log_newcases, True)
covidData = covidData.fillna(0)

# create array of data based on location
location_data = []
for location in location_list:
	location_data.append(covidData.loc[covidData['location'] == location])


# plot scatter plot for case_fatality_rate vs log new cases
for data in location_data:
	if not(data.empty):
		location_name = data['location'].values[0]
		plt.scatter(data['log_newcases'], data['case_fatality_rate'], label=location_name)

plt.ylabel("case_fatality_rate")
plt.xlabel("log_new_cases")
plt.title("Covid19 Dataset case fatality rate vs log new cases")

plt.xscale('log')
plt.xlim(0, 10000000)
plt.ylim(0, 1.0)
plt.grid(True)
plt.legend()
plt.savefig(filename2)
