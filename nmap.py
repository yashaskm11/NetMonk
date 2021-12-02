import nmap3
nmap=nmap3.NmapHostDiscovery()
results = nmap.nmap_arp_discovery("192.168.0.*")
print(results)