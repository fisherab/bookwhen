#!/bin/env python
import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime, date, timedelta
with open("key.txt","r") as f:
    key = f.readline().strip()
baseurl = "https://api.bookwhen.com/v2/"
today = date.today()
firstOfMonth = today.replace(day=1)
lastOfPreviousMonth = firstOfMonth - timedelta(days=1)
firstOfPreviousMonth = lastOfPreviousMonth.replace(day=1)
dfrom = firstOfPreviousMonth.strftime("%Y%m%d")
dto = lastOfPreviousMonth.strftime("%Y%m%d")

url = baseurl+"events?filter[tag]=RealBridge&filter[from]="+dfrom+"&filter[to]="+dto
auth = HTTPBasicAuth(key ,"")
with open("bw.csv","w") as ofile:
    print('Date','Name','Tickets', sep=",", file=ofile)
    while True:
        response = requests.get(url,auth=auth)
        output = json.loads(response.content)
        for datum in output['data']:
            attributes = datum['attributes']
            title=attributes['title']
            start_at = datetime.fromisoformat(attributes['start_at']).date()
            attendee_count = attributes['attendee_count']
            print(start_at, title, attendee_count, sep=",", file=ofile)
        links = output['links']
        if 'next' not in links: break
        url = links['next']
