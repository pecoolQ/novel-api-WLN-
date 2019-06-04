import requests
import json
from pprint import pprint
import time
import sys
name = input("novel name:")
# request name search 
url = "https://www.wlnupdates.com/api" 
header = {"Content-Type" : 'application/json'} 
d_p = {"title" : name, "mode": "search-title"}
response = requests.post( url, json=d_p)
data_load = response.json()



# put all name id on a list(results_list_id)
sys.stdout.write("fetching data: \t")
sys.stdout.write("[")

results_list_id = []

for i in data_load['data']['results'] :
    results_list_id.append(i['sid'])


response_id = {}
# fetch series data 
for  i, sid in  enumerate(results_list_id):
    sys.stdout.write("=")
    payload_id = { "mode" : "get-series-data" , "id" : sid}
    rest = requests.post(url , json=payload_id)
    response_id[i] = rest.json()
    time.sleep(0.5)
    
sys.stdout.write("]")
sys.stdout.flush()
print("\n\nData:")
# print title chapter 
for i,x in enumerate(response_id):
    print(str(response_id[i]['data']['title']) + "\tChapter:\t" + str(response_id[i]['data']['latest_chapter']))
