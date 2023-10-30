def  generate_query_from_file_real_iranian(file):
    with open(file,'r') as file:
        input = file.readlines()
    input = [input[x].strip() for x in range(len(input))]
    file.close()
    total_query = '------------{0}-----------------'
    for i in range(0,len(input)):
        select_ip_id = f'(SELECT ID from CRM.TB_INVOLVED_PARTY where NATIONAL_CODE_NATIONAL_ID = {input[i]})'    
        select_cif_siba_1_update_query = f'UPDATE SIBA.TB_CIF_SIBA1 t SET t.SHAHAB_CODE =  null, t.TRANSFER_STATUS_CODE = null, t.TRANSFER_DATE = null, t.USR_TRANSFER_NATIONAL_CODE = null, t.FK_IP_TRANSFER = null WHERE t.FK_IP_TRANSFER = {select_ip_id}'
        select_ip_role_query_id = f'SELECT id from CRM.TB_IPROLE where FK_IP_INPR_ID = {select_ip_id}'
        select_ip_customer_query_string = f'SELECT * from CRM.TB_IP_CUSTOMER where FK_IPL = ({select_ip_role_query_id})'
        select_ip_customer_query_id = f'SELECT id from CRM.TB_IP_CUSTOMER where FK_IPL = ({select_ip_role_query_id})'
        select_customer_service_query_string = f'SELECT * from CRM.TB_CUSTOMER_SERVICE where FK_ICS = ({select_ip_customer_query_id})'
        select_cust_siba_query_string = f'SELECT * from CRM.TB_CUST_SIBA where FK_ICS = ({select_ip_customer_query_id})'
        select_ip_role_query_string = f'SELECT * from CRM.TB_IPROLE where FK_IP_INPR_ID = {select_ip_id}'
        select_log_query_string = f'SELECT * from LOG.TB_LOG where FK_IP = {select_ip_id}'
        select_contact_preference_query_string = f'SELECT * from CRM.TB_CONTACT_PREFERENCE where FK_IP_INVOLVED_PARTY = {select_ip_id}'
        select_contact_point_query_string = f'SELECT * from CRM.TB_CONTACT_POINT where FK_IP_ID = {select_ip_id}'
        select_contact_point_aud_query_string = f'SELECT * from CRM.TB_CONTACT_POINT_AUD where FK_IP_ID = {select_ip_id}'
        select_image_reference_query_string = f'SELECT * from CRM.TB_IMAGE_REFERENCE where FK_IP_ID = {select_ip_id}'
        select_deficiency_flag_query_string = f'SELECT * from CRM.TB_DEFICIENCY_INFORMATION_FLAGS where FK_IP = {select_ip_id}'
        select_individual_query_string = f'SELECT * from CRM.TB_INDIVIDUAL where ID = {select_ip_id}'
        select_individual_query_id = f'SELECT id from CRM.TB_INDIVIDUAL where ID = {select_ip_id}'
        select_individual_aud_query_string = f'SELECT * from CRM.TB_INDIVIDUAL_AUD where ID = {select_ip_id}'
        select_individual_det_query_string = f'SELECT * from CRM.TB_INDIVIDUAL_DETAIL where FK_INC_INDIVIDUAL_ID = ({select_individual_query_id})'
        select_individual_det_aud_query_string = f'SELECT * from CRM.TB_INDIVIDUAL_DETAIL_AUD where FK_INC_INDIVIDUAL_ID = ({select_individual_query_id})'
        select_ip_query_string = f'SELECT * from CRM.TB_INVOLVED_PARTY where ID = {select_ip_id}'
        
        ip_id = f'(SELECT ID from CRM.TB_INVOLVED_PARTY where NATIONAL_CODE_NATIONAL_ID = {input[i]})'    
        cif_siba_1_update_query = f'UPDATE SIBA.TB_CIF_SIBA1 t SET t.SHAHAB_CODE =  null ,t.TRANSFER_STATUS_CODE =  null ,t.TRANSFER_DATE = null,t.USR_TRANSFER_NATIONAL_CODE = null , t.FK_IP_TRANSFER = null WHERE t.FK_IP_TRANSFER = {ip_id}'
        ip_role_query_id = f'SELECT id from CRM.TB_IPROLE where FK_IP_INPR_ID = {ip_id}'
        ip_customer_query_string = f'delete from CRM.TB_IP_CUSTOMER where FK_IPL = ({ip_role_query_id})'
        ip_customer_query_id = f'SELECT id from CRM.TB_IP_CUSTOMER where FK_IPL = ({ip_role_query_id})'
        customer_service_query_string = f'delete from CRM.TB_CUSTOMER_SERVICE where FK_ICS = ({ip_customer_query_id})'
        cust_siba_query_string = f'delete from CRM.TB_CUST_SIBA where FK_ICS = ({ip_customer_query_id})'
        ip_role_query_string = f'delete from CRM.TB_IPROLE where FK_IP_INPR_ID = {ip_id}'
        log_query_string = f'delete from LOG.TB_LOG where FK_IP = {ip_id}'
        contact_preference_query_string = f'delete from CRM.TB_CONTACT_PREFERENCE where FK_IP_INVOLVED_PARTY = {ip_id}'
        contact_point_query_string = f'delete from CRM.TB_CONTACT_POINT where FK_IP_ID = {ip_id}'
        contact_point_aud_query_string = f'delete from CRM.TB_CONTACT_POINT_AUD where FK_IP_ID = {ip_id}'
        image_reference_query_string = f'delete from CRM.TB_IMAGE_REFERENCE where FK_IP_ID = {ip_id}'
        deficiency_flag_query_string = f'delete from CRM.TB_DEFICIENCY_INFORMATION_FLAGS where FK_IP = {ip_id}'
        inquiry_status_query_string = f'delete from CRM.TB_INQUIRIES_STATUS_SERVICE where FK_IP = {ip_id}'
        ip_ip_relationship_1_query_string = f'delete from CRM.TB_IP_IP_RELATIONSHIP where FK_IP_INPR_ID1 = {ip_id}'
        ip_ip_relationship_2_query_string = f'delete from CRM.TB_IP_IP_RELATIONSHIP where FK_IP_INPR_ID2 = {ip_id}'
        individual_query_string = f'delete from CRM.TB_INDIVIDUAL where ID = {ip_id}'
        individual_query_id = f'SELECT id from CRM.TB_INDIVIDUAL where ID = {ip_id}'
        individual_aud_query_string = f'delete from CRM.TB_INDIVIDUAL_AUD where ID = {ip_id}'
        individual_det_query_string = f'delete from CRM.TB_INDIVIDUAL_DETAIL where FK_INC_INDIVIDUAL_ID = ({individual_query_id})'
        individual_det_aud_query_string = f'delete from CRM.TB_INDIVIDUAL_DETAIL_AUD where FK_INC_INDIVIDUAL_ID = ({individual_query_id})'
        ip_query_string = f'delete from CRM.TB_INVOLVED_PARTY where ID = {ip_id}'
        total_query = total_query + '\n' + cust_siba_query_string + ';' +'\n' + customer_service_query_string + ';' + '\n' + ip_customer_query_string  + ';' + '\n' +  ip_role_query_string  + ';' + '\n' + log_query_string  + ';' + '\n' + contact_preference_query_string  + ';' + '\n' + contact_point_aud_query_string  + ';' +  '\n' + contact_point_query_string  + ';' + '\n' + image_reference_query_string  + ';' + '\n' + deficiency_flag_query_string + ';' + '\n' + individual_det_aud_query_string  + ';' + inquiry_status_query_string + ';' + ip_ip_relationship_1_query_string + ';' + ip_ip_relationship_2_query_string  + '\n' + individual_det_query_string  + ';' + '\n' + individual_aud_query_string  + ';' + '\n' + individual_query_string  + ';' + '\n'+  ip_query_string  + ';' + '\n' +cif_siba_1_update_query  + ';' + '\n'+ f'------------{i+1}-----------------' 
    with open('d:/new2_result.txt','a+') as file:
        file.write(total_query)
        
        
def  generate_query_from_natCode(nationalCode)  :
        total_query = ''
        ip_id = f'(SELECT ID from CRM.TB_INVOLVED_PARTY where NATIONAL_CODE_NATIONAL_ID = {nationalCode})'    
        ip_role_query_id = f'SELECT id from CRM.TB_IPROLE where FK_IP_INPR_ID ={ip_id}'
        ip_customer_query_string = f'delete from CRM.TB_IP_CUSTOMER where FK_IPL = ({ip_role_query_id})'
        ip_customer_query_id = f'SELECT id from CRM.TB_IP_CUSTOMER where FK_IPL = ({ip_role_query_id})'
        customer_service_query_string = f'delete from CRM.TB_CUSTOMER_SERVICE where FK_ICS = ({ip_customer_query_id})'
        cust_siba_query_string = f'delete from CRM.TB_CUST_SIBA where FK_ICS = ({ip_customer_query_id})'
        cif_siba_1_update_query = f'UPDATE SIBA.TB_CIF_SIBA1 t SET t.SHAHAB_CODE = null , t.TRANSFER_STATUS_CODE = null ,t.TRANSFER_DATE = null ,t.USR_TRANSFER_NATIONAL_CODE = null , t.FK_IP_TRANSFER = null WHERE t.customer_id in (select customer_no from CRM.TB_CUST_SIBA where FK_ICS = ({ip_customer_query_id}));\n'
        ip_role_query_string = f'delete from CRM.TB_IPROLE where FK_IP_INPR_ID = {ip_id}'
        log_query_string = f'delete from LOG.TB_LOG where FK_IP = {ip_id}'
        contact_preference_query_string = f'delete from CRM.TB_CONTACT_PREFERENCE where FK_IP_INVOLVED_PARTY = {ip_id}'
        contact_point_query_string = f'delete from CRM.TB_CONTACT_POINT where FK_IP_ID = {ip_id}'
        contact_point_aud_query_string = f'delete from CRM.TB_CONTACT_POINT_AUD where FK_IP_ID = {ip_id}'
        image_reference_query_string = f'delete from CRM.TB_IMAGE_REFERENCE where FK_IP_ID = {ip_id}'
        deficiency_flag_query_string = f'delete from CRM.TB_DEFICIENCY_INFORMATION_FLAGS where FK_IP = {ip_id}'
        inquiry_status_query_string = f'delete from CRM.TB_INQUIRIES_STATUS_SERVICE where FK_IP = {ip_id}'
        ip_ip_relationship_1_query_string = f'delete from CRM.TB_IP_IP_RELATIONSHIP where FK_IP_INPR_ID1 = {ip_id}'
        ip_ip_relationship_2_query_string = f'delete from CRM.TB_IP_IP_RELATIONSHIP where FK_IP_INPR_ID2 = {ip_id}'
        individual_query_string = f'delete from CRM.TB_INDIVIDUAL where ID = {ip_id}'
        individual_query_id = f'SELECT id from CRM.TB_INDIVIDUAL where ID = {ip_id}'
        individual_aud_query_string = f'delete from CRM.TB_INDIVIDUAL_AUD where ID = {ip_id}'
        individual_det_query_string = f'delete from CRM.TB_INDIVIDUAL_DETAIL where FK_INC_INDIVIDUAL_ID = ({individual_query_id})'
        individual_det_aud_query_string = f'delete from CRM.TB_INDIVIDUAL_DETAIL_AUD where FK_INC_INDIVIDUAL_ID = ({individual_query_id})'
        ip_rescind_person_query_string = f'delete from CRM.TB_RESCIND_RECORD where FK_IP_RESCIND_PERSON = {ip_id}'
        ip_rescind_candid_query_string = f'delete from CRM.TB_RESCIND_RECORD where FK_IP_CANDIDATE_IP = {ip_id}'
        ip_query_string = f'delete from CRM.TB_INVOLVED_PARTY where national_code_national_id = {nationalCode};'
        total_query = total_query + '\n' + cust_siba_query_string + ';' +'\n' + customer_service_query_string + ';' + '\n' + ip_customer_query_string  + ';' + '\n' +  ip_role_query_string  + ';' + '\n' + log_query_string  + ';' + '\n' + contact_preference_query_string  + ';' + '\n' + contact_point_aud_query_string  + ';' +  '\n' + contact_point_query_string  + ';' + '\n' + image_reference_query_string  + ';' + '\n' + deficiency_flag_query_string + ';' + '\n' + individual_det_aud_query_string  + ';' + '\n' + inquiry_status_query_string + ';' + '\n' + ip_ip_relationship_1_query_string + ';'+ '\n' + ip_ip_relationship_2_query_string + ';' + '\n' + individual_det_query_string  + ';' + '\n' + individual_aud_query_string  + ';' + '\n' + individual_query_string  + ';' + '\n'+  ip_rescind_person_query_string + ';' + '\n' + ip_rescind_candid_query_string + ';' + '\n' +ip_query_string +'\n' + cif_siba_1_update_query
        print(total_query)
        
        
        
def  generate_query_from_fidaCode(fidaCode):
        total_query = ''
        ip_id = f'(SELECT ID from CRM.TB_INVOLVED_PARTY where fida_code = {fidaCode})'    
        ip_role_query_id = f'SELECT id from CRM.TB_IPROLE where FK_IP_INPR_ID = {ip_id}'
        ip_customer_query_string = f'delete from CRM.TB_IP_CUSTOMER where FK_IPL = ({ip_role_query_id});'
        ip_customer_query_id = f'SELECT id from CRM.TB_IP_CUSTOMER where FK_IPL = ({ip_role_query_id})'
        customer_service_query_string = f'delete from CRM.TB_CUSTOMER_SERVICE where FK_ICS = ({ip_customer_query_id});'
        cust_siba_query_string = f'delete from CRM.TB_CUST_SIBA where FK_ICS = ({ip_customer_query_id});'
        cif_siba_1_update_query = f'UPDATE SIBA.TB_CIF_SIBA1 t SET t.SHAHAB_CODE = null , t.TRANSFER_STATUS_CODE = null ,t.TRANSFER_DATE = null ,t.USR_TRANSFER_NATIONAL_CODE = null , t.FK_IP_TRANSFER = null WHERE t.customer_id in (select customer_no from CRM.TB_CUST_SIBA where FK_ICS = ({ip_customer_query_id}));\n'
        ip_role_query_string = f'delete from CRM.TB_IPROLE where FK_IP_INPR_ID = {ip_id};'
        log_query_string = f'delete from LOG.TB_LOG where FK_IP = {ip_id};'
        contact_preference_query_string = f'delete from CRM.TB_CONTACT_PREFERENCE where FK_IP_INVOLVED_PARTY = {ip_id};'
        contact_point_query_string = f'delete from CRM.TB_CONTACT_POINT where FK_IP_ID = {ip_id};'
        contact_point_aud_query_string = f'delete from CRM.TB_CONTACT_POINT_AUD where FK_IP_ID = {ip_id};'
        image_reference_query_string = f'delete from CRM.TB_IMAGE_REFERENCE where FK_IP_ID = {ip_id};'
        deficiency_flag_query_string = f'delete from CRM.TB_DEFICIENCY_INFORMATION_FLAGS where FK_IP = {ip_id};'
        inquiry_status_query_string = f'delete from CRM.TB_INQUIRIES_STATUS_SERVICE where FK_IP = {ip_id};'
        ip_ip_relationship_1_query_string = f'delete from CRM.TB_IP_IP_RELATIONSHIP where FK_IP_INPR_ID1 = {ip_id};'
        ip_ip_relationship_2_query_string = f'delete from CRM.TB_IP_IP_RELATIONSHIP where FK_IP_INPR_ID2 = {ip_id};'
        ip_document_item_aud_query_string = f'delete from CRM.TB_DOCUMENT_EXPIRATION_INFO_AUD where FK_IP = {ip_id};'
        ip_document_item_query_string = f'delete from CRM.TB_DOCUMENT_EXPIRATION_INFO where FK_IP = {ip_id};'
        individual_query_string = f'delete from CRM.TB_INDIVIDUAL where ID = {ip_id};'
        individual_query_id = f'SELECT id from CRM.TB_INDIVIDUAL where ID = {ip_id}'
        individual_aud_query_string = f'delete from CRM.TB_INDIVIDUAL_AUD where ID = {ip_id};'
        individual_det_query_string = f'delete from CRM.TB_INDIVIDUAL_DETAIL where FK_INC_INDIVIDUAL_ID = ({individual_query_id});'
        individual_det_aud_query_string = f'delete from CRM.TB_INDIVIDUAL_DETAIL_AUD where FK_INC_INDIVIDUAL_ID = ({individual_query_id});'
        ip_rescind_rec_query_string = f'delete from CRM.TB_RESCIND_RECORD where FK_IP_RESCIND_PERSON = {ip_id};'
        ip_rescind_candid_query_string = f'delete from CRM.TB_RESCIND_RECORD where FK_IP_CANDIDATE_IP = {ip_id};'
        ip_query_string = f'delete from CRM.TB_INVOLVED_PARTY where fida_code = {fidaCode};'
        total_query = total_query +'\n'+ cust_siba_query_string +'\n'+ customer_service_query_string +'\n'+ ip_customer_query_string +'\n'+ ip_role_query_string +'\n'+ log_query_string +'\n'+ contact_preference_query_string +'\n'+ contact_point_aud_query_string +'\n'+ contact_point_query_string +'\n'+ image_reference_query_string +'\n'+ deficiency_flag_query_string +'\n'+ individual_det_aud_query_string +'\n'+ inquiry_status_query_string +'\n'+ ip_ip_relationship_1_query_string +'\n' + ip_ip_relationship_2_query_string +'\n'+ individual_det_query_string +'\n'+ individual_aud_query_string  +'\n'+ individual_query_string +'\n'+ ip_rescind_rec_query_string +'\n'+ ip_rescind_candid_query_string +'\n'+ ip_document_item_aud_query_string +'\n'+ ip_document_item_query_string +'\n'+ ip_query_string +'\n' + cif_siba_1_update_query
        print(total_query)


if __name__ == '__main__':
    # define host and port numbers to scan
    # test the ports
    #generate_query_from_natCode("'3254173848'")
    generate_query_from_fidaCode("'104144527678'")
