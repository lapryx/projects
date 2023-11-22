#!/usr/bin/python

from requests import request
from requests.auth import HTTPBasicAuth
import json
username = 'loggenmm@vuw.leidenuniv.nl'
apikey   = 'ATATT3xFfGF0vdC0QNVdjRhqJi43yMUSSk0jsmEU_l4bvkC-DIqrWXS_qMLk3W_j96oKIvHztUwIlqR5PnCG7CMTjjN2Ity_RpodMmsXkwlK5WJ1rrHZpxrXrU3ojl-4PfYH3lBVWgZwKsqTxv4JjAH4qu3tYJ2iVhdl0hf8GuhG1Blu06yl1fE=FB82EC70'
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

#print(response)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
