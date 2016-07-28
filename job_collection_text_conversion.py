#Name: job_collection_text_conversion.py
#
#Purpose: Iterate through the job_collection within MongoDB
#and convert each entry into a text file that will be read by Mallet
#
#Last Modified: June 28, 2016

from pymongo import MongoClient

client = MongoClient()

summer2016 = client.summer2016
myplan_collection = summer2016.myplan_collection.find()
whatcanidowiththismajor_collection= summer2016.whatcanidowiththismajor_collection.find()

#looping through myplan_collection
for entry in myplan_collection:
	_id = str(entry["_id"])
	f = open(_id+".txt","w")
	
	f.write("Job Title: "+entry["Job Title"].encode('utf-8').strip()+"\n")
	f.write("Major: "+ entry["Major"].encode('utf-8').strip()+"\n\n")
	f.write("Description: "+entry["Description"].encode('utf-8').strip()+"\n\n")
	f.write("Requirements: ")
	for item in entry["Requirements"]:
		f.write(item.encode('utf-8').strip()+"\n\n")
	f.write("\n")
	f.write("Significant Points: "+entry["Significant Points"].encode('utf-8').strip())
	f.close()


#looping through whatcanidowiththismajor_collection
for entry in whatcanidowiththismajor_collection:	
	_id = str(entry["_id"])
	f = open(_id+".txt","w")
	f.write("Job Title: "+entry["job_title"].encode('utf-8').strip()+"\n\n")
	f.write("Information: ")
	for item in entry["information"]:
		f.write(item.encode('utf-8').strip())
	f.write("\n\n")
	f.write("Major: "+entry["major"].encode('utf-8').strip()+"\n\n")
	f.write("Area: ")
	for item in entry["area"]:
		f.write(item.encode('utf-8')+" ")
	f.write("\n\n")
	f.write("Employer: ")
	for item in entry["employer"]:
		f.write(item.encode('utf-8').strip())
	f.close()

