"""
"""
import jqdatasdk as jq
import json

from rrshare.rqUtil.config_setting import setting

try:
    jq_user = setting['JQ_USER']
    jq_passwd = setting['JQ_PASSWD']
    #print(jq_user)
    jq.auth(jq_user,jq_passwd)
    print(jq.get_query_count(), jq_user)
    count_remain = jq.get_query_count()['spare']
    #print(f'can use count:  {count_remain}')
    if count_remain < 500:
        jq.logout()
        jq_user = setting['JQ_USER2']
        jq_passwd = setting['JQ_PASSWD2']
        #print(jq_user)
        jq.auth(jq_user,jq_passwd)
        print(jq.get_query_count(), jq_user)
        count_remain = jq.get_query_count()['spare']
        #print(f'can use count:  {count_remain}')
        if count_remain < 500:
            jq.logout()
            jq_user = setting['JQ_USER3']
            jq_passwd = setting['JQ_PASSWD3']
            #print(jq_user)
            jq.auth(jq_user,jq_passwd)
            print(jq.get_query_count(), jq_user)
            count_remain = jq.get_query_count()['spare']
            #print(f'can use count:  {count_remain}')
except Exception as e:
    print(e)
"""
else:
    try:
        #import jqdatasdk as jq
        jq.auth(jq_user, jq_passwd)
        count_remain3 = jq.get_query_count()['spare']
        print(f'can use count:  {count_remain}')
        print(jq.is_auth())
    except Exception as e:
        print(e)
"""

if __name__ == "__main__":
    """
    name_code = jq.get_all_securities('stock')['display_name'].head(5).reset_index()
    print(name_code.head())
    name_code['code'] = name_code['index'].apply(lambda x : x[0:6])
    name_code = name_code.rename(columns={'display_name':'name'})
    name_code = name_code[['code','name']]
    print(name_code.head())
    """
    pass
