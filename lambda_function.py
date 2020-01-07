import requests
import json
import os
import subprocess

def lambda_handler(event, context):
  url = event['url']
  api_res = requests.get(url)
  data = api_res.json()

  node = event['node']
  message = event['message'] + '\n'
  for i in range(10):
    item = data[node][i]
    rank = str(i+1)
    message = message + rank + '位: ' + item['title'] + '\n'

  print(message)

  WEBHOOK_URL = os.environ['WEBHOOK_URL']
  requests.post(WEBHOOK_URL, data = json.dumps({
    'text': message,
    'username': u'Trend bot',
    'icon_emoji': u':filmarks:',
    'link_names': 1,
  }))
