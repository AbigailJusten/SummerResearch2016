# SummerResearch2016
The purpose of this repository is to store the code, data and site for research done on the topic modeling of job descriptions. 

The data for the project can be found in the summer2016.db. Some of the files that originally stored the information for this
database are also in the repository, but the most accurate data will be found in the database.

The analysis from the topic modeling (done using Mallet) can be found in the Jobs_Data folder. The code for collecting the initial
data that was run through Mallet can be found throughout the following files: 
MyPlan_MajorParser.py (Purpose: Gather the first round of URLs and store them in MyPlan_URLs.txt)
MyPlan_MajorSpecificParser_BeautifulSoup.py (Purpose: Iterate through MyPlan_URLs.py, finding all secondary links, iterating through secondary links which lead to major specific data and then collecting the major specific data )
MyPlan_MajorSpecificParser_Uniform.py (Purpose: Same as MyPlan_MajorSpecificParser_BeautifulSoup.py but stores the data in a schema matching the data from What Can I Do With This Major )
WhatCanIDoWithThisMajor_Parse.py (Purpose: Parser What Can I Do With This Major listing site and gather URLs for each major.)
WhatCanIDoWithThisMajor_BeautifulSoup.py(Purpose: Iterates through Major_List.txt and gathers data from each of the specific major job listings. )
WhatCanIDoWithThisMajor_Uniform.py (Purpose: Same as WhatCanIDoWithThisMajor_Parse.py but changes the schema of the data to match MyPlan data)

The results from the topic analysis can be found in the Jobs_Data_Anlysis folder.

The code for the site, which shows a visual representation of the data, can be found in the CareerTopics folder and is based on the
Django framework. 


