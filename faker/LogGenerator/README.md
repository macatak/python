Found Faker for Python. Install is easy and has a lot of built in patterns.  

The goal I had was to generate a log where most of the event contain no personal data but some did. Most of the events are meant to be (sort of) web traffic. 

Files  
faker101.py - prints out most of the types of data it can print.  
fakerFunctions.txt - The output from faker101.py. Shows examples of the random data.  
fakerFields.txt - These are the fileds I was interested in and sample values. Sorted by types of events.  
fakerLogGenerator.py - The script I used to generate events. It's set to a percentage of which functions are called how often. Functions are broken up into varying levels of personal data. Set the range to however many events you want (currently 10,000)
