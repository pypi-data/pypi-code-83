import pandas as pd


def calculate_amino_composition(input_file, output_file):
    """
	Finds the Amino Acids composition of protein Sequences. Calculates each Amino Acid's count and percentage in the sequences.

	:param input_file: Name of the input file which contains list of Amino Sequences.
	:type input_file: string

	:param output_file: Name of the output file in which sequences along with their amino comosition is saved.
	:type output_file: string

    """
    input_file = 'pinpy/data/'+input_file
    output_file = 'pinpy/data/output/'+output_file
    # Reading the input file in sequencesDF Data Frame
    sequencesDF = pd.read_excel(input_file)
    # print(sequencesDF)
    # print(sequencesDF.columns)
    # Setting the fields of output file
    outputFields = ['ID', 'Sequence', 'Length', 'A', 'A_per', 'C', 'C_per', 'D', 'D_per', 'E', 'E_per', 'F', 'F_per', 'G',
                    'G_per', 'H', 'H_per', 'I', 'I_per', 'K', 'K_per', 'L', 'L_per', 'M', 'M_per', 'N', 'N_per', 'O',
                    'O_per', 'P', 'P_per', 'Q', 'Q_per', 'R', 'R_per', 'S', 'S_per', 'T', 'T_per', 'U', 'U_per', 'V',
                    'V_per', 'W', 'W_per', 'X', 'X_per', 'Y', 'Y_per', 'Z', 'Z_per']
    # Creating the output Data Frame
    seqAminoCompDF = pd.DataFrame(columns=outputFields)
    # Iterating through the Amino acid sequences and computing the Amino Acid composition of each sequence
    for index, row in sequencesDF.iterrows():
        ln = len(row['Sequence'])  # Length of sequence
        a = row['Sequence'].count('A')
        a_per = (a / ln) * 100
        c = row['Sequence'].count('C')
        c_per = (c / ln) * 100
        d = row['Sequence'].count('D')
        d_per = (d / ln) * 100
        e = row['Sequence'].count('E')
        e_per = (e / ln) * 100
        f = row['Sequence'].count('F')
        f_per = (f / ln) * 100
        g = row['Sequence'].count('G')
        g_per = (g / ln) * 100
        h = row['Sequence'].count('H')
        h_per = (h / ln) * 100
        i = row['Sequence'].count('I')
        i_per = (i / ln) * 100
        k = row['Sequence'].count('K')
        k_per = (k / ln) * 100
        l = row['Sequence'].count('L')
        l_per = (l / ln) * 100
        m = row['Sequence'].count('M')
        m_per = (m / ln) * 100
        n = row['Sequence'].count('N')
        n_per = (n / ln) * 100
        o = row['Sequence'].count('O')
        o_per = (o / ln) * 100
        p = row['Sequence'].count('P')
        p_per = (p / ln) * 100
        q = row['Sequence'].count('Q')
        q_per = (q / ln) * 100
        r = row['Sequence'].count('R')
        r_per = (r / ln) * 100
        s = row['Sequence'].count('S')
        s_per = (s / ln) * 100
        t = row['Sequence'].count('T')
        t_per = (t / ln) * 100
        u = row['Sequence'].count('U')
        u_per = (u / ln) * 100
        v = row['Sequence'].count('V')
        v_per = (v / ln) * 100
        w = row['Sequence'].count('W')
        w_per = (w / ln) * 100
        x = row['Sequence'].count('X')
        x_per = (x / ln) * 100
        y = row['Sequence'].count('Y')
        y_per = (y / ln) * 100
        z = row['Sequence'].count('Z')
        z_per = (z / ln) * 100

        # Preparing the output Record
        record = [row['ID'], row['Sequence'], ln, a, a_per, c, c_per, d, d_per, e, e_per, f, f_per, g, g_per, h,
                  h_per, i, i_per, k, k_per, l, l_per, m, m_per, n, n_per, o, o_per, p, p_per, q, q_per, r, r_per, s, s_per,
                  t, t_per, u, u_per, v, v_per, w, w_per, x, x_per, y, y_per, z, z_per]
        # Adding one Row to the seqAminoCompDF Data Frame, with the prepared record list
        seqAminoCompDF.loc[index] = record
        # print(record)
        # print(index)
    seqAminoCompDF.index += 1  # Incrementing the index by one so that it starts at 1
    print(seqAminoCompDF)
    seqAminoCompDF.to_csv(output_file)  # Writing the Data Frame to the output file