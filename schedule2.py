import os
import datetime

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()

from get_crm.models import CRM_Data_Staging, Max_date_Table, EolCertClientTelematics
# three_year_ago = datetime.datetime.now() - datetime.timedelta(days=3*365)

datetime_last_schedule  = Max_date_Table.objects.order_by('id').first().datetime

obj_staging = CRM_Data_Staging.objects.filter(data_received_date__gt=datetime_last_schedule).values()

print(obj_staging)

# for i in obj_staging:
#     i['staging_id'] = i.pop('id')
#     EolCertClientTelematics.objects.filter().update(**i)
