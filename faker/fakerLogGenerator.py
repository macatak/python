#!/usr/bin/python3

'''
Faker Log generator
Want to generate the following events
- Basic web traffic
- Basic web traffic w/ credentials
- Basic web traffic w/ credit card info
- Basic personal info
- Advanced personal info
- Basic personal w/ location
'''

from faker import Faker
import random

faker = Faker()

def basicWebTraffic():
    #print("hi from basicWebTraffic")
    userAgent = f'user_agent: {faker.user_agent()}'
    url = f'url: {faker.url()}'
    requestIP = f'ipv4: {faker.ipv4()}'
    imageUrl = f'image_url: {faker.image_url()}'
    # bytesReturned = f'pyint: {faker.pyint()}'
    # to-do - add a platform
    print("{} {} {} {}".format(userAgent, url, requestIP, imageUrl))


def basicWebTrafficCredentials():
    #print("hi from basicWebTrafficCredentials")
    userAgent = f'user_agent: {faker.user_agent()}'
    url = f'url: {faker.url()}'
    requestIP = f'ipv4: {faker.ipv4()}'
    imageUrl = f'image_url: {faker.image_url()}'
    bytesReturned = f'pyint: {faker.pyint()}'
    # to-do - add a platform
    userName = f'user_name: {faker.user_name()}'
    password = f'password: {faker.password()}'
    print("{} {} {} {} {} {}".format(userAgent, url, requestIP, imageUrl, userName, password))

def basicWebTrafficCreditCardInfo():
    #print("hi from basicWebTrafficCreditCardInfo")
    userAgent = f'user_agent: {faker.user_agent()}'
    url = f'url: {faker.url()}'
    requestIP = f'ipv4: {faker.ipv4()}'
    imageUrl = f'image_url: {faker.image_url()}'
    #bytesReturned = f'pyint: {faker.pyint()}'
    # to-do - add a platform
    print("{} {} {} {}".format(userAgent, url, requestIP, imageUrl))

def basicPersonalInfo():
    #print("hi from basicPersonalInfo")
    userAgent = f'user_agent: {faker.user_agent()}'
    requestIP = f'ipv4: {faker.ipv4()}'
    fullName = f'name: {faker.name()}'
    address = f'street_address: {faker.street_address()}'
    city = f'city: {faker.city()}'
    state = f'state_abbr: {faker.state_abbr()}'
    zip = f'postalcode: {faker.postalcode()}'
    print("{} {} {} {} {} {}".format(userAgent, requestIP, fullName, address, state, zip))

def advancedPersonalInfo():
    #print("hi from advancedPersonalInfo")
    # credentials
    userAgent = f'user_agent: {faker.user_agent()}'
    requestIP = f'ipv4: {faker.ipv4()}'
    fullName = f'name: {faker.name()}'
    address = f'street_address: {faker.street_address()}'
    city = f'city: {faker.city()}'
    state = f'state_abbr: {faker.state_abbr()}'
    zip = f'postalcode: {faker.postalcode()}'
    userName = f'user_name: {faker.user_name()}'
    password = f'password: {faker.password()}'
    print("{} {} {} {} {} {} {} {}".format(userAgent, requestIP, fullName, address, state, zip, userName, password))

def simpleProfile():
    # name, username, address, DoB, email
    #print("hi from basicProfile")
    simpleProfile = f'simple_profile: {faker.simple_profile()}'
    userAgent = f'user_agent: {faker.user_agent()}'
    requestIP = f'ipv4: {faker.ipv4()}'
    print("{} {} {}".format(userAgent, requestIP, simpleProfile))

def detailedProfile():
    # name ssn, address, DoB, geo coordinates, username, email
    #print("hi from advancedProfile")
    advancedProfile = f'profile: {faker.profile()}'
    userAgent = f'user_agent: {faker.user_agent()}'
    requestIP = f'ipv4: {faker.ipv4()}'
    print("{} {} {}".format(userAgent, requestIP, advancedProfile))


if __name__ == '__main__':
    # set the range for however many events you want
    for i in range(10000):
        # generate a random number b/w 1-100
        ranNumber = random.randint(1, 100)
        #print(ranNumber)
        if ranNumber >= 1 and ranNumber <= 59:
            # ~ 60% of the events
            basicWebTraffic()
        elif ranNumber >= 60 and ranNumber <= 89:
            basicPersonalInfo()
        elif ranNumber >= 90 and ranNumber <= 96:
            simpleProfile()
        elif ranNumber == 97:
            basicWebTrafficCredentials()
        elif ranNumber == 98:
            basicWebTrafficCreditCardInfo()
        elif ranNumber == 99:
            advancedPersonalInfo()
        else:
            detailedProfile()
