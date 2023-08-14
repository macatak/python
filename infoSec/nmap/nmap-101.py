'''

pip install python-nmap
https://pypi.org/project/python-nmap/

todo
file input (use args?)

'''

import nmap

# http://scanme.nmap.org/
target = 'http://scanme.nmap.org/'
metaspoitableIP = '172.16.0.102'

nm = nmap.PortScanner()
# nm.scan('45.33.32.156')
# nm.scan('45.33.32.156', arguments=" -sV")

# nm.scan(metaspoitableIP, arguments="-sV")
nm.scan(metaspoitableIP, arguments="-p 20-88 -sV")

# print(nm.scaninfo())
print(nm.csv()) # not really csv but semicolon
print(type((nm.csv())))
print(nm[metaspoitableIP]['tcp'].keys())
# print(nm.all_hosts)
# print(nm.scan())
