import pandas as pd


def find_domains_in_seq(input_domain_file, input_seq_file, output_file):
    """
	Find which Domains (IRDs) are found in a protein sequence and what are their location.

	:param input_domain_file: Name of the input file which contains list of Domains (IRDs).
	:type input_domain_file: string

	:param input_seq_file: Name of the input file which contains list of protein Sequences.
	:type input_seq_file: string

	:param output_file: Name of the output file in which details about domains in a sequence are saved.
	:type output_file: string

    """
    input_domain_file = 'pinpy/data/'+input_domain_file
    input_seq_file = 'pinpy/data/'+input_seq_file
    output_file = 'pinpy/data/output/'+output_file
    # print(input_domain_file, input_seq_file, output_file)

    names1 = ['UniprotID', 'Sequence', 'OrganismID', 'Organism']
    dframe1 = pd.read_excel(input_seq_file,sheet_name="Sequence", names=names1)
    # print(dframe1)

    for index, row in dframe1.iterrows():
        dframe1.at[index, 'Sequence'] = row['Sequence'].replace(" ", "")
        # print(len(dframe1.at[index, 'Sequence']))
        # print(dframe1.at[index, 'Sequence'])

    names2 = ['DomainID', 'Sequence', 'variant']
    dframe2 = pd.read_excel(input_domain_file,sheet_name="Domains", names=names2)
    print(dframe2)

    for index, row in dframe2.iterrows():
        dframe2.at[index, 'Sequence'] = row['Sequence'].replace(" ", "")
        print(len(dframe2.at[index, 'Sequence']))
        print(dframe2.at[index, 'Sequence'])

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
    
    names = ['UniprotID', 'Sequence', 'OrganismID', 'Organism', 'DomainID', 'Domain', 'DomainStartPosition',
         'DomainEndPosition']
    dFrameFinal = pd.DataFrame(columns=names)

    for index1, row1 in dframe1.iterrows():
        x = row1['Sequence'].strip()
        len1 = len(x)

        for index2, row2 in dframe2.iterrows():
            y = row2['Sequence']
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
                    {'UniprotID': row1['UniprotID'], 'Sequence': row1['Sequence'], 'OrganismID': row1['OrganismID'],
                    'Organism': row1['Organism'], 'DomainID': row2['DomainID'], 'Domain': row2['Sequence'],
                    'DomainStartPosition': str(t),
                    'DomainEndPosition': str(t + len(y) - 1)}, ignore_index=True)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(dFrameFinal)
    dFrameFinal.to_csv(output_file)