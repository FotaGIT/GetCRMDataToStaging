from django.utils import timezone

from get_crm.models import CRM_Data_Staging


def normalize_format_name(arg1, arg2):
    if arg1 and arg2:
        return f'{arg1} {arg2}'
    elif arg1:
        return f'{arg1}'
    elif arg2:
        return f'{arg2}'
    else:
        return None


def normalize_format_address(arg1, arg2):
    if arg1 and arg2:
        return f'{arg1}, {arg2}'
    elif arg1:
        return f'{arg1}'
    elif arg2:
        return f'{arg2}'
    else:
        return None


def save_in_database(data):
    while data:
        k = data.pop()
        if k.get("invoice_details"):
            k.update(k.pop("invoice_details"))
        try:
            CRM_Data_Staging.objects.create(
                chassis_number=k.get("CHASSIS_NUM_s"),
                vc_number=k.get("NAME_s"),
                engine_type=k.get("ENGINE_TYPE_s"),
                engine_number=k.get("ENGINE_NUM_s"),
                emission_norm=k.get("EMITION_NOM_s"),
                customer_delivered_date=k.get("VEH_DELDT_dt"),
                lob=k.get("LOB_s"),
                pl=k.get("PL_s"),
                ppl=k.get("PPL_s"),
                physical_status=k.get("CHA_STAT_s"),
                logical_status=k.get("VEH_STATUS_s"),
                dealer_name=k.get("VEHICLE_ORG_s"),
                dealer_code=k.get("DEALERCODE_s"),
                dealer_region=k.get("DLR_REGION_s"),
                dealer_state=k.get("DLRSO_STATE_s"),
                dealer_city=k.get("DLR_CITY_s"),
                customer_name=normalize_format_name(k.get('CON_FSTNAME_s'), k.get('CON_LSTNAME_s')),
                vehicle_account=k.get("VEH_ACCOUNT_s"),
                customer_type=k.get("CON_CUST_SEGMENT_s"),
                customer_ph_no=normalize_format_address(k.get('CON_CELL_PH_NUM_s'), k.get('ACC_MAINPH_NUM_s')),
                customer_state=normalize_format_address(k.get('CA_STATE_s'), k.get('CA_STATE_s')),
                customer_city=normalize_format_address(k.get('CA_CITY_s', ''), k.get('ACC_CITY_s', '')),
                customer_address=normalize_format_address(k.get('CA_ADLINE1_s'), k.get('ACC_ADLINE1_s')),
                driver_name=normalize_format_name(k.get('DRIVER_FIRSTNAME_s'), k.get('DRI_LNAME_s')),
                driver_contact=k.get("DRI_MOBNUM_s"),
                invoice_date=k.get("INVC_dt") or None,
                invoice_number=k.get("INVC_NUM_s") or None,
                invoice_cancle_date=k.get("CANCEL_dt") or None,
                data_received_date=timezone.now(),
            )
        except Exception as e:
            print(e)
    return 'all data saved successfully'
