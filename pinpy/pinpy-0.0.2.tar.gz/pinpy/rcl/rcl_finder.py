import pandas as pd


def find_rcl_in_domain(input_domain_file, input_rcl_file, output_file):
    """
	Find which RCL is found in a Domain and what is its location.

	:param input_domain_file: Name of the input file which contains list of Domains (IRDs).
	:type input_domain_file: string

	:param input_rcl_file: Name of the input file which contains list of RCL.
	:type input_rcl_file: string

	:param output_file: Name of the output file in which Domains along with RCL found in them are saved.
	:type output_file: string

    """
    input_domain_file = 'pinpy/data/'+input_domain_file
    input_rcl_file = 'pinpy/data/'+input_rcl_file
    output_file = 'pinpy/data/output/'+output_file
    print(input_domain_file, input_rcl_file, output_file)

    names1 = ['DomainID', 'Sequence', 'variant']
    dframe1 = pd.read_excel(input_domain_file, sheet_name="Domains", names=names1)
    # print(dframe1)

    for index, row in dframe1.iterrows():
        dframe1.at[index, 'Sequence'] = row['Sequence'].replace(" ", "")
    # print(dframe1)

    names2 = ['RclID', 'Rcl', 'targetProtease', 'tpID']
    dframe2 = pd.read_excel(input_rcl_file, sheet_name="RCL", names=names2)
    print(dframe2)

    x = []
    y = []
    def find_str(s, char):
        index = 0

        if char in s:
            c = char[0]
            for ch in s:
                if ch == c:
                    if s[index:index + len(char)] == char:
                        return index

                index += 1

        return -1

    names = ['DomainID', 'Domain', 'DomVariant', 'RclID', 'RCL', 'targetProtease', 'tpID', 'S_position', 'E_position']
    dFrameFinal = pd.DataFrame(columns=names)

    for index1, row1 in dframe1.iterrows():
        x = row1['Sequence'].strip()
        len1 = len(x)

        for index2, row2 in dframe2.iterrows():
            y = row2['Rcl']
            len2 = len(y)
            # print(y+' len:'+str(len(y)))
            j = 0
            list_index = [-1]
            k = len1 - len2 + 1
            r = x
            i = 0
            while i < k:
                list_index.append(find_str(r, y))
                r = r[:i] + '#' + r[i + 1:]
                print(r)
                i += 1
            list_index = [z for z in list_index if z != -1]

            print(list_index)
            finallist = []
            finallist = set(list_index)
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(finallist)
            for t in finallist:
                print("------------------------------------------------------------------------------------------------")
                dFrameFinal = dFrameFinal.append(
                    {'DomainID': row1['DomainID'], 'Domain': row1['Sequence'], 'DomVariant': row1['variant'],
                    'RclID': row2['RclID'], 'RCL': row2['Rcl'], 'targetProtease': row2['targetProtease'],
                    'tpID': row2['tpID'], 'S_position': str(t), 'E_position': str(t + len(y) - 1)}, ignore_index=True)

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(dFrameFinal)
    dFrameFinal.to_csv(output_file)