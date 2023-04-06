"""
three_year_ago = datetime.datetime.now() - datetime.timedelta(days=3*365)

"""

import os
import datetime

from django.core.wsgi import get_wsgi_application
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
from get_crm.models import CRM_Data_Staging, Max_date_Table, EolCertClientTelematics, CRM_Data_Dump

datetime_last_schedule = Max_date_Table.objects.order_by('id').first()

staging_objects_filter = CRM_Data_Staging.objects.filter(data_received_date__gt=datetime_last_schedule.datetime)
obj_staging = staging_objects_filter.values()

for i in obj_staging:
    try:
        ID = i.pop('id')
        created_on = i.pop('created_on')
        modified_on = i.pop('modified_on')

        objects_filter = EolCertClientTelematics.objects.filter(vin=i.pop("chassis_number"))
        if objects_filter.exists():
            objects_filter.update(**i)
            print('staging add', i['staging_id'])
            staging_objects_filter.objects.filter(id=ID).delete()
        else:
            CRM_Data_Dump.objects.create(**i)
            staging_objects_filter.objects.filter(id=ID).delete()
            print('dump add')
    except Exception as e:
        print(str(e))
        pass

datetime_last_schedule.datetime = timezone.now()  # change field
datetime_last_schedule.save()  # this will update only

with open(r'C:\Users\ISHWARA.TTL\Desktop\scheduler 2.txt', 'a+') as f:
    f.write(f"{datetime.datetime.now()}, scheduler 2\n")

