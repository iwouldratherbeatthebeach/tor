#!/usr/local/bin/python
#Written by Aaron Johnsen
import requests
import os
import re
import csv
#This script is used to gather live Tor exit nodes from torproject.org
print ('Pulling IPs Now')
sleep = 2
# Pulls the IPs from an official Tor website
ipPull = requests.get("https://check.torproject.org/exit-addresses", allow_redirects=False, verify=False).text
r = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ipPull)
#Writes the IPs to a CSV file
q = "tor_ip"
f = open("tor.csv", "w")
csvwriter = csv.writer(f, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow([q])
for IPAddr in r:
    csvwriter.writerow([IPAddr])
f.close()
sleep = 2
print ('IPs Pulled Successfully')