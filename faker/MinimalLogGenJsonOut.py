#!/usr/bin/python3

'''
basic Python script to write stdout and a file
Outputs an IP address, log level, and return code
'''
# imports
from datetime import datetime
from faker import Faker
from random import randint
import json, random, time

# objects
faker = Faker()

# functions
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

def createHttpResponseCode():
    # return response code
    # weighted on a sale of 0-100
    # 200's/300's should be most common
    # Define the ranges of HTTP status codes
    http_200s = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]
    http_300s = [300, 301, 302, 303, 304, 305, 307, 308]
    http_400s = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 426, 428, 429, 431, 451]
    http_500s = [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]
    # Define the weighted choices
    response_code_ranges = [http_200s, http_300s, http_400s, http_500s]
    weights = [0.70, 0.20, 0.07, 0.03]
    # Choose a range based on the weights
    chosen_range = random.choices(response_code_ranges, weights)[0]
    # Choose a random code from the selected range
    response_code = random.choice(chosen_range)
    return response_code

def createIpAddress():
    # create a somewhat random IP address
    ranIP = '10.10.10.' + str(random.randint(0, 50))
    return ranIP

if __name__ == '__main__':
    # for file out
    # outWriteFile = open('/home/bikeride/sampleLogs/logGen.log', 'a')
    # Create a list to hold the JSON data 
    data = []
    
    # print a header row
    print("ip,logLevel,returnCode")

    # set to number of lines out
    for i in range(10000):
        row = {
            "ip": createIpAddress(),
            "loglevel": createLogLevel(),
            "returnCode": createHttpResponseCode()
            }
        data.append(row)
    with open("mininalLog.json", "w") as outfile:
        json.dump(data, outfile,)
