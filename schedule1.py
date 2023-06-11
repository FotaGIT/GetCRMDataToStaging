"""
CV = Project
"""
import datetime
import json
import math
import os

import requests
from django.core.wsgi import get_wsgi_application
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
from get_crm.models import ExceptionGetCRMDataToStaging, Max_date_Table
from utils import save_in_database

# url = "https://skindevreplica.api.tatamotors/api/cv/fota_campaign/get_details/" # development
url = "https://skinprod.api.tatamotors/api/cv/fota_campaign/get_details/" # production
headers = {'Authorization': 'Bearer uW5opVREeJWnptG0ETfas8asd8h', 'Content-Type': 'application/json'}

datetime_last_schedule = Max_date_Table.objects.order_by('id').first()
today_date = datetime_last_schedule.datetime.strftime("%d-%m-%Y %H:%M:%S")

try:
    date_offset_ = {"from_date": "11-06-2023 04:00:00", "offset": 0}
    payload = json.dumps(date_offset_)
    response = requests.request("POST", url, headers=headers, data=payload)
    try:
        data = json.loads(response.text).get("data")
        print(0, save_in_database(data))
    except Exception as e:
        ExceptionGetCRMDataToStaging.objects.create(payload=payload, response=response.text, url=url, error=str(e))
except Exception as e:
    ExceptionGetCRMDataToStaging.objects.create(payload=payload, response=response.text, url=url, error=str(e))

datetime_last_schedule.datetime = timezone.now()  # change field
datetime_last_schedule.save()  # this will update only

total_count = json.loads(response.text).get("total_count", 0)
total_count_round_number = (math.ceil(total_count / 20) * 20) + 20


for num in range(20, total_count_round_number, 20):
    try:
        date_offset_.update(offset=num)
        payload = json.dumps(date_offset_)
        response = requests.request("POST", url, headers=headers, data=payload)
        try:
            list_data = json.loads(response.text).get("data")
            print(num, save_in_database(list_data))
        except Exception as e:
            ExceptionGetCRMDataToStaging.objects.create(payload=payload, response=response.text, url=url, error=str(e))
    except Exception as e:
        ExceptionGetCRMDataToStaging.objects.create(payload=payload, response=None, url=url, error=str(e))

with open(r'C:\Users\ISHWARA.TTL\Desktop\scheduler 1.txt', 'a+') as f:
    f.write(f"{datetime.datetime.now()}, scheduler 1\n")
