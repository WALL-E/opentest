#!/usr/bin/env python3.6

import requests
import time


res = requests.get("https://api.fcoin.com/v2/public/server-time")


server_time = res.json()["data"]
client_time = int(time.time()*1000)

print("remote: %s" % (server_time))
print("local:  %s" % (client_time))
print("offset: %sms" % (server_time - client_time))
