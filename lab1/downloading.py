import urllib.request
import datetime
import os

if not os.path.isdir("data"):
    os.makedirs("data")

print("Downloading VHI data...")	
	
for x in range (1,28):
	url1="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+str(x)+"&year1=1981&year2=2017&type=Mean"
	vhi_url1 = urllib.request.urlopen(url1)
	file1 = open('data/vhi_id_'+str(x)+'(averaged)  '+str(datetime.date.today())+'.csv','wb')
	file1.write(vhi_url1.read())
	file1.close()
	url2="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+str(x)+"&year1=1981&year2=2017&type=VHI_Parea"
	vhi_url2 = urllib.request.urlopen(url2)
	file2 = open('data/vhi_id_'+str(x)+'(percentage)  '+str(datetime.date.today())+'.csv','wb')
	file2.write(vhi_url2.read())
	file2.close()
	
print ("Completed")
