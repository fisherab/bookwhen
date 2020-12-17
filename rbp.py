#!/bin/env python
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime, date
with open("key.txt","r") as f:
    key = f.readline().strip()
baseurl = "https://api.bookwhen.com/v2/"
auth = HTTPBasicAuth(key ,"")
response = requests.get(baseurl+"events?filter[tag]=RealBridge&filter[from]=20200101&filter[to]="+date.today().strftime("%Y%m%d"),auth=auth)
output = json.loads(response.content)
with open("bw.csv","w") as ofile:
    print('Date','Name','Tickets', sep=",", file=ofile)
    for datum in output['data']:
        attributes = datum['attributes']
        title=attributes['title']
        start_at = datetime.fromisoformat(attributes['start_at']).date()
        attendee_count = attributes['attendee_count']
        print(start_at, title, attendee_count, sep=",", file=ofile)
