'''
dictionary 101
'''
# several ways, this is one
metasploitable = {
    '21' : 'vsftpd 2.3.4',
    '22' : 'OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)',
    '23' : 'Linux telnetd',
    '25' : 'Postfix smtpd'
}

print(metasploitable['21'])

# add to dict
metasploitable['53'] = 'BIND 9.4.2'
print(metasploitable['53'])
# update it 
metasploitable['53'] = 'ISC BIND 9.4.2'
print(metasploitable['53'])

# get all the items
print(metasploitable.items())

# check if somethingis there
if '53' in metasploitable:
    print('possible DNS')

# get the keys
print(metasploitable.keys())
# get the values
print(metasploitable.values())