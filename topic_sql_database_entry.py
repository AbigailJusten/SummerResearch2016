#Name: topic_sql_database_entry.py
#
#Purpose: Iterate through job_topic_keys_100.txt and put the topics
#into a mongo database name topic_keys_100
#
#Last Modified: July 15, 2016

from pymongo import MongoClient
import sqlite3

#Database Setup
client = MongoClient()
db = client.summer2016
job_topic_keys_100 = db.job_topic_keys_100

conn = sqlite3.connect('/home/abigail/SummerResearch2016/summer2016.db')
curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS topics")
curs.execute("CREATE TABLE topics(id INTEGER PRIMARY KEY, topic TEXT)")
conn.commit()

#Open up and traverse job_topic_keys_100.txt
f = open('./Jobs_Data_Analysis/job_topic_keys_100.txt', 'r')
text = f.readlines()

count = 0;
for line in text:
	line = line.replace('	0.05	',' ')
	line = line.replace(str(count), '')
	line = line.decode('utf-8', 'ignore')
	
	topic_bson = {'topic' : line}
	job_topic_keys_100.insert(topic_bson)
	
	count = count + 1
	#curs.execute("INSERT INTO topics(id, topic) VALUES(?,?)", \
        #(count, line))
	#conn.commit()
	#count = count + 1

#Move the MongoDB to a SQL DB
mongodata = job_topic_keys_100.find()
id_count = 0
for topic in mongodata:
	curs.execute("INSERT INTO topics(id, topic) VALUES(?,?)", \
	(id_count, topic['topic']))
	id_count = id_count + 1
	conn.commit()
	
print(id_count)
conn.close()

