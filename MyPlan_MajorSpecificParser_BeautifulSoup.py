#Name: MyPlan_MajorSpecificParser_BeautifulSoup.py
#
#Purpose: Iterates through MyPlan_URLs, and puts secondary links
#from those pages into a temporary file.
#Then, loops through the temporary file and parses each of the 
#secondary links. Within those secondary links, gathers the
#job specific information, puts it into a bson form and
#inserts it into the job colleciion of the summer2016
#mongo database
#
#Last Modified: June 27, 2016

from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import re

primary_urls = open('MyPlan_URLs.txt','r')

urls = primary_urls.readlines()

#Database Setup
client = MongoClient()
db = client.summer2016
myplan_collection = db.myplan_collection
job_collection = db.job_collection

#URL traversal and data collection
for url in urls:
	major_title = ""
	#Parsing primary URL for all secondary URLs
	f = open('Secondary_URLs_temp.txt','w')
	major = requests.get('http://www.myplan.com/majors/'+url)
	soup = BeautifulSoup(major.text)
	majortitle_span = soup.find("span",{"class":"style19"})
	if not(majortitle_span is None):
		majortitle_span = majortitle_span.contents
		major_title = majortitle_span[1]
		print(major_title)

	major_td = soup.find_all("td",{"class":"grey_dark_bold"})
	
	
	for td in major_td:
		major_a = td.find_all("a", href=True)
		for a in major_a:
			f.write(a['href'])
			f.write("\n")
	f.close()
	
	#Iterating through the secondary URLs to gather job spefic data
	f = open('Secondary_URLs_temp.txt', 'r')
	job_list = f.readlines()
	
	for j in job_list:
		headers = ['Description','Requirements','Significant Points']
		job = requests.get('http://www.myplan.com'+j)
		job_soup = BeautifulSoup(job.text)
		job_headers = job_soup.find_all(attrs={"class":"careerpage"})
		job_table = job_soup.find_all("table",{"width":"259"})
		
		job_title = job_soup.find("span",{"class":"title_header"}).string.encode('utf-8')
		job_title = job_title.replace('\r\n','').replace("  ", '')

		count = 0
		description = ""
		req = []
		sig_pts = ""
		#for table in job_table:
		while count<3:		
			if len(job_headers)>0 and count == 0 and job_headers[0].string == 'Job Description':
				job_span = job_table[0].find_all("span", {"class":"tool_description"})
				description = job_span[0].text
       	        	    	
		
       		        elif len(job_headers)>1 and count== 1 and job_headers[1].string == 'Job Requirements':
				req_td = job_soup.find_all(attrs={"background":"../../images/career_details_panel_bg.gif"})
				req_span = req_td[1].find_all(attrs={"tool_description"})	
				for j in req_span[:-1]:
					req.append(j.text)
				
			#Significant points are stored differently then
			#the rest of the data. For significant points
			#data collection, use this code
			elif len(job_headers)>2 and count==2 and job_headers[2].string == 'Significant Points':
				sig_pts_td = job_table[2].find_all("td",{"class":"tool_description"})
				pt = sig_pts_td[0].text.replace('LI {','')
				pt = pt.replace('margin-bottom: 6px;','')
				pt = pt.replace('padding-bottom: 6px;','')
				pt = pt.replace('}','')
				pt = pt.replace("\r\n",'')
				pt = pt.replace("  ",'')
				pt = pt.replace("\t",'')
				pt = pt.replace("\n",'')
				sig_pts = pt
			count = count + 1
				
	
		#Formatting for database
		job_bson = {'Major':major_title,
				'Job Title': job_title,
				headers[0]:description,
				headers[1]:req,
				headers[2]: sig_pts}
		myplan_collection.insert(job_bson)
		job_collection.insert(job_bson)		
 			
