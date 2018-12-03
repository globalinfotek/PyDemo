import requests
import pprint
import time
import threading

from source.application_details import ApplicationDetails
from source.json_converter import JsonConverter


class UpdateService:
    _URL = 'http://demo-update-api-devops.b9ad.pro-us-east-1.openshiftapps.com/updates'
    _HEADERS = {'Content-type': 'application/json'}

    def __init__(self):
        pass

    # Creates a JSON message and posts that message to the updates API.
    def post_update(self):
        app_details = JsonConverter.convert(ApplicationDetails())
        pprint.pprint(time.ctime())
        pprint.pprint("Publishing :" + app_details + ":To:" + UpdateService._URL)
        response = requests.post(UpdateService._URL, data=app_details, headers=UpdateService._HEADERS)
        pprint.pprint(response)
        timer = threading.Timer(5, self.post_update)
        timer.start()
        return timer
