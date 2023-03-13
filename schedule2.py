"""
three_year_ago = datetime.datetime.now() - datetime.timedelta(days=3*365)

"""

import os

from django.core.wsgi import get_wsgi_application
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
from get_crm.models import CRM_Data_Staging, Max_date_Table, EolCertClientTelematics, CRM_Data_Dump

datetime_last_schedule = Max_date_Table.objects.order_by('id').first().datetime

obj_staging = CRM_Data_Staging.objects.filter(data_received_date__gt=datetime_last_schedule).values()

for i in obj_staging:
    ID = i.pop('id')
    objects_filter = EolCertClientTelematics.objects.filter(vc_number=i.get("vc_number"))
    if objects_filter.exists():
        i['staging_id'] = ID
        objects_filter.update(**i)
    else:
        CRM_Data_Dump.objects.create(**i)

time_change_obj = Max_date_Table.objects.order_by('id').first()
time_change_obj.datetime = timezone.now()  # change field
time_change_obj.save()  # this will update only
