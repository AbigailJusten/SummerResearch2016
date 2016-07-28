#Name: JobDataImport.py
#
#Purpose: Traverses through job_topic_percentage, find the topics
#that are >.1 and add to the file's main topics.
#Formats data intobson formatting and enters into a MongoDB Collection
#
#Last Modified: July 14, 2016

from pymongo import MongoClient

#Database setup
client = MongoClient()
db = client.summer2016
job_topic_percentages = db.job_topic_percentage

#Open up and traverse job_topic_percentage
f = open('./Jobs_Data_Analysis/job_topic_percentages_100.txt','r')
text = f.readlines()

main_topics = []
topic_position = []
file_name = ''
for line in text:
	count = -2
	line_edit = line.split()
	for word in line_edit:
		if count == -1:
			file_name = word
		if count > -1 and float(word) > .1:
			main_topics.append(float(word))
			topic_position.append(count)
				
		count = count + 1	
	main_topics, topic_position = zip(*sorted(zip(main_topics, topic_position)))
	main_topics, topic_position = (list(t) for t in zip(*sorted(zip(main_topics, topic_position))))
	length = len(main_topics)
	topic_1 = main_topics[length-1]
	topic_1_position = topic_position[length-1]
	#Not all files will have three main topics,
	#therefore topics 2 and 3 are within a 
	#try - except in order to avoid the code 
	#stopping because of an IndexError
	if length > 1:
		topic_2 = main_topics[length-2]
		topic_2_position = topic_position[length-2]
	else:
		topic_2 = None
		topic_2_positon = None
		topic_3 = None
		topic_3_position = None
	if length > 2:
		topic_3 = main_topics[length-3]
		topic_3_position = topic_position[length-3]
	else:
		topic_3 = None
		topic_3_position = None
	main_topics = []
	topic_position = []
	
	job_bson = {'file_name':file_name,
			'topic_1':topic_1,
			'topic_1_position': topic_1_position,
			'topic_2':topic_2,
			'topic_2_position':topic_2_position,
			'topic_3':topic_3,
			'topic_3_position':topic_3_position,
		}
		
	main_topics = []
	topic_position = []
	topic_1 = ''
	topic_2 = ''
	topic_3 = ''
	topic_1_position = ''
	topic_2_position = ''
	topic_3_position = ''
	job_topic_percentages.insert(job_bson)
	
