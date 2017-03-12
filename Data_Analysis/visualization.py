from spyre import server
import re
import pandas as pd
import matplotlib.pyplot as plt

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
					"label":"Province",
					"options":list_of_dicts,
					"key":"clicker1",
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
	outputs = [	{"type":"plot",
				"id" : "plot",
				"control_id" : "update_data",
				"tab" : "Plot"},
				
				{"type" : "table",
				"id" : "table_id",
				"control_id" : "update_data",
				"tab" : "Table",
				"on_page_load" : True }]
	
	def getData(self, params):
	
		file = 'data/vhi_id_{}(averaged)  2017-02-28.csv'.format(params["clicker1"])
		columns_list=['Year','Week','SMN','SMT','VCI','TCI','VHI']
		df=pd.read_csv(file, skiprows=1, names=columns_list, engine='python', delimiter='\,\s+|\,|\s+')
		year_frame = df[df.Year == str(params["clicker3"])]
		return year_frame
	
	def getPlot(self,params):
		df = self.getData(params)
		plt_obj = df.plot(x='Week', y=params['clicker2'], style='g--')
		plt_obj.set_ylabel("Index")
		fig = plt_obj.get_figure()
		return fig
			
app = ViData()
app.launch()			
			
			
			
			
			