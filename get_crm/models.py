from django.db import models

class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CRM_Data_Staging(Base):
    chassis_number              = models.CharField(max_length=50, null=True, blank=True)
    vc_number                   = models.CharField(max_length=50, null=True, blank=True)  #
    engine_type                 = models.CharField(max_length=50, null=True, blank=True)
    engine_number               = models.CharField(max_length=50, null=True, blank=True)  #
    emission_norm               = models.CharField(max_length=50, null=True, blank=True)
    customer_delivered_date     = models.DateTimeField(null=True, blank=True)
    lob                         = models.CharField(max_length=50,null=True, blank=True)
    pl                          = models.CharField(max_length=50, null=True, blank=True)
    ppl                         = models.CharField(max_length=50, null=True, blank=True)
    physical_status             = models.CharField(max_length=50, null=True, blank=True)
    logical_status              = models.CharField(max_length=100, null=True, blank=True)
    dealer_name                 = models.CharField(max_length=50, null=True, blank=True)
    dealer_code                 = models.CharField(max_length=50, null=True, blank=True)
    dealer_region               = models.CharField(max_length=50, null=True, blank=True)
    dealer_state                = models.CharField(max_length=50, null=True, blank=True)
    dealer_city                 = models.CharField(max_length=50, null=True, blank=True)
    customer_name               = models.CharField(max_length=100, null=True, blank=True)
    vehicle_account             = models.CharField(max_length=50, null=True, blank=True)
    customer_type               = models.CharField(max_length=50, null=True, blank=True)
    customer_ph_no              = models.CharField(max_length=50, null=True, blank=True)
    customer_state              = models.CharField(max_length=100, null=True, blank=True)
    customer_city               = models.CharField(max_length=100, null=True, blank=True)
    customer_address            = models.TextField(null=True, blank=True)
    driver_name                 = models.CharField(max_length=100, null=True, blank=True)
    driver_contact              = models.CharField(max_length=50, null=True, blank=True)    #
    invoice_date                = models.DateTimeField(null=True, blank=True)
    invoice_number              = models.CharField(max_length=50, null=True, blank=True)
    invoice_cancle_date         = models.DateTimeField(null=True, blank=True)
    data_received_date          = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'CRM_Data_Staging'


class Max_date_Table(models.Model):
    datetime = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Max_date_Table'
