#Name: Mongo-to-SQLite-transfer-percentages.py
#
#Purpose: To pipe  all_job_data_final into SQLite
#
#Last Modified: July 13, 2016
import sqlite3
from pymongo import MongoClient

#Open Mongo connection
client = MongoClient()
db = client.summer2016
mongodata = db.all_job_data.find()

#Set up SQLite connection
conn = sqlite3.connect('/home/abigail/SummerResearch2016/summer2016.db')
curs = conn.cursor()

curs.execute("DROP TABLE IF EXISTS all_job_data_final")
curs.execute("CREATE TABLE  all_job_data_final(id INTEGER PRIMARY KEY,\
title TEXT, major TEXT, description TEXT, topic1 REAL,\
topic1_position REAL, topic2 REAL, topic2_position REAL, topic3 REAL,\
topic3_position REAL)")
conn.commit()	

#Move data from Mongo to SQLite
count = 0
for job in mongodata:
	topic2_p = None
	topic3_p = None
	try:
		topic2_p = int(job['topic_2_position'])
	except ValueError:
		topic2_p = None

	try:
		topic3_p = int(job['topic_3_position'])
	except:
		topic3_p = None

	curs.execute("INSERT INTO all_job_data_final(id, title, major,\
description, topic1, topic1_position, topic2, topic2_position, \
topic3, topic3_position) VALUES(?,?,?,?,?,?,?,?,?,?)",
(count, job['title'], job['major'], job['description'], \
job['topic_1'], int(job['topic_1_position']), job['topic_2'], \
topic2_p,job['topic_3'], topic3_p))
	count = count + 1
	conn.commit()
print(count)
conn.close()

