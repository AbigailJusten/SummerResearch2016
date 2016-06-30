#Name: MyPlan_MajorParser.py
#
#Purpose: Compile top level  URLs 
#from http://www.myplan.com/majors/what-to-do-with-a-major.php
#
#Last Modified: June 23, 2016

from bs4 import BeautifulSoup
import requests

f = open('MyPlan_URLs.txt', 'w')

url = requests.get('http://www.myplan.com/majors/what-to-do-with-a-major.php')
soup = BeautifulSoup(url.text)

majors_td = soup.find_all("td",{"class":"tool_description"})
for td in majors_td:
	majors_a = td.find_all("a", href=True)
	for link in majors_a:
		f.write(link['href'])
		f.write("\n")
f.close()
