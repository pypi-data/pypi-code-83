import pandas as pd


def identify_domain_type(input_file, output_file):
    """
	Identify the Domain Type based upon Linker organization in IRD's (Domains).
    Type 1: H-L Type, in which RCL is on right of Linker
    Type 2: L-H Type, in which RCL is on left of Linker
    Type 3: H+L Type, in which NO Linker is present

	:param input_file: Name of the input file which contains details about Domains (IRDs).
	:type input_file: string

	:param output_file: Name of the output file in which Domains detail along with type of Domain are saved.
	:type output_file: string

    """
    input_file = 'pinpy/data/'+input_file
    output_file = 'pinpy/data/output/'+output_file
    # print(input_file,output_file)

    # Counters to count 3 Domain Types
    HL = 0
    LH = 0
    NOLinker = 0

    dom_rcl_linker = pd.read_excel(input_file)  # Reading the input file
    # print(dom_rcl_linker)
    for index, row in dom_rcl_linker.iterrows():
        # print(row)
        domainType = row['DomainType']
        linkerSPOS = row['Linker_startPosition']
        linkerEPOS = row['Linker_endPosition']
        rclSPOS = row['RCL_startPosition']
        rclEPOS = row['RCL_endPosition']
        if domainType != 3:  # Skipping the rows with DomainType 3
            # print(row['linkerID'])
            if rclSPOS > linkerEPOS:
                print('Domain H-L type: Type 1')
                HL = HL + 1
                # Assigning the Domain Type to the Data Frame dom_rcl_linker
                dom_rcl_linker.loc[dom_rcl_linker.domainID ==
                                   row['domainID'], 'DomainType'] = 1
            elif linkerSPOS > rclEPOS:
                print('Domain L-H type: Type 2')
                LH = LH + 1
                # Assigning the Domain Type to the Data Frame dom_rcl_linker
                dom_rcl_linker.loc[dom_rcl_linker.domainID ==
                                   row['domainID'], 'DomainType'] = 2
            else:
                # Not Necessary
                print('Domain H+L Type: Type 3')
                NOLinker = NOLinker + 1
        else:
            # Condition where Domain Type is equal to 3
            print('Domain H+L Type: Type 3')
            NOLinker = NOLinker + 1
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('H-L Type Domains: ', HL)
    print('L-H Type Domains: ', LH)
    print('Type-3 Domains: ', NOLinker)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(dom_rcl_linker.DomainType.value_counts())

    # Writing the Data Frame dom_rcl_linker to the output CSV file
    dom_rcl_linker.to_csv(output_file, index=False)
