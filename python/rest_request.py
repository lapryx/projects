#!/home/loggenmm/.venv/dev/bin/python

from requests import request
from requests import session
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json
import pandas

hosts = open("hosts.txt","r")

hosts_data = hosts.read()

hosts_list = hosts_data.split("\n")


username = 'adminloggen@vuw.leidenuniv.nl'
url      = 'https://vcenter-wld01.luci.leidenuniv.nl/api/'
#auth = HTTPBasicAuth(username, getpass())


headers = {
}

current_session = session(
)

current_session.auth=(username, getpass())

sessionID = current_session.post(url+"session")


headers = {
        "vmware-api-session-id": json.loads(sessionID.text)
        }

current_session.headers.update(headers)

response = current_session.get(url+"vcenter/vm")

r_json = json.loads(response.text)

vcenter_hosts = []

for entry in r_json:
    vcenter_hosts.append(entry["name"])

print(list(filter(lambda a: a not in vcenter_hosts,hosts_list )))
#response = request(
#    "GET",
#    url+"vcenter/vm/t-luci-020341",
#    headers=headers,
#    auth=
#        )
