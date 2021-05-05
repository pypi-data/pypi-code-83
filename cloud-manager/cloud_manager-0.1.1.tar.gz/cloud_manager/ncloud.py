import ncloud_server
from ncloud_server.api.v2_api import V2Api
from ncloud_server.rest import ApiException


class NCloud(V2Api):
    def __init__(self, input_access_key: str, input_secret_key: str):

        configuration = ncloud_server.Configuration()
        configuration.access_key = input_access_key
        configuration.secret_key = input_secret_key
        super().__init__(ncloud_server.ApiClient(configuration))

    def new_get_image_list_info(self):
        try:
            tmp_request = ncloud_server.GetMemberServerImageListRequest()
            tmp_dict = self.get_member_server_image_list(tmp_request).to_dict()
            return tmp_dict["member_server_image_list"]
        except ApiException as e:
            print("Exception when calling V2Api->get_image_list: %s\n" % e)

    def new_get_login_key_list_as_dict(self):
        try:
            get_login_key_list_request = ncloud_server.GetLoginKeyListRequest()
            api_response = self.get_login_key_list(get_login_key_list_request)
            return api_response.to_dict()
        except ApiException as e:
            print("Exception when calling V2Api->get_login_key_list: %s\n" % e)

    def new_get_instance_info(self):
        tmp_result_dict = dict()
        tmp_request = ncloud_server.GetServerInstanceListRequest()
        tmp_list = self.get_server_instance_list(tmp_request).to_dict()["server_instance_list"]
        for tmp_server in tmp_list:
            tmp_dict = dict()
            tmp_dict["server_instance_no"] = tmp_server["server_instance_no"]
            tmp_dict["create_date"] = tmp_server["create_date"]
            tmp_dict["uptime"] = tmp_server["uptime"]
            tmp_dict["private_ip"] = tmp_server["private_ip"]
            tmp_dict["server_instance_type"] = tmp_server["server_instance_type"]["code_name"]
            tmp_dict["server_instance_status_name"] = tmp_server["server_instance_status_name"]
            tmp_result_dict[tmp_server["server_name"]] = tmp_dict
        return tmp_result_dict

    def new_get_dict_form4creation_instance(self, cralwer=None):
        tmp_dict = {'server_image_product_code': None,
                    'server_product_code': None,
                    'member_server_image_no': None,
                    'server_name': None,
                    'server_description': None,
                    'login_key_name': None,
                    'is_protect_server_termination': None,
                    'server_create_count': None,
                    'server_create_start_no': None,
                    'internet_line_type_code': None,
                    'fee_system_type_code': None,
                    'user_data': None,
                    'init_script_no': None,
                    'zone_no': None,
                    'access_control_group_configuration_no_list': None,
                    'raid_type_name': None,
                    'instance_tag_list': None,
                    'is_vaccine_install': None}
        if cralwer == 2:
            tmp_dict = {'server_product_code': 'SPSVRSSD00000003',
                        'member_server_image_no': 41286,
                        'server_name': None,
                        'server_description': None,
                        'login_key_name': None,
                        'is_protect_server_termination': False,
                        'server_create_count': None,
                        'server_create_start_no': None,
                        'internet_line_type_code': None,
                        'fee_system_type_code': None,
                        'init_script_no': None,
                        'zone_no': 3,
                        'access_control_group_configuration_no_list': None,
                        'raid_type_name': None,
                        'instance_tag_list': [],
                        'is_vaccine_install': None}
        elif cralwer == 16:
            tmp_dict = {'server_product_code': 'SPSVRSSD00000009',
                        'member_server_image_no': 41286,
                        'server_name': None,
                        'server_description': None,
                        'login_key_name': None,
                        'is_protect_server_termination': False,
                        'server_create_count': None,
                        'server_create_start_no': None,
                        'internet_line_type_code': None,
                        'fee_system_type_code': None,
                        'init_script_no': None,
                        'zone_no': 3,
                        'access_control_group_configuration_no_list': None,
                        'raid_type_name': None,
                        'instance_tag_list': [],
                        'is_vaccine_install': None}
        elif cralwer == "p401ea":
            tmp_dict = {'server_product_code': 'SPSVRGPUSSD00001',
                        'member_server_image_no': 48618,
                        'server_name': None,
                        'server_description': None,
                        'login_key_name': None,
                        'is_protect_server_termination': False,
                        'server_create_count': None,
                        'server_create_start_no': None,
                        'internet_line_type_code': None,
                        'fee_system_type_code': None,
                        'init_script_no': None,
                        'zone_no': 3,
                        'access_control_group_configuration_no_list': None,
                        'raid_type_name': None,
                        'instance_tag_list': [],
                        'is_vaccine_install': None}
        elif cralwer == "p402ea":
            tmp_dict = {'server_product_code': 'SPSVRGPUSSD00002',
                        'member_server_image_no': 48618,
                        'server_name': None,
                        'server_description': None,
                        'login_key_name': None,
                        'is_protect_server_termination': False,
                        'server_create_count': None,
                        'server_create_start_no': None,
                        'internet_line_type_code': None,
                        'fee_system_type_code': None,
                        'init_script_no': None,
                        'zone_no': 3,
                        'access_control_group_configuration_no_list': None,
                        'raid_type_name': None,
                        'instance_tag_list': [],
                        'is_vaccine_install': None}
        elif cralwer == "gpu1ea":
            tmp_dict = {'server_product_code': 'SPSVRGPUSSD00005',
                        'member_server_image_no': 48618,
                        'server_name': None,
                        'server_description': None,
                        'login_key_name': None,
                        'is_protect_server_termination': False,
                        'server_create_count': None,
                        'server_create_start_no': None,
                        'internet_line_type_code': None,
                        'fee_system_type_code': None,
                        'init_script_no': None,
                        'zone_no': 3,
                        'access_control_group_configuration_no_list': None,
                        'raid_type_name': None,
                        'instance_tag_list': [],
                        'is_vaccine_install': None}
        elif cralwer == "gpu2ea":
            tmp_dict = {'server_product_code': 'SPSVRGPUSSD00006',
                        'member_server_image_no': 48618,
                        'server_name': None,
                        'server_description': None,
                        'login_key_name': None,
                        'is_protect_server_termination': False,
                        'server_create_count': None,
                        'server_create_start_no': None,
                        'internet_line_type_code': None,
                        'fee_system_type_code': None,
                        'init_script_no': None,
                        'zone_no': 3,
                        'access_control_group_configuration_no_list': None,
                        'raid_type_name': None,
                        'instance_tag_list': [],
                        'is_vaccine_install': None}
        elif cralwer == "gpu4ea":
            tmp_dict = {'server_product_code': 'SPSVRGPUSSD00010',
                        'member_server_image_no': 48618,
                        'server_name': None,
                        'server_description': None,
                        'login_key_name': None,
                        'is_protect_server_termination': False,
                        'server_create_count': None,
                        'server_create_start_no': None,
                        'internet_line_type_code': None,
                        'fee_system_type_code': None,
                        'init_script_no': None,
                        'zone_no': 3,
                        'access_control_group_configuration_no_list': None,
                        'raid_type_name': None,
                        'instance_tag_list': [],
                        'is_vaccine_install': None}

        return tmp_dict

    def new_get_total_info(self):
        tmp_result_dict = dict()

        try:
            get_block_storage_instance_list_request = ncloud_server.GetBlockStorageInstanceListRequest()  # GetBlockStorageInstanceListRequest | getBlockStorageInstanceListRequest
            tmp_result_dict["block_storage_instance_list"] = \
                self.get_block_storage_instance_list(get_block_storage_instance_list_request).to_dict()[
                    "block_storage_instance_list"]
        except ApiException as e:
            print("Exception when calling V2Api->get_block_storage_instance_list: %s\n" % e)

        try:
            get_init_script_list_rqeust = ncloud_server.GetInitScriptListRequest()  # GetInitScriptListRequest | getInitScriptListRqeust
            tmp_result_dict["init_script_list"] = self.get_init_script_list(get_init_script_list_rqeust).to_dict()[
                "init_script_list"]
        except ApiException as e:
            print("Exception when calling V2Api->get_init_script_list: %s\n" % e)

        get_login_key_list_request = ncloud_server.GetLoginKeyListRequest()  # GetLoginKeyListRequest | getLoginKeyListRequest
        try:
            tmp_result_dict["login_key_list"] = self.get_login_key_list(get_login_key_list_request).to_dict()[
                "login_key_list"]
        except ApiException as e:
            print("Exception when calling V2Api->get_login_key_list: %s\n" % e)

        try:
            get_member_server_image_list_request = ncloud_server.GetMemberServerImageListRequest()  # GetMemberServerImageListRequest | getMemberServerImageListRequest
            tmp_result_dict["member_server_image_list"] = \
                self.get_member_server_image_list(get_member_server_image_list_request).to_dict()[
                    "member_server_image_list"]
        except ApiException as e:
            print("Exception when calling V2Api->get_member_server_image_list: %s\n" % e)

        try:
            get_region_list_request = ncloud_server.GetRegionListRequest()  # GetRegionListRequest | getRegionListRequest
            tmp_result_dict["region_list"] = self.get_region_list(get_region_list_request).to_dict()["region_list"]
        except ApiException as e:
            print("Exception when calling V2Api->get_region_list: %s\n" % e)

        get_server_instance_list_request = ncloud_server.GetServerInstanceListRequest()  # GetServerInstanceListRequest | getServerInstanceListRequest
        try:
            tmp_result_dict["server_instance_list"] = \
                self.get_server_instance_list(get_server_instance_list_request).to_dict()["server_instance_list"]
        except ApiException as e:
            print("Exception when calling V2Api->get_server_instance_list: %s\n" % e)

        try:
            get_server_image_product_list_request = ncloud_server.GetServerImageProductListRequest()  # GetServerImageProductListRequest | getServerImageProductListRequest
            tmp_result_dict["product_list"] = \
                self.get_server_image_product_list(get_server_image_product_list_request).to_dict()["product_list"]
        except ApiException as e:
            print("Exception when calling V2Api->get_server_image_product_list: %s\n" % e)

        return tmp_result_dict

    def new_create_instance(self, input_dict: dict):
        create_server_instances_request = ncloud_server.CreateServerInstancesRequest(
            **input_dict)  # CreateServerInstancesRequest | createServerInstancesRequest
        try:
            api_response = self.create_server_instances(create_server_instances_request)
            return api_response.to_dict()
        except ApiException as e:
            print("Exception when calling V2Api->create_server_instances: %s\n" % e)

    def new_stop_instance(self, input_list: list):
        stop_server_instances_request = ncloud_server.StopServerInstancesRequest(
            input_list)  # StopServerInstancesRequest | stopServerInstancesRequest
        try:
            api_response = self.stop_server_instances(stop_server_instances_request)
            return api_response.to_dict()
        except ApiException as e:
            print("Exception when calling V2Api->stop_server_instances: %s\n" % e)

    def new_start_instance(self, input_list: list):
        start_server_instances_request = ncloud_server.StartServerInstancesRequest(
            input_list)  # StartServerInstancesRequest | startServerInstancesRequest
        try:
            api_response = self.start_server_instances(start_server_instances_request)
            return api_response.to_dict()
        except ApiException as e:
            print("Exception when calling V2Api->start_server_instances: %s\n" % e)

    def new_terminate_instance(self, input_list: list):

        try:
            terminate_server_instances_request = ncloud_server.TerminateServerInstancesRequest(
                input_list)  # TerminateServerInstancesRequest | terminateServerInstancesRequest
            api_response = self.terminate_server_instances(terminate_server_instances_request)
            return api_response.to_dict()
        except ApiException as e:
            print("Exception when calling V2Api->terminate_server_instances: %s\n" % e)

    def new_get_init_script(self):
        try:
            tmp_request = ncloud_server.GetInitScriptListRequest()
            api_response = self.get_init_script_list(tmp_request)
            return api_response.to_dict()
        except Exception as e:
            print("Exception when calling V2Api->get_init_script: %s\n" % e)


    def new_start_instance(self, input_list: list):

        try:
            start_server_instances_request = ncloud_server.StartServerInstancesRequest(
                input_list)  # StartServerInstancesRequest | startServerInstancesRequest
            api_response = self.start_server_instances(start_server_instances_request)
            return api_response.to_dict()
        except ApiException as e:
            print("Exception when calling V2Api->start_server_instances: %s\n" % e)

    def new_make_login_key(self, input_key_name: str):

        try:
            tmp_request = ncloud_server.CreateLoginKeyRequest(input_key_name)
            tmp_dict = self.create_login_key(tmp_request).to_dict()
            return tmp_dict
        except Exception as e:
            print("Exception when calling V2Api->create_login_key: %s\n" % e)

    def new_remove_login_key(self, input_key_name: str):

        try:
            tmp_request = ncloud_server.CreateLoginKeyRequest(input_key_name)
            tmp_dict = self.delete_login_key(tmp_request).to_dict()
            return tmp_dict

        except Exception as e:
            print("Exception when calling V2Api->create_login_key: %s\n" % e)

    @property
    def new_id_spec_dict(self):
        return {"SPSVRSTAND000056": "vCPU 1EA, Memory 1GB, Disk 50GB",
                "SPSVRSTAND000003": "vCPU 1EA, Memory 2GB, Disk 50GB",
                "SPSVRSTAND000049": "vCPU 2EA, Memory 2GB, Disk 50GB",
                "SPSVRSSD00000001": "vCPU 1EA, Memory 2GB, [SSD]Disk 50GB",
                "SPSVRSSD00000002": "vCPU 2EA, Memory 2GB, [SSD]Disk 50GB",
                "SPSVRSTAND000004": "vCPU 2EA, Memory 4GB, Disk 50GB",
                "SPSVRSTAND000024": "vCPU 2EA, Memory 8GB, Disk 50GB",
                "SPSVRSTAND000052": "vCPU 2EA, Memory 16GB, Disk 50GB",
                "SPSVRSTAND000050": "vCPU 4EA, Memory 4GB, Disk 50GB",
                "SPSVRSTAND000005": "vCPU 4EA, Memory 8GB, Disk 50GB",
                "SPSVRSTAND000025": "vCPU 4EA, Memory 16GB, Disk 50GB",
                "SPSVRSTAND000054": "vCPU 4EA, Memory 32GB, Disk 50GB",
                "SPSVRSTAND000051": "vCPU 8EA, Memory 8GB, Disk 50GB",
                "SPSVRSTAND000006": "vCPU 8EA, Memory 16GB, Disk 50GB",
                "SPSVRSTAND000055": "vCPU 8EA, Memory 32GB, Disk 50GB",
                "SPSVRSTAND000053": "vCPU 16EA, Memory 16GB, Disk 50GB",
                "SPSVRSTAND000046": "vCPU 16EA, Memory 32GB, Disk 50GB",
                "SPSVRSSD00000003": "vCPU 2EA, Memory 4GB, [SSD]Disk 50GB",
                "SPSVRSSD00000010": "vCPU 2EA, Memory 8GB, [SSD]Disk 50GB",
                "SPSVRSSD00000011": "vCPU 2EA, Memory 16GB, [SSD]Disk 50GB",
                "SPSVRSSD00000004": "vCPU 4EA, Memory 4GB, [SSD]Disk 50GB",
                "SPSVRSSD00000005": "vCPU 4EA, Memory 8GB, [SSD]Disk 50GB",
                "SPSVRSSD00000012": "vCPU 4EA, Memory 16GB, [SSD]Disk 50GB",
                "SPSVRSSD00000013": "vCPU 4EA, Memory 32GB, [SSD]Disk 50GB",
                "SPSVRSSD00000006": "vCPU 8EA, Memory 8GB, [SSD]Disk 50GB",
                "SPSVRSSD00000007": "vCPU 8EA, Memory 16GB, [SSD]Disk 50GB",
                "SPSVRSSD00000014": "vCPU 8EA, Memory 32GB, [SSD]Disk 50GB",
                "SPSVRSSD00000009": "vCPU 16EA, Memory 16GB, [SSD]Disk 50GB",
                "SPSVRSSD00000016": "vCPU 16EA, Memory 32GB, [SSD]Disk 50GB",
                "SPSVRSTAND000059": "vCPU 8EA, Memory 64GB, Disk 50GB",
                "SPSVRSTAND000060": "vCPU 16EA, Memory 64GB, Disk 50GB",
                "SPSVRSTAND000061": "vCPU 16EA, Memory 128GB, Disk 50GB",
                "SPSVRSTAND000062": "vCPU 32EA, Memory 128GB, Disk 50GB",
                "SPSVRSTAND000067": "vCPU 32EA, Memory 256GB, Disk 50GB",
                "SPSVRSTAND000063": "vCPU 8EA, Memory 64GB, [SSD]Disk 50GB",
                "SPSVRSTAND000064": "vCPU 16EA, Memory 64GB, [SSD]Disk 50GB",
                "SPSVRSTAND000065": "vCPU 16EA, Memory 128GB, [SSD]Disk 50GB",
                "SPSVRSTAND000066": "vCPU 32EA, Memory 128GB, [SSD]Disk 50GB",
                "SPSVRSTAND000069": "vCPU 32EA, Memory 256GB, [SSD]Disk 50GB",
                "SPSVRGPUSSD00001": "GPU 1EA, GPUMemory 24GB, vCPU 4EA, Memory 30GB, [SSD]Disk 50GB",
                "SPSVRGPUSSD00002": "GPU 2EA, GPUMemory 48GB, vCPU 8EA, Memory 60GB, [SSD]Disk 50GB",
                "SPSVRGPU00000001": "GPU 1EA, GPUMemory 24GB, vCPU 4EA, Memory 30GB, Disk 50GB",
                "SPSVRGPU00000002": "GPU 2EA, GPUMemory 48GB, vCPU 8EA, Memory 60GB, Disk 50GB",
                "SPSVRSSD00000021": "vCPU 20EA, Memory 80GB, [SSD]Disk 1000GB (Booting 50GB/Data 950GB)",
                "SPSVRSSD00000023": "vCPU 20EA, Memory 80GB, [SSD]Disk 2000GB (Booting 50GB/Data 1950GB)",
                "SPSVRSSD00000025": "vCPU 32EA, Memory 122GB, [SSD]Disk 1000GB (Booting 50GB/Data 950GB)",
                "SPSVRSSD00000027": "vCPU 32EA, Memory 122GB, [SSD]Disk 2000GB (Booting 50GB/Data 1950GB)",
                "SPSVRSSD00000029": "vCPU 32EA, Memory 244GB, [SSD]Disk 1000GB (Booting 50GB/Data 950GB)",
                "SPSVRSSD00000031": "vCPU 32EA, Memory 244GB, [SSD]Disk 2000GB (Booting 50GB/Data 1950GB)"}
