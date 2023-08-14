'''
pip install python3-nmap
https://pypi.org/project/python3-nmap/
'''

import nmap3


# http://scanme.nmap.org/
target = "45.33.32.156"
# port = 


nmap = nmap3.Nmap()

# results = nmap.scan_top_ports("45.33.32.156")
# custom
results = nmap.scan_top_ports("45.33.32.156", args="-p 22-443 -sV")
# print(results)
print(type(results))

# dictionary info
# get the keys
nmapDict_keys = results.keys()
# print(nmapDict_keys)
# get the values
nmapDict_values = results.values()
# print(nmapDict_values)

for key, value in results.items():
    # print(key,"--->", value)
    print('')

# convert to tuples

nmap2tuples = [(key, value) for key, value in results.items()]
print(nmap2tuples)