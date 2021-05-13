#!/usr/bin/env python3

try:
  import requests
except ImportError as exc:
  print(exc.msg)
  exit(1)

req = requests.get('https://pypi.org/pypi/ansible-core/json')

print('Current ansible-core version is {}'.format(req.json()['info']['version']))
