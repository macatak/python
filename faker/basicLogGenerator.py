#!/usr/bin/python3

'''
basic Python script to write stdout and a file
'''
# imports
from datetime import datetime
from faker import Faker
from random import randint
import csv, random, time

# objects
faker = Faker()

# functions
def createRanNum():
    # return a unique scaled number
    # weighted on a sale of 0-100 so most should be info
    ranNumber = random.randint(0, 100)
    if ranNumber >= 0 and ranNumber <= 70:
        # 70% should be 1
        ranNumber = "1"
        # ranNumber = "fatal"
    elif ranNumber >= 71 and ranNumber <= 75:
        # 5%
        ranNumber = "2"
    elif ranNumber >= 76 and ranNumber <= 80:
        # 5%
        ranNumber = "3"
    elif ranNumber >= 81 and ranNumber <= 85:
        # 5%
        ranNumber = "4"
    elif ranNumber >= 86 and ranNumber <= 90:
        # 5%
        ranNumber = "5"
    elif ranNumber >= 91 and ranNumber <= 98:
        # 7%
        ranNumber = "6"   
    else:
        # 3%
        ranNumber = "9" #  + str(ranNumber)   
    return ranNumber

def createLogLevel():
    # return a standard log level
    # weighted on a sale of 0-100 so most should be info
    ranNumber = random.randint(0, 100)
    if ranNumber >= 0 and ranNumber <= 70:
        logLevel = "info"
    elif ranNumber >= 71 and ranNumber <= 75:
        logLevel = "debug"
    elif ranNumber >= 76 and ranNumber <= 80:
        logLevel = "trace"
    elif ranNumber >= 81 and ranNumber <= 85:
        logLevel = "warn"
    elif ranNumber >= 86 and ranNumber <= 90:
        logLevel = "error"
    elif ranNumber >= 91 and ranNumber <= 99:
        logLevel = "critical"    
    else:
        logLevel = "fatal " #  + str(ranNumber)    
    return logLevel

def get_random_item(list_name, random_range):
    '''
    return a random item from a list
    '''
    ran = random.randint(1,random_range)
    return list_name[ran]

def createHttpResponseCode():
    # return response code
    # weighted on a sale of 0-100
    # 200's/300's should be most common
    ranNumber = random.randint(0, 100)
    if ranNumber >= 0 and ranNumber <= 90:
        httpResponse = "1"  # 100/200/300 not important
    elif ranNumber >= 91 and ranNumber <= 97:
        httpResponse = "3"  #400's 
    else:
        httpResponse = "6" # 500   
    return httpResponse

def createIpAddress():
    # create a somewhat random IP address
    ranIP = '10.10.10.' + str(random.randint(0, 50))
    return ranIP

if __name__ == '__main__':
    # variables
    # for file out
    outWriteFile = open('/home/bikeride/sampleLogs/logGen.log', 'a')

    #runTime = 6000
    runTime = 10
    timeToRun = int(time.time() + runTime)
    # for i in range(1000):
    while (int(time.time()) < int(timeToRun)):
        severity = createRanNum()
        loglevel = createLogLevel()
        http_response_code = createHttpResponseCode()
        return_status = faker.boolean()
        hostName = faker.hostname()
        src_ip = createIpAddress()
        # get a timestamp
        today = datetime.now()
        iso_datetime = today.isoformat()
        # stdout
        print("{},ip:{},ReturnCode:{},logLevel:{},Severity:{}".format \
              (iso_datetime, src_ip, http_response_code, loglevel, severity))
        outWriteFile.write("{},ip:{},ReturnCode:{},logLevel:{},Severity:{}\n".format(iso_datetime, src_ip, http_response_code, loglevel, severity))
        # short random delay
        time.sleep((random.random()))
