import nmap3
nmap=nmap3.Nmap()
results = nmap.scan_top_ports("192.168.0.200")
print(results)