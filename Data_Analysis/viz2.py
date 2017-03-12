from spyre import server
import re
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

list_of_provinces=[]
for x in range (1,28):
	file = open('data/vhi_id_'+str(x)+'(averaged)  2017-02-28.csv','r')
	strln = file.readline()
	province = re.findall(r'\S+',strln)[6]
	if province[-1]==',':
		province=province[:-1]
	list_of_provinces.append(province)
	
list_of_dicts=[]
id=1
for y in list_of_provinces:
	dict = {"label":y, "value":id}
	list_of_dicts.append(dict)
	id+=1


	
	
class ViData(server.App):
	title = "Vegetation Index Data"
	inputs = [	{	"type":"dropdown",
					"label":"First province",
					"options":list_of_dicts,
					"key":"province1",
					"action_id":"update_data"},
				
				{	"type":"dropdown",
					"label":"Second province",
					"options":list_of_dicts,
					"key":"province2",
					"action_id":"update_data"},
	
				{	"type":"dropdown",
					"label":"Time Raw",
					"options":[	{"label":"VCI", "value":"VCI"},
								{"label":"TCI", "value":"TCI"},
								{"label":"VHI", "value":"VHI"}],
					"key":"clicker2",
					"action_id":"update_data"},
					
				{	"type":"dropdown",
					"label":"Year",
					"options":[{"label" : "{}".format(x), "value" : "{}".format(x)} for x in range(1981,2018)],
					"key":"clicker3",
					"action_id":"update_data"}	
													]
	controls = [{   "type" : "hidden",
                    "id" : "update_data"}]
	
	tabs = ["Plot", "Table"]
	outputs = [	{"type":"plot","id" : "plot","control_id" : "update_data","tab" : "Plot"},{"type" : "table","id" : "table_id","control_id" : "update_data","tab" : "Table","on_page_load" : True }]
	
	def getData(self, params):
	
		'''columns_list=['Year','Week','SMN','SMT','VCI','TCI','VHI']
		
		file1 = 'data/vhi_id_{}(averaged)  2017-02-28.csv'.format(params["province1"])
		file2 = 'data/vhi_id_{}(averaged)  2017-02-28.csv'.format(params["province2"])
		
		df1=pd.read_csv(file1, skiprows=1, names=columns_list, engine='python', delimiter='\,\s+|\,|\s+')
		df2=pd.read_csv(file2, skiprows=1, names=columns_list, engine='python', delimiter='\,\s+|\,|\s+')
				
		year_frame1 = df1[df1.Year == str(params["clicker3"])]
		year_frame2 = df2[df2.Year == str(params["clicker3"])]
		
		result = pd.concat([year_frame1, year_frame2], axis=1)
		
		#result = year_frame1.append(year_frame2, ignore_index=True)
		return result'''
		
		columns_list1=['Year','Week','SMN1','SMT1','VCI1','TCI1','VHI1']
		columns_list2=['Year','Week','SMN2','SMT2','VCI2','TCI2','VHI2']
		
		file1 = 'data/vhi_id_{}(averaged)  2017-02-28.csv'.format(params["province1"])
		file2 = 'data/vhi_id_{}(averaged)  2017-02-28.csv'.format(params["province2"])
		
		df1=pd.read_csv(file1, skiprows=1, names=columns_list1, engine='python', delimiter='\,\s+|\,|\s+')
		df2=pd.read_csv(file2, skiprows=1, names=columns_list2, engine='python', delimiter='\,\s+|\,|\s+')
				
		year_frame1 = df1[df1.Year == str(params["clicker3"])]
		year_frame2 = df2[df2.Year == str(params["clicker3"])]
		
		result = pd.concat([year_frame1, year_frame2], axis=1)
		
		return result
	
	def getPlot(self,params):
		'''df = self.getData(params)
		plt_obj = df.plot(x='Week', y=params['clicker2'], style='g')
		plt_obj.set_ylabel("Index")
		fig = plt_obj.get_figure()
		return fig'''
		df = self.getData(params)
		style.use('bmh')
		if params['clicker2'] == "VCI":
			plt.plot(df["Week"], df["VCI1"], label = "VCI1")
			plt.plot(df["Week"], df["VCI2"], label = "VCI2")
		elif params['clicker2'] == "TCI":
			plt.plot(df["Week"], df["TCI1"], label = "TCI1")
			plt.plot(df["Week"], df["TCI2"], label = "TCI2")
		else:
			plt.plot(df["Week"], df["VHI1"], label = "VHI1")
			plt.plot(df["Week"], df["VHI2"], label = "VHI2")
		plt.title("Epic Chart")
		plt.ylabel("Index value")
		plt.legend()
		fig = plt.gcf()
		return fig
		
			
app = ViData()
app.launch()			
			
			
			
			
			
			
			
			
			
			