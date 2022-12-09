#!/bin/bash
grep -A13 -f "$1" "$2" | sed -r ':a;N;$!ba;s/^(>.+)(\n--\n)/\1\2/g' | sed '/^--$/d' >"$3"

#use: ./extract_sequences.sh gene_names.txt all_sequences.fasta selected_sequences.fasta

