codon_table = {
    "ATG": "Methionine",
    "GCG": "Alanine",
    "TCC": "Serine",
    "TAT": "Tyrosine",
    "CGT": "Arginine"
}
dna_sequence = "ATGCGTTATGCG"


# def dna_transcriber(codon_table, dna_seq):
#     new_list = []
#     if len(dna_seq) % 3 != 0:
#         return False

#     for _ in range(int(len(dna_seq) / 3)):
#         chunk = dna_seq[:3]
#         dna_seq = dna_seq[3:]
#         if chunk in codon_table:
#             new_list.append(codon_table[chunk])
#     return "-".join(new_list)

# print(f"Sequence: {dna_sequence}")
# result = dna_transcriber(codon_table, dna_sequence)
# print(f"Proteins: {result}")





def dna_transcriber(codon_table, dna_seq):
    proteins = []
    for i in range(0, len(dna_seq), 3):
        codon = dna_seq[i:3+i]
        if len(codon) != 3:
            continue
        if codon in codon_table:
            proteins.append(codon_table[codon])
    return "-".join(proteins)


print(f"Sequence: {dna_sequence}")
result = dna_transcriber(codon_table, dna_sequence)
print(f"Proteins: {result}")
