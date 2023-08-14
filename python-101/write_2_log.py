#!/usr/bin/python3

# write a log file in Python using a datetime stamp and hostname
# format of log entry
#
# # <ISO timestamp> - <hostname> : <message>

from datetime import datetime   # to get a timestamp
import socket                # get the host name

# get the current time and date
now = datetime.now()

# get the hostname
hostname = socket.gethostname()
print("host : ", hostname)

# declare the log file
# 'a' is for append, creates it if not there
# addes a line if it is
log_file = open("/tmp/spam.log", "a")

# format it so it is HH:MM:SS-day-month-year
# for a 2 digit year use 'y' instead of 'Y'
dts = now.strftime("%H:%M:%S-%d-%m-%Y")
# ISO 8601 format
iso_dts = now.isoformat()
print('human friendly date : {}'.format(dts))
print('ISO 8601 format : {}'.format(iso_dts))

# create a dummy log entry
message = 'always look on the bright side of life'

# write it to a log
print('Sample log entry (human friendly) \n', dts + ' - ' + hostname + ' : ' + message + '\n' )
log_file.write(dts + ' - ' + hostname + ' : ' + message + '\n')
# ISO format
print('Sample log entry (ISO format) \n', iso_dts + ' - ' + hostname + ' : ' + message + '\n' )
log_file.write(iso_dts + ' - ' + hostname + ' : ' + message + '\n')
