#Name: WhatCanIDoWithThisMajor_Parse.py
#
#Purpose: Parses http://whatcanidowiththismajor.com/major/majors/ to collect
#the majors listed on the page that will then be used in a later program 
#to access the URLs for these majors
#
#Last Modified: June 28, 2016

import requests
from bs4 import BeautifulSoup

url = requests.get("http://whatcanidowiththismajor.com/major/majors/")
soup = BeautifulSoup(url.text)

majors_list = open("Major_List.txt",'w')

majors = soup.find_all("li", {"class":"associated-post"})

for major in majors:
	link = major.find("a")
	majors_list.write(link['href'])
	majors_list.write("\n")

