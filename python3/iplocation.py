#!/usr/bin/python3
import urllib.request, json

access_token = "changeme" #Your justreqit access_token...

def ip_location(ip):
	api_url = "https://justreqit.com/api/ipv4/%s/?access_token=%s" % (ip, access_token)
	response = json.loads(urllib.request.urlopen(api_url).read())
	if (response["status"] == "success"):
		return "%s, %s" % (response["results"]["city"], response["results"]["state"])
	else:
		return None

#example 
print(ip_location("140.82.112.3"))