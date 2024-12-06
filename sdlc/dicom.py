# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:00:16 2024

@author: 11107045
"""

import requests
import json
patientsurl = "http://40.81.30.76:8042/patients/"
studiesurl = "http://40.81.30.76:8042/studies/"
seriesurl = "http://40.81.30.76:8042/series/"
instancesurl = "http://40.81.30.76:8042/instances/"
payload = {}
headers = {
  'Authorization': 'Basic b3J0aGFuYzpvcnRoYW5j'
}

patientresponse = requests.request("GET", patientsurl, headers=headers, data=payload)
patientsurljson=json.loads(patientresponse.text)
print(patientsurljson)

studiesresponse = requests.request("GET", studiesurl, headers=headers, data=payload)
studiesjson=json.loads(studiesresponse.text)
print(studiesjson)

seriesresponse = requests.request("GET", seriesurl, headers=headers, data=payload)
seriesurljson=json.loads(seriesresponse.text)
print(seriesurljson)

instancesresponse = requests.request("GET", instancesurl, headers=headers, data=payload)
instancesurljson=json.loads(instancesresponse.text)
print(instancesurljson)