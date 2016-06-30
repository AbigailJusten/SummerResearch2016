#Name: UW_CareerServicesMajorList.py
#
#Purpose: Gather list of majors from 
#http://careers.washington.edu/Students/What-Can-I-Do-With-a-Major-In
#
#Last Modified: June 23, 2016

from bs4 import BeautifulSoup
import requests

#Open WU_Major_List.txt
WU = open('WU_Major_URLs.txt', 'w')

url = requests.get('http://careers.washington.edu/Students/What-Can-I-Do-With-a-Major-In')
soup = BeautifulSoup(url.text)
linklist = soup.find_all("ul", {"class":"linklist"})
for item in linklist:
	links = item.find_all("a",href=True)
	for a in links:
		if "%20Paths" not in a['href']:
			WU.write(a['href'])
			WU.write("\n")
WU.close()

	
