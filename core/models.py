from django.db import models


# Create your models here.

class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CRM_Data_Staging(Base):
    chassis_number              = models.CharField(max_length=50, null=True, blank=True)
    vc_number                   = models.IntegerField(null=True, blank=True)  #
    engine_type                 = models.CharField(max_length=50, null=True, blank=True)
    engine_number               = models.IntegerField(null=True, blank=True)  #
    emission_norm               = models.CharField(max_length=50, null=True, blank=True)
    customer_delivered_date     = models.DateField(null=True, blank=True)
    lob                         = models.CharField(max_length=50,null=True, blank=True)
    pl                          = models.CharField(max_length=50, null=True, blank=True)
    ppl                         = models.CharField(max_length=50, null=True, blank=True)
    physical_status             = models.CharField(max_length=50, null=True, blank=True)
    logical_status              = models.CharField(max_length=50, null=True, blank=True)
    dealer_name                 = models.CharField(max_length=50, null=True, blank=True)
    dealer_code                 = models.CharField(max_length=50, null=True, blank=True)
    dealer_region               = models.CharField(max_length=50, null=True, blank=True)
    dealer_state                = models.CharField(max_length=50, null=True, blank=True)
    dealer_city                 = models.CharField(max_length=50, null=True, blank=True)
    customer_name               = models.CharField(max_length=50, null=True, blank=True)
    vehicle_account             = models.CharField(max_length=50, null=True, blank=True)
    customer_type               = models.CharField(max_length=50, null=True, blank=True)
    customer_ph_no              = models.CharField(max_length=50, null=True, blank=True)
    customer_state              = models.CharField(max_length=50, null=True, blank=True)
    customer_city               = models.CharField(max_length=50, null=True, blank=True)
    customer_address            = models.CharField(max_length=50, null=True, blank=True)
    driver_name                 = models.CharField(max_length=50, null=True, blank=True)
    driver_contact              = models.IntegerField(null=True, blank=True)    #
    data_received_date          = models.DateTimeField(null=True)

    class Meta:
        managed = False
        db_table = 'CRM_Data_Staging'


class Max_date_Table(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Max_date_Table'

'''
class CrmDataStaging(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_on = models.DateTimeField()
    modified_on = models.DateTimeField()
    chassis_number = models.CharField(max_length=50, blank=True, null=True)
    vc_number = models.IntegerField(blank=True, null=True)
    engine_type = models.CharField(max_length=50, blank=True, null=True)
    engine_number = models.IntegerField(blank=True, null=True)
    emission_norm = models.CharField(max_length=50, blank=True, null=True)
    customer_delivered_date = models.DateField(blank=True, null=True)
    lob = models.CharField(max_length=50, blank=True, null=True)
    pl = models.CharField(max_length=50, blank=True, null=True)
    ppl = models.CharField(max_length=50, blank=True, null=True)
    physical_status = models.CharField(max_length=50, blank=True, null=True)
    logical_status = models.CharField(max_length=50, blank=True, null=True)
    dealer_name = models.CharField(max_length=50, blank=True, null=True)
    dealer_code = models.CharField(max_length=50, blank=True, null=True)
    dealer_region = models.CharField(max_length=50, blank=True, null=True)
    dealer_state = models.CharField(max_length=50, blank=True, null=True)
    dealer_city = models.CharField(max_length=50, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    vehicle_account = models.CharField(max_length=50, blank=True, null=True)
    customer_type = models.CharField(max_length=50, blank=True, null=True)
    customer_ph_no = models.CharField(max_length=50, blank=True, null=True)
    customer_state = models.CharField(max_length=50, blank=True, null=True)
    customer_city = models.CharField(max_length=50, blank=True, null=True)
    customer_address = models.CharField(max_length=50, blank=True, null=True)
    driver_name = models.CharField(max_length=50, blank=True, null=True)
    driver_contact = models.IntegerField(blank=True, null=True)
    data_received_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CRM_Data_Staging'

'''