#!/usr/bin/python3

'''
Faker Log generator
generate server names with time stamps
and some other meaningless info
format
dca/dcb/dcc _data center A/B/C
server name 100-300

'''

from faker import Faker
from datetime import datetime
#from random import randint
import random, time

faker = Faker()

def create_edc():
    ranNumber = random.randint(1, 10)
    #print(ranNumber)
    if ranNumber >= 1 and ranNumber <= 5:
        dc = "dca"
    elif ranNumber >= 6 and ranNumber <= 8:
        dc = "dcb"
    else:
        dc = "dcc"
    return dc

def create_server_number():
    return random.randint(100, 299)

if __name__ == '__main__':
    # set the range for however many events you want
    #for i in range(100):
    # timeToRun is how many seconds you want the loop to run
    timeToRun = int(time.time() + 10000000000)
    # print it, make it all lower case, and tweak the epoch time to an int
    #for i in range(10):
    while (int(time.time()) < int(timeToRun)):
        # generate a date/time stamp
        now = datetime.now()
        dts = now.strftime("%m/%d/%Y %H:%M:%S")
        edc = create_edc()
        server_num = create_server_number()
        print('{},{}{},{},{}'.format(dts,edc,server_num,faker.ipv4_public(),faker.user_agent()))
        # set a delay
        time_delay = (random.random() * 10)
        #print(time_delay)
        time.sleep(time_delay)
        #time.sleep((random.random()))
