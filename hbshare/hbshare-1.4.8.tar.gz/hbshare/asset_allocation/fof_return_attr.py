import os
import pandas as pd

path = 'D:\\kevin\\绩效归因'
"===========================================域秀==================================================="
data_path = os.path.join(path, r'data')
filenames = os.listdir(data_path)

all_data = []
date_list = []
mkt_list = []
for name in filenames:
    file_path = os.path.join(data_path, name)
    date = name.split('.')[0].split('_')[-1]
    data = pd.read_excel(file_path, header=3)
    # 基金市值
    fund_mkv = float(data[data['科目代码'] == '基金资产净值:']['市值'].values[0])
    # 持仓
    data['sign'] = data['科目代码'].apply(lambda x: x[:8])
    data = data[data['sign'].isin(['11050201', '11090601'])]
    data['sign_2'] = data['科目代码'].apply(lambda x: len(x))
    data = data[data['sign_2'] > 8][['科目名称', '数量', '单位成本', '成本', '市价']]
    data.rename(
        columns={"科目名称": "name", "数量": "volume", "单位成本": "unit_cost", "成本": "cost", "市价": "price"}, inplace=True)
    data['date'] = date
    all_data.append(data)
    date_list.append(date)
    mkt_list.append(fund_mkv)

all_data = pd.concat(all_data)
mkv_df = pd.Series(index=date_list, data=mkt_list).sort_index()

earning = []
for i in range(1, len(date_list)):
    tdate = sorted(date_list)[i]
    pre_date = sorted(date_list)[i - 1]

    df1 = all_data[all_data['date'] == pre_date].set_index(
        'name').rename(columns={"volume": "pre_volume", "cost": "pre_cost", "price": "pre_price"})[
        ['pre_volume', 'pre_cost', 'pre_price']]
    df2 = all_data[all_data['date'] == tdate].set_index('name')[['volume', 'cost', 'price']]
    df = pd.merge(df1, df2, left_index=True, right_index=True, how='outer').fillna(0.)
    # 1、数量不变
    part1 = df[df['volume'] == df['pre_volume']]
    part1['earning'] = part1['pre_volume'] * (part1['price'] - part1['pre_price'])
    # 2、数量从0到有
    part2 = df[(df['pre_volume'] == 0) & (df['volume'] > 0)]
    part2['earning'] = part2['volume'] * part2['price'] - part2['cost']
    # 3、数量从有到0
    part3 = df[(df['pre_volume'] > 0) & (df['volume'] == 0)]
    part3['earning'] = 0
    # 4、数量增加
    part4 = df[(df['volume'] > df['pre_volume']) * (df['pre_volume'] > 0)]
    part4['earning'] = part4['price'] * part4['volume'] - part4['pre_price'] * part4['pre_volume'] - (
            part4['cost'] - part4['pre_cost'])
    # 5、数量减少
    part5 = df[(df['volume'] < df['pre_volume']) * (df['volume'] > 0)]
    part5['earning'] = part5['volume'] * (part5['price'] - part5['pre_price'])

    df_new = pd.concat([part1, part2, part3, part4, part5])[['earning']]
    df_new['date'] = tdate

    earning.append(df_new)

earning = pd.concat(earning)