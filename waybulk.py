import requests
import json

with open('domains.txt','r') as f:
	domains = f.readlines()
	domains = [x.rstrip() for x in domains]

for domain in domains:

	response=requests.get("http://archive.org/wayback/available?url=" + domain)
	if response.status_code==200:
		data=response.json()
		if(len(data["archived_snapshots"]) != 0):
			print("[+]"+data["archived_snapshots"]["closest"]["url"]) 

