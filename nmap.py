from pprint import pprint

import nmap3
def scan():
    nmap=nmap3.Nmap()
    l1=list()
    results = nmap.nmap_os_detection('192.168.0.217')
    pprint(results)
    #for i in results-2:
     #   print(i)
#
scan()