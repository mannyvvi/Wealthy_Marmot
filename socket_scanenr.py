import nmap
n = nmap.PortScanner()
n.scan(hosts='192.168.1.0/24', arguments='-0')
for h in nm.all_hosts():
    if 'mac' in nm[h]['addresses']:
        print(nm[h]['addresses'], nm[h]['vendor'])
