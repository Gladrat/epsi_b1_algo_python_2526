seq_mouches =  ["CCATTAGTTA", "ATTGCCTTGG", "CGCTTGAAAT"]

for s in seq_mouches:
    seq_comp = ""

    for lettre in s:
        if lettre == "A":
            seq_comp = seq_comp + "T"
        elif lettre == "T":
            seq_comp = seq_comp + "A"
        elif lettre == "C":
            seq_comp = seq_comp + "G"
        elif lettre == "G":
            seq_comp = seq_comp + "C"

    print(seq_comp)