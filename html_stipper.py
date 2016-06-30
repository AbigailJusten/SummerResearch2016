#html_stripper.py
#
#Purpose: Remove all html tags from the files created by downloading 
#the URLs listed in Majors_List_URLs.txt
#
#Last Modified: June 18, 2016

import re

major_list = open("Major_List.txt",'r')

for major in major_list:
	major = major.strip('\n')
	major_html = open('WhatCanIDoWithThisMajor_Data/'+major,'r')
	file_text = major_html.read()
	major_html.close()
	p = re.compile('<[^>]>')
	clean_text  = re.sub(p,'',file_text)
	major_text = open('WhatCanIDoWithThisMajor_Data/clean_'+major,'w')
	major_text.write(clean_text)
