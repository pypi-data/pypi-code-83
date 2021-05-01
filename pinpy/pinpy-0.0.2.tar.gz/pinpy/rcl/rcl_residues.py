import pandas as pd


def identify_residues(input_file, output_file):
    """
	Identify the Residues at P1, P2 and P1` position in an RCL for example in CPRNC:
    P1 Residue is: R
    P2 Residue is: P
    P1` (prime) Residue is: N

	:param input_file: Name of the input file which contains list of RCL.
	:type input_file: string

	:param output_file: Name of the output file in which RCLs along with their Residues at P1, P2 and P1` position are saved.
	:type output_file: string

    """
    input_file = 'pinpy/data/'+input_file
    output_file = 'pinpy/data/output/'+output_file
    # print(input_file,output_file)

    rcl = pd.read_excel(input_file)  # Reading the input file
    rcl['P2Residue'] = rcl['Rcl'].apply(lambda x: x[1])
    rcl['P1Residue'] = rcl['Rcl'].apply(lambda x: x[2])
    rcl['P1primeResidue'] = rcl['Rcl'].apply(lambda x: x[3])
    print(rcl)
    # Writing the Data Frame to the output CSV file
    rcl.to_csv(output_file, index=False)