# dna-sequence-analyzer

# DNA Sequence Analysis Report

A Python script that cleans, validates and analyzes raw DNA sequences.

## What it does
- Cleans messy input — strips whitespace, removes dashes and N bases
- Skips sequences shorter than 6 bases
- Reports GC%, codon info, RNA transcription per sequence  
- Identifies highest GC% sequence across all inputs

## Concepts used
- String methods — strip, upper, replace, count
- Loops and enumerate
- Conditionals and continue
- f-string formatting

## How to run
python sequence_report.py

## Example output

sequence: ATGCGATAC --> length: 9 --> GC%: 44.44
G positions: 2
G positions: 4
ATG
start codon present
RNA seq :  AUGCGAUAC
----------------------------------------
sequence: GGCATGCC --> length: 8 --> GC%: 75.0
G positions: 0
G positions: 1
G positions: 5
GGC
start codon present
RNA seq :  GGCAUGCC
----------------------------------------
sequence: TTAACCGG --> length: 8 --> GC%: 50.0
G positions: 6
G positions: 7
TTA
no start codon
RNA seq :  UUAACCGG
----------------------------------------
sequence: ATGCGATAA --> length: 9 --> GC%: 33.33
G positions: 2
G positions: 4
ATG
start codon present
RNA seq :  AUGCGAUAA
----------------------------------------
sequence: GGGCCC --> length: 6 --> GC%: 100.0
G positions: 0
G positions: 1
G positions: 2
GGG
no start codon
RNA seq :  GGGCCC
----------------------------------------
highest GC%: 100.0 | sequence: GGGCCC
