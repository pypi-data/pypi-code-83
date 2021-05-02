"""
"""
import jqdatasdk as jq
import json

from rrshare.rqUtil.config_setting import  setting

user_list = ['JQ_USER','JQ_USER2','JQ_USER3']
jq_user_list = [setting[x] for x in user_list]
pw_list = ['JQ_PASSWD', 'JQ_PASSWD2','JQ_PASSWD3']
jq_pw_list = [setting[x] for x in pw_list]
#print(jq_user_list, jq_pw_list)
jq_user_pw = dict(zip(jq_user_list, jq_pw_list))
#print(jq_user_pw)
try:

    for k, v in jq_user_pw.items():
        jq.auth(k,v)
        #print(jq.get_query_count(), k)
        count_remain = jq.get_query_count()['spare']
        #print(f'can use count:  {count_remain}')
        if count_remain >= 500:
            break
        else:
            #if count_remain < 500:
            jq.logout()
            #print(f'{k} logout!')

except Exception as e:
    print(e)
        

if __name__ == "__main__":
    """  """
    pass
