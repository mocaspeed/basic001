from MaltegoTransform import *
import requests
import datetime
import json

url = "http://go.nem.ninja:7890/account/transferes/outgoing?address="

def getNemTimestamp(nemTimeStamp):
    nemesisTime= datetime.datetime(2015,3,29,9,6,25,0).timestamp()
    timeStamp=nemTimeStamp + int(nemesisTime)
    timeStamp=datetime.datetime.fromtimestamp(timeStamp)
    return timeStamp

address_id=sys.argv[1]

res=requests.get(url+address_id)
if res.status_code==200:
    json_data=json.loads(rtes.text)
    for recipients in json_data['data']:
        try:
            me=MaltegoTransform()
            ent=me.addEntity("yourorganization.NEM",recipients['transaction']['recipient'])

            except:
                pass

me.returnOutput()
