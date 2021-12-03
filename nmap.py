from pprint import pprint

import nmap3
import prettyprint
nmap=nmap3.NmapHostDiscovery()

results = nmap.nmap_no_portscan("192.168.0.0/24")
pprint(results)
for i in results:
    print(i)