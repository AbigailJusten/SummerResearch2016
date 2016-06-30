#Name: WhatCanIDoWithThisMajor_BeautifulSoup.py
#
#Purpose: Parse http://whatcanidowiththismajor.com/major/majors/<major>
#to gather information to put into database
#
#Last Modified: June 20, 2016

from bs4 import BeautifulSoup
import requests

#Open Major_List.txt and iterate through the majors. Access data
#on each page, place into MangoDB doucments and insert into
#MongoDB
f = open('Majors_List_URLs.txt','r')
major_list = f.readlines()
all_majors =[]

for major in major_list:
	major = major.strip('\n')
	#Access URL and create a BeautifulSoup
	#url = requests.get("http://whatcanidowiththismajor.com/major/"+major)
	url = requests.get(major)
	soup = BeautifulSoup(url.text)
	formatted_job_list = []
	area = []
	employer = []
	information = []
	#Overarching Career Field
	if soup.find("h1",{"class":"entry-title"}):
		major_title = soup.find("h1",{"class":"entry-title"}).string
		print(major_title)
	#Job Titles
	job_titles = []
	strong = soup.find_all("strong")
	for item in strong:
		if item.string!= 'Area' and item.string!='Employer' and item.string!='Information/Strategies' and item.string != None and item.string!=' ':
			job_titles.append(item.string)
		#Dealing with <br/>
		if item.string == None:
			for child in item.children:
				if child != None:
					job_titles.append(child.string)
					
	#print(job_titles)
	#Job Information
	headers = ['AREA', 'EMPLOYER', 'INFORMATION']
	#everything in a div with the class ezcol-one-third
	ezcol_all = soup.find_all("div", {"class":"ezcol-one-third"})
	ezcol_lists = []
	
	#every list within the above divs
	for entry in ezcol_all:
		item = entry.find("ul")
		if item != None: 
			ezcol_lists.append(item)
	
	#Match up the Area, Employer and Information of each job 
	#with the correct lists
	header_counter = 0;
	job_counter = 0;
	for entry in ezcol_lists:
		#if header_counter == 0:
		#print(job_titles[job_counter])
		#print(headers[header_counter])
		
		#An item is one of the bullet points within one of the columns
		for item in entry:
	
			#Checking for any sub lists within the bullet point
			if item.string != None and item.find("ul") == None:
				if header_counter == 0:
					area.append(item.string.encode('utf-8'))
				elif header_counter == 1:
					employer.append(item.string.encode('utf-8'))
				elif header_counter == 2:
					information.append(item.string.encode('utf-8'))	
				#print(item.string.encode('utf-8'))
	
			#If there is a sub list, iterate through 
			#everything inside of it
			else:
				#Iterates through lists within the item
				inside_list = item.find("ul")
				if inside_list != -1 and inside_list !=None:
					for i in inside_list:
						if header_counter == 0 :
							#Traversing interior lists
							if i.find("ul") and i.find("ul") != -1:
								inside = i.find("ul")
								for j in inside:
									area.append(j.string.encode('utf-8'))
							else:
								area.append(i.string.encode('utf-8'))
						elif header_counter == 1:
							#Traversing interior lists
							if i.find("ul") and i.find("ul") != -1:
								inside = i.find("ul")
								for j in inside:
									employer.append(j.string.encode('utf-8'))
							elif not(i.string is None):
								employer.append(i.string.encode('utf-8'))
						elif header_counter == 2:
							if i.find("ul") and i.find("ul")!=-1:
								inside = i.find("ul")
								for j in inside:
									information.append(j.string.encode('utf-8'))
							else:
								information.append(i.string.encode('utf-8'))
						#print(i.string.encode('utf-8'))
				
		if header_counter < 2:
			header_counter = header_counter + 1
			#print("\n")
		else:
			header_counter = 0
			job_json = {'major' : major_title,
					'job_title' : job_titles[job_counter],
					'area':area,
					'employer':employer,
					'information':information
					}
			#print(job_json)
	
			formatted_job_list.append(job_json)
			job_counter = job_counter + 1
			area = []
			employer = []
			information = []
			#print("\n")
	
	all_majors.append(formatted_job_list)
#print(all_majors)

	#Set up database
#	client = MongoClient()
#	db = client.summer2016
#	db.createCollection(jobs)
	
#	for job in formatted_job_list:

#		db.jobs.insert(job)
