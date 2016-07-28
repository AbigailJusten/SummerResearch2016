#Name: all_job_data.py
#
#Purpose: Read the file associated with the documents in the
#job_topic_percentage table and add in the missing data to the
#document
#
#Last Modified: July 13, 2016

from pymongo import MongoClient

#Open both Mongo connections
client = MongoClient()
db = client.summer2016
percentages = db.job_topic_percentage.find()
all_data = db.all_job_data
#Iterate through job_topic_percentags
for job in percentages:
	file_name = str(job['file_name'])
	file_name = file_name.replace('file:','')
	f = open(file_name)
	job_title = f.readline()
	job_title = unicode(job_title, 'ascii', 'ignore')
	major = f.readline()
	major = unicode(major, 'ascii', 'ignore')
	description = f.readlines()
	description_edit = ''
	
	for d in description:
		if d != '\n':
			description_edit = description_edit + unicode(d, 'ascii', 'ignore') + "\n"
	
	job_bson = {'major': major, 'title': job_title,\
'description' : description_edit, 'topic_1': job['topic_1'], \
'topic_2': job['topic_2'], 'topic_3': job['topic_3'],\
'topic_1_position': job['topic_1_position'], 'topic_2_position':\
job['topic_2_position'], 'topic_3_position': job['topic_3_position']}
	all_data.insert(job_bson)
