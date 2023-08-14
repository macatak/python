import nmapthon as nm

# metasploitable
metasploitable = '192.168.56.105'

# This instantiates a scanner for localhost and Service Detection on default ports
scanner = nm.NmapScanner(metasploitable, arguments='-sV')

# example_scanner = nm.NmapScanner(target='127.0.0.1', arguments='-sS')

# Execute the scan
try:
    scanner.run()
except nm.NmapScanError as e:
    print('Catching all scan errors!: {}'.format(e))

# Now the 'scanner' object contains all the information from the scan.