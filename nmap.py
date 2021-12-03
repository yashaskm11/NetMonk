from pprint import pprint

import nmap3
import prettyprint
def scan():
    nmap=nmap3.NmapHostDiscovery()
    l1=list()
    results = nmap.nmap_no_portscan("192.168.0.0/24")
    pprint(results)
    for i in results-2:
        print(i)

scan()