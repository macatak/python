import nmapthon as nm

metasploitable = '192.168.56.105'

# scanner = nm.NmapScanner('192.168.1.0/24', ports='22,53,443', arguments='-sV -T4')
scanner = nm.NmapScanner(metasploitable, arguments='-sV -T4')
scanner.run()

# for every host scanned
for host in scanner.scanned_hosts():
    # for every protocol scanned for each host
    for proto in scanner.all_protocols(host):
        # for each scanned port
        for port in scanner.scanned_ports(host, proto):
            # Get service information
            service, service_info = scanner.standard_service_info(host, proto, port)
            if service is not None:
                print("Port:{} Service: {}\tInfo: {}".format(port, service, service_info))

