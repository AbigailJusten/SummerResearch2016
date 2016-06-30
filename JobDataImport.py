#Name: JobDataImport.py
#
#Purpose: Traverses through job_topic_percentage, find the topics
#that are >.2 and add to the file's main topics.
#Formats data intobson formatting and enters into a MongoDB Collection
#
#Last Modified: June 30, 2016

from pymongo import MongoClient

#Database setup
client = MongoClient()
db = client.summer2016
job_topic_percentages = db.job_topic_percentage

#Open up and traverse job_topic_percentage
f = open('./Jobs_Data_Analysis/job_topic_percentages_100.txt','r')
text = f.readlines()

main_topics = []
file_name = ''
for line in text:
	count = -2
	line_edit = line.split()
	for word in line_edit:
		if count == -1:
			file_name = word
		if count > -1 and float(word) > .2:
			main_topics.append(word)
	
		count = count + 1
	main_topics = sorted(main_topics)
	print(main_topics)
	length = len(main_topics)
	topic_1 = main_topics[length-1]
	#Not all files will have three main topics,
	#therefore topics 2 and 3 are within a 
	#try - except in order to avoid the code 
	#stopping because of an IndexError
	try:
		topic_2 = main_topics[length-2]
	except IndexError:
		topic_2 = ''
	try:
		topic_3 = main_topics[length-3]
	except IndexError:
		topic_3 = ''
		
	job_bson = {'file_name':file_name,
			'topic_1':topic_1,
			'topic_2':topic_2,
			'topic_3':topic_3}
	#print(job_bson)
	main_topics = []
	#job_topic_percentages.insert(job_bson)
