import socket

from notion_as_db.configured_notion import Notion

from .ncloud import NCloud

notion = Notion()
collection_dict = notion.get_collections_as_dict(notion.block_dict["cloud"])


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    return s.getsockname()[0]


def get_instance_name():
    return socket.gethostname().split(".")[0]


def get_ncloud_api_dict():
    global notion, collection_dict
    tmp_collection = collection_dict["API info"]
    df = notion.get_df_from_collection_block(tmp_collection)
    api_dict = dict()
    for row in df.itertuples():
        if row.cloud_name == "ncloud":
            api_dict[row.user_email] = NCloud(row.access_key_id, row.secret_key)
    return api_dict


api_dict = get_ncloud_api_dict()


def make_login_key_all_ncloud(input_key_name: str):
    global notion, collection_dict
    api_dict = get_ncloud_api_dict()
    collection = collection_dict["API info"]
    collection_login_key = collection_dict["Login key info"]
    tmp_df = notion.get_df_from_collection_block(collection)
    for row in tmp_df.itertuples():
        if row.cloud_name == "ncloud":
            try:
                tmp_row = collection_login_key.add_row()
                tmp_dict = api_dict[row.user_email].new_make_login_key(input_key_name)
                tmp_row.key_name = input_key_name
                tmp_row.email = row.user_email
                tmp_row.private_key = tmp_dict["private_key"]
            except Exception as e:
                print(e)


def remove_login_key_all_ncloud(input_key_name: str):
    global notion, collection_dict
    api_dict = get_ncloud_api_dict()
    collection_login_key = collection_dict["Login key info"]
    tmp_list = collection_login_key.get_rows()
    for i in range(len(tmp_list) - 1, -1, -1):
        if input_key_name == tmp_list[i].key_name:
            try:
                print(api_dict[tmp_list[i].email].remove_login_key(input_key_name))
                tmp_list[i].remove()
            except Exception as e:
                print(e)


def stop_all_machine(task_name: str):
    api_dict = get_ncloud_api_dict()
    tmp_running_machine_num = 0
    for key in api_dict.keys():
        tmp_list = list()
        tmp_instance_info_dict = api_dict[key].new_get_instance_info()
        for item in tmp_instance_info_dict.items():
            if task_name in item[0]:
                print(item[1])
                if item[1]["server_instance_status_name"] == "running":
                    tmp_list.append(item[1]["server_instance_no"])
                else:
                    tmp_running_machine_num += 1
        if tmp_list:
            api_dict[key].new_stop_instance(tmp_list)
        print("{} remains {} machines".format(key, tmp_running_machine_num))


def terminate_all_machine(task_name: str):
    api_dict = get_ncloud_api_dict()
    tmp_not_terminated_num = 0
    for key in api_dict.keys():
        tmp_list = list()
        tmp_instance_info_dict = api_dict[key].new_get_instance_info()
        for item in tmp_instance_info_dict.items():
            if task_name in item[0]:
                print(item[1])
                if item[1]["server_instance_status_name"] == "stopped":
                    tmp_list.append(item[1]["server_instance_no"])
                else:
                    tmp_not_terminated_num += 1
        if tmp_list:
            api_dict[key].new_terminate_instance(tmp_list)
        print("{} remains {} machines".format(key, tmp_not_terminated_num))


def start_all_machine(input_machine_info_dict: dict):
    api_dict = get_ncloud_api_dict()
    for key in api_dict.keys():
        api_dict[key].new_create_instance(input_machine_info_dict)


def log_instance(instance_name="", server_instance_no="", create_date="", uptime="", private_ip="",
                 server_instance_type="", server_instance_status_name="", email=""):
    global notion, collection_dict
    collection = collection_dict["Instance log"]
    row = collection.add_row()
    if instance_name:
        row.instance_name = instance_name
    if server_instance_no:
        row.server_instance_no = server_instance_no
    if create_date:
        row.create_date = create_date
    if uptime:
        row.uptime = uptime
    if private_ip:
        row.private_ip = private_ip
    if server_instance_type:
        row.server_instance_type = server_instance_type
    if server_instance_status_name:
        row.server_instance_status_name = server_instance_status_name
    if email:
        row.email = email


def update_log(instance_name="", server_instance_no="", create_date="", uptime="", private_ip="",
               server_instance_type="", server_instance_status_name="", email=""):
    global notion, collection_dict
    collection = collection_dict["Instance log"]
    row_list = collection.get_rows(search=instance_name)
    for row in row_list:
        if row.private_ip == private_ip:
            if server_instance_no:
                row.server_instance_no = server_instance_no
            if create_date:
                row.create_date = create_date
            if uptime:
                row.uptime = uptime
            if private_ip:
                row.private_ip = private_ip
            if server_instance_type:
                row.server_instance_type = server_instance_type
            if server_instance_status_name:
                row.server_instance_status_name = server_instance_status_name
            if email:
                row.email = email
            break


def log_start():
    tmp_private_ip = get_local_ip()
    tmp_instance_name = get_instance_name()
    tmp_api_dict = get_ncloud_api_dict()
    for email in tmp_api_dict.keys():
        tmp_instance_dict = tmp_api_dict[email].new_get_instance_info()
        if tmp_instance_name in tmp_instance_dict.keys() and tmp_private_ip == tmp_instance_dict[tmp_instance_name][
            "private_ip"]:
            tmp_dict = dict()
            tmp_dict["instance_name"] = tmp_instance_name
            tmp_dict["email"] = email
            tmp_dict.update(tmp_instance_dict[tmp_instance_name])
            log_instance(**tmp_dict)
            break


def log_successful_end_and_stop_instance():
    tmp_private_ip = get_local_ip()
    tmp_instance_name = get_instance_name()
    tmp_api_dict = get_ncloud_api_dict()
    for email in tmp_api_dict.keys():
        tmp_instance_dict = tmp_api_dict[email].get_instance_info()
        if tmp_instance_name in tmp_instance_dict.keys() and tmp_private_ip == tmp_instance_dict[tmp_instance_name][
            "private_ip"]:
            tmp_dict = dict()
            tmp_dict["instance_name"] = tmp_instance_name
            tmp_dict["private_ip"] = tmp_instance_dict[tmp_instance_name]["private_ip"]
            tmp_dict["server_instance_status_name"] = "stopped"
            update_log(**tmp_dict)
            tmp_api_dict[email].stop_instance([tmp_instance_dict[tmp_instance_name]["server_instance_no"]])
            break


def log_error():
    tmp_private_ip = get_local_ip()
    tmp_instance_name = get_instance_name()
    tmp_api_dict = get_ncloud_api_dict()
    for email in tmp_api_dict.keys():
        tmp_instance_dict = tmp_api_dict[email].new_get_instance_info()
        if tmp_instance_name in tmp_instance_dict.keys() and tmp_private_ip == tmp_instance_dict[tmp_instance_name][
            "private_ip"]:
            tmp_dict = dict()
            tmp_dict["instance_name"] = tmp_instance_name
            tmp_dict["private_ip"] = tmp_instance_dict[tmp_instance_name]["private_ip"]
            tmp_dict["server_instance_status_name"] = "error may running"
            update_log(**tmp_dict)
            break


def stop_instance():
    global notion, collection_dict, api_dict
    tmp_df = notion.get_df_from_collection_block(collection_dict["Instance log"])
    tmp_ip = get_local_ip()
    tmp_host_name = get_instance_name()
    tmp_result_df = tmp_df[(tmp_df.private_ip == tmp_ip) & (tmp_df.instance_name == tmp_host_name) & (
            tmp_df.server_instance_status_name == "running")]
    if len(tmp_result_df) != 0:
        update_log(private_ip=tmp_ip, instance_name=tmp_host_name, server_instance_status_name="stopped")
        tmp_email = tmp_result_df["email"].loc[0]
        api_dict[tmp_email].new_stop_instance([tmp_result_df["server_instance_no"].loc[0]])
    else:
        print("No proper instance")

def terminate_instances():
    global notion, collection_dict
    tmp_df = notion.get_df_from_collection_block(collection_dict["Instance log"])
    tmp_df = tmp_df[tmp_df.server_instance_status_name == "stopped"]
    for row in tmp_df.itertuples():
        tmp = api_dict[row.email].new_terminate_instance([row.server_instance_no])
        if tmp["return_message"] == "success":
            update_log(instance_name=row.instance_name, server_instance_no=row.server_instance_no,
                                     server_instance_status_name="terminated")
