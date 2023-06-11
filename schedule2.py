"""
three_year_ago = datetime.datetime.now() - datetime.timedelta(days=3*365)

"""
import os
import datetime

from django.core.wsgi import get_wsgi_application
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
from get_crm.models import CRM_Data_Staging, EolCertClientTelematics, CRM_Data_Dump

staging_objects_filter = CRM_Data_Staging.objects.all()
obj_staging = staging_objects_filter.values()

for i in obj_staging:
    try:
        ID = i.pop('id')
        created_on = i.pop('created_on')
        modified_on = i.pop('modified_on')
        chassis_number = i.pop("chassis_number")

        objects_filter = EolCertClientTelematics.objects.filter(vin=chassis_number)
        if objects_filter.exists():
            objects_filter.update(**i)
            print('staging add', chassis_number)
        else:
            CRM_Data_Dump.objects.create(**i)
            print('dump add', chassis_number)
    except Exception as e:
        print(e)
    else:
        staging_objects_filter.filter(id=ID).delete()


with open(r'C:\Users\ISHWARA.TTL\Desktop\scheduler 2.txt', 'a+') as f:
    f.write(f"{datetime.datetime.now()}, scheduler 2\n")

