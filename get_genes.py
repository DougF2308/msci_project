#!/bin/bash
#!/usr/bin/python

import sys

def main():
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 3:
        print('Usage: python script.py gene_names.txt genes.fasta')
        sys.exit()

    # Get the name of the gene names file and the FASTA file from the command line arguments
    gene_names_file = sys.argv[1]
    genes_file = sys.argv[2]

    # Open the text file of gene names and read it line by line
    with open(gene_names_file, 'r') as gene_names_file:
        gene_names = gene_names_file.read().splitlines()

    # Open the FASTA file and read it line by line
    with open(genes_file, 'r') as genes_file:
        # Initialize a variable to store the current gene sequence
        gene_seq = ''
        # Initialize a variable to keep track of whether we are currently reading a gene sequence
        reading_gene_seq = False

        for line in genes_file:
            # Check if the line starts with a ">" character
            if line.startswith('>'):
                # Get the gene name from the line
                gene_name = line[1:].strip()
                # Check if the gene name is in the list of gene names that we want to retrieve
                if gene_name in gene_names:
                    # Set the reading_gene_seq flag to True
                    reading_gene_seq = True
                    # Print the gene name
                    print(gene_name)
                else:
                    # Set the reading_gene_seq flag to False
                    reading_gene_seq = False
            elif reading_gene_seq:
                # If we are currently reading a gene sequence, then append the line to the gene_seq string
                gene_seq += line.strip()

    # Print the gene sequence for each gene that we found in the FASTA file
    print(gene_seq)

if __name__ == '__main__':
    main()
