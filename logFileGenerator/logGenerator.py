#!/usr/bin/python3

'''
simple CSV reader
will print out the row selected
or add it to a list to be used as part of a larger program
so just change it to the desired row
'''

# importing module
import csv, random, time
from random import randint


def read_csv(csvFilename, row_number):
    '''
    read a CSV file into a list
    args are filename and row of the desired item
    '''

    with open(csvFilename) as f:
        # list object to return
        return_list = []
        # open the file which returns a pointer to the 1st line
        reader = csv.reader(f)
        # this will move the pointer to the next line so it skips the header line of the CSV
        next(reader)
        for row in reader:
            # print it if you want
            # print(row[row_number])
            # add it to a list
            return_list.append(row[row_number])
    return return_list

def get_random_item(list_name, random_range):
    '''
    return a random item from a list
    '''
    ran = random.randint(1,random_range)
    return list_name[ran]

if __name__ == '__main__':
    # generate lists from CSV files
    filename2 = "/home/zaphod/Downloads/lascon/csv/surnames.csv"
    firstNameList = read_csv("/home/zaphod/Downloads/lascon/csv/baby-names.csv", 1)
    lastNameList = read_csv("/home/zaphod/Downloads/lascon/csv/surnames.csv", 0)
    urlsList = read_csv("/home/zaphod/Downloads/lascon/csv/top-500-urls.csv", 1)
    #messageList = read_csv("/home/zaphod/Downloads/lascon/csv/Human-to-HumanActionableRequestsDataset.csv", 1)
    messageList = read_csv("/home/zaphod/Downloads/lascon/csv/PasswordActionableRequestsDataset.csv", 1)
    requestList = read_csv("/home/zaphod/Downloads/lascon/csv/PasswordActionableRequestsDataset.csv", 0)

    # get the lengths of each list
    lenFirstName = len(firstNameList)
    lenLastName = len(lastNameList)
    lenUrl = len(urlsList)
    lenMessage = len(messageList)
    lenRequest = len(requestList)
    # timeToRun is how many seconds you want the loop to run
    timeToRun = int(time.time() + 600)
    # print it, make it all lower case, and tweak the epoch time to an int
    #for i in range(10):
    while (int(time.time()) < int(timeToRun)):
        fname = get_random_item(firstNameList, lenFirstName - 1)
        lname = get_random_item(lastNameList, lenLastName - 1)
        url = get_random_item(urlsList, lenUrl - 1)
        sender = str.lower((get_random_item(firstNameList, lenFirstName - 1) + "." + get_random_item(lastNameList, lenLastName - 1) + "@" +  get_random_item(urlsList, lenUrl - 1)))
        receiver = str.lower((get_random_item(firstNameList, lenFirstName - 1) + "." + get_random_item(lastNameList, lenLastName - 1) + "@" +  get_random_item(urlsList, lenUrl - 1)))
        message = get_random_item(messageList, lenMessage -1)
        request = get_random_item(requestList, lenRequest - 1)
        print("{} : sender: {} : receiver: {} requestType : {} : msg : {}".format(int(time.time()), sender, receiver, request, message))
        time.sleep((random.random()))
