#dna seq analysis report 
raw_sequences = [
    "  atg-cga-tac\n",
    "GGCNNATGCC",
    "  ttaa-ccgg  ",
    "atgcgataa",
    "GGG-CCC-NNN"
]
highest_gc = 0
highest_Seq = ""
#cleaned seq
for sequence in raw_sequences:
    clean_sequence = sequence.strip().upper().replace("-","").replace("N", "")
    

    if len(clean_sequence) < 6:
        print("too short, skipped")
        continue
    

#for valid seq
    gc = clean_sequence.count("G") + clean_sequence.count("C")
    GC_percen = round(gc / len(clean_sequence) * 100 , 2)
    print(f"sequence: {clean_sequence} --> length: {len(clean_sequence)} --> GC%: {GC_percen}") 

    for i, base in enumerate(clean_sequence):
        if base == "G":
            print(f"G positions: {i}")

    print(clean_sequence[0:3])

    if "ATG" in clean_sequence:
        print("start codon present")
    else:
        print("no start codon")

# transcription (dna -> rna )
    print(f"RNA seq :  {clean_sequence.replace('T', 'U')}")
    print("-" * 40)  # after each sequence's report

#highest GC %
    if GC_percen > highest_gc :
        highest_gc = GC_percen
        highest_Seq = clean_sequence

print(f"highest GC%: {highest_gc} | sequence: {highest_Seq}")
