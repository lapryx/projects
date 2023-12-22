#!/home/loggenmm/.venv/dev/bin/python

from requests import request
from requests.auth import HTTPBasicAuth
import json
import pandas

csv = 'tmp.csv'
username = 'loggenmm@vuw.leidenuniv.nl'
apikey   = 'ATATT3xFfGF0hB7xzb7pEEA3DPrDQ9knwKSJTPXhykBMt3CmQrEQpboEAHcGmG6xymS8VPfWwvjLIQL0z_al6eNCdMdZrZGtlGamwEr0MGLnwGlt8EUCKKKZY7QD0-Hb6OakR2BBiMKsVe6lsv7bh3wEkujMYRwGW03-OyEj8-P0kp9_M0LP4EM=2489715D'
url      = 'https://universiteitleiden.atlassian.net'
apiPath  = '/wiki/rest/api/content/2295889921?expand=body.storage'
auth = HTTPBasicAuth(username, apikey)


headers = {
        "Accept": "application/json"
}

response = request(
    "GET",
    url+apiPath,
    headers=headers,
    auth=auth
)
response_json = json.loads(response.text)
#print(response.text)
tables = pandas.read_html(response_json["body"]["storage"]["value"])
tables[0].to_csv(csv)

#print(json.dumps(response_json["body"]["storage"]["value"], sort_keys=True, indent=4, separators=(",", ": ")))
#print(json.dumps(response.text))
