import pandas as pd
import argparse
import datetime
from IPython.display import display
import sys

#reading data
covidData = pd.read_csv("owid-covid-data.csv", encoding="ISO-8859-1")
cd = covidData.copy()

# create 'month' columnn 
month = []
for date in cd['date']:
	date_m = datetime.datetime.strptime(date, "%d/%m/%y")
	if(date_m.year == 2020):
		month.append(date_m.month)
	else:
		month.append(-1)
cd.insert(4, "months", month, True)

# create list to store every starting month and every country
months_list = []
location_list = []
months_list.append(cd['months'][0])
location_list.append(cd['location'][0])
for i in range(1, len(cd['months'])):
	if(cd['months'][i] != cd['months'][i-1]):
		if(cd['months'][i] != -1):
			months_list.append(cd['months'][i])
			location_list.append(cd['location'][i])
cd = cd.fillna(0)

# exclude data from year 2021
cd = cd.loc[cd['months'] != -1, ['location', 'months', 'total_cases', 
'new_cases', 'total_deaths', 'new_deaths']]
cd.reset_index(inplace=True)

# creating a list for case_fatality_rate
# create list for total_deaths, new_deaths, total_cases, new_cases based on month
cases_month = 0
cases_month_list = []	
total_cases_list = []	
death_month = 0
cases_death_list = []
total_death_list = []	
month = months_list[0]
increment = 0
case_fatality_rate = []

for i in range(len(cd['new_cases'])):
	if(month == cd['months'][i]):
		cases_month += cd['new_cases'][i]
		death_month += cd['new_deaths'][i]
	elif(cd['months'][i] == -1):
		pass
	else:
		total_cases_list.append(cd['total_cases'][i-1])
		total_death_list.append(cd['total_deaths'][i-1])
		cases_month_list.append(cases_month)
		cases_death_list.append(death_month)
		if cases_month != 0:
			case_fatality_rate.append(death_month/cases_month)
		else:
			case_fatality_rate.append(0)
		cases_month = 0
		death_month = 0
		cases_month += cd['new_cases'][i]
		death_month += cd['new_deaths'][i]
		increment += 1
		month = months_list[increment]
total_cases_list.append(cd['total_cases'][i])
total_death_list.append(cd['total_deaths'][i])
cases_month_list.append(cases_month)
cases_death_list.append(death_month)
if cases_month != 0:
	case_fatality_rate.append(death_month/cases_month)
else:
	case_fatality_rate.append(0)
	
# create new data, 'dataframe' which has required attributes while year = 2020
dataframe = pd.DataFrame({"location": location_list, "month": months_list, 
"total_cases": total_cases_list, "new_cases": cases_month_list, 
"total_deaths": total_death_list, "new_deaths": cases_death_list,
"case_fatality_rate": case_fatality_rate})

# sort the data by location and month
dataframe.sort_values(by=["location", "month"], ascending = True, inplace=True)


display(dataframe.head(5))

filename = sys.argv[1]
dataframe.to_csv(filename)

