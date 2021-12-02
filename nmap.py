import nmap3
nmap=nmap3.NmapHostDiscovery()
results = nmap.nmap_no_portscan("192.168.0.0/24")
for i in results:
    print(i)