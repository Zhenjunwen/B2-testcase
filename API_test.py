import requests
import json
import datetime
import urllib
import hashlib
import time

class RunMain:
    def __init__(self,url,params,data,headers,method):
        self.response = self.run_main(url,params,data,headers,method)

    def send_post(self,url,data,headers):
        response = requests.post(url=url,data=data,headers=headers).json()
        return json.dumps(response,sort_keys=True,indent=4)

    def send_get(self,url,params,headers):
        response = requests.get(url=url,params=params,headers=headers).json()
        return json.dumps(response,sort_keys=True,indent=4)

    def run_main(self,url,params,data,headers,method):
        respose = None
        if method == 'GET':
            respose = self.send_get(url,params,headers)
        else:
            respose = self.send_post(url,data,headers)
        return respose

if __name__ == "__main__":
    pass





