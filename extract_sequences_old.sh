#!/bin/bash

# set the input and output filenames as variables
gene_names_file=$1
sequences_file=$2
selected_sequences_file=$3

# extract the sequences of the specified genes
grep -A13 -f "$gene_names_file" "$sequences_file" > "$selected_sequences_file"


#for use: ./extract_sequences.sh gene_names.txt all_sequences.fasta selected_sequences.fasta

