#!/home/loggenmm/.venv/dev/bin/python

from requests import request
from requests import session
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json
import pandas


hostname = 'p-issc-016435.vuw.leidenuniv.nl'

url      = 'https://puppetca.issc.leidenuniv.nl:8000/puppet/ca'
#auth = HTTPBasicAuth(username, getpass())


headers = {
}

current_session = session(
)

#current_session.auth=(username, getpass())

#sessionID = current_session.post(url+"session")


#headers = {
#        "vmware-api-session-id": json.loads(sessionID.text)
#        }

#current_session.headers.update(headers)

#response = current_session.get(url+"vcenter/vm")

#r_json = json.loads(response.text)

#vcenter_hosts = []


#for entry in r_json:
 #   vcenter_hosts.append(entry["name"])

response = request(
    "GET",
    url,
    headers=headers,

        )
print(response)
