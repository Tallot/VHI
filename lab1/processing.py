import pandas as pd
import matplotlib.pyplot as plt


def df_averaged(file):
	columns_list=['Year','Week','SMN','SMT','VCI','TCI','VHI']
	df=pd.read_csv(file, skipfooter=1, skiprows=1, names=columns_list, engine='python', delimiter='\,\s+|\,|\s+', verbose=True)
	df.fillna(0)
	return df
	
def df_percentage(file):
	columns_list = ['Year', 'Week']
	percentage_list=[str(x) for x in range(0, 105, 5)]
	columns_list.extend(percentage_list)
	df=pd.read_csv(file, skipfooter=1, skiprows=1, names=columns_list, engine='python', delimiter='\,\s+|\,|\s+')
	return df
	
def year_vhi_extremums(df,year):
	year_df = df[df.Year == year]
	max = year_df["VHI"].max()
	min = year_df["VHI"].min()
	print('Maximal VHI:', max)
	print('Minimal VHI:', min)
	year_df.plot(x='Week', y='VHI', style='g--')
	plt.show()
	print(year_df)

def percent_vhi(frame, percent):
	years_dictionary = {}
	list_of_years = []
	for year in range(1981, 2018):
		cut_frame = frame[frame.Year == year][['0', '5', '10', '15']]  #frame with percentage<=15 for current year
		list_sum = 0
		for c in list(cut_frame.columns.values):
			list_sum += cut_frame[c].mean()
		years_dictionary[str(year)] = list_sum
	series_of_years = pd.Series(years_dictionary)
	print(series_of_years.items)
	for key in series_of_years.keys():
		if series_of_years[key] > percent:
			list_of_years.append(key)
	print(list_of_years)
	return list_of_years

frame1=df_averaged('data/vhi_id_1(averaged)  2017-02-28.csv')
year_vhi_extremums(frame1, 1981)
frame2=df_percentage('data/vhi_id_1(percentage)  2017-02-28.csv')
percent_vhi(frame2, 5)