#This script is to count atomic interaction occurrences made by a specific residue with all other possible residues in COCOMAPS2 output file format

import sys
import pandas as pd

if len(sys.argv) != 4:
    print("Usage: python res_int_count.py input.csv RESIDUE_CODE output.csv")
    sys.exit(1)

# Function definition to count occurrences of each type of interaction for a given residue
def count_interactions(df, three_letter_code, residue, interaction_list):
    interactions = df[(df['Res. Name1'].str[-3:] == three_letter_code) & (df['Res. Name2'].str[-3:] == residue)]['Type of Interaction'] #define dataframe
    interaction_counts = {interaction: 0 for interaction in interaction_list} #initialized dictionary for interactions count
    for interaction in interactions:
        if interaction != "":
            interaction_split = interaction.split(";") #semicolons is the field separator for Type of interaction column in the input file
            for inter in interaction_split: 
                if inter.strip() in interaction_list: #to overpass the possible presence of spaces in the interaction entry
                    interaction_counts[inter.strip()] += 1
    return interaction_counts

input_file = sys.argv[1] #input file
three_letter_code = sys.argv[2] #residue code to analyze
output_file = sys.argv[3] #name of the output file
interaction_list = ['pi-pi stacking', 'apolar-vdw']  # Replace with interactions type list of your choice

df = pd.read_csv(input_file) #create dataframe reaidng the input file

residues = df[df['Res. Name1'].str[-3:] == three_letter_code]['Res. Name2'].str[-3:].unique() #extract all possible residue listed in columns Res. Name1 and Res. Name2
#note that -3 is to avoid any possible non standard residue annotation in pdb ex:. BLEU will be LEU 

# Initialize a dataframe as res,interaction1,intercation2,...,interactionN
result_df = pd.DataFrame(columns=['Residue'] + interaction_list)
result_df['Residue'] = residues
result_df = result_df.fillna(0)

# Calculating interaction counts for each residue
for residue in residues:
    interaction_counts = count_interactions(df, three_letter_code, residue, interaction_list)
    for interaction, count in interaction_counts.items():
        result_df.loc[result_df['Residue'] == residue, interaction] = count

# output results in a CSV file format
result_df.to_csv(output_file, index=False)
print(f"{output_file}")
