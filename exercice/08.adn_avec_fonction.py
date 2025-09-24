seq_mouche =  ["CCATTAGTTA", "ATTGCCTTGG", "CGCTTGAAAT"]
seq_escargot =  ["CCATTAGTTA", "ATTGCCTTGG", "CGCTTGAAAT"]
seq_limaces =  ["CCATTAGTTA", "ATTGCCTTGG", "CGCTTGAAAT"]

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def inverse_adn(seq_adn):
    seq_comp = ""
    for lettre in seq_adn:
        if lettre == "A":
            seq_comp = seq_comp + "T"
        elif lettre == "T":
            seq_comp = seq_comp + "A"
        elif lettre == "G":
            seq_comp = seq_comp + "C"
        elif lettre == "C":
            seq_comp = seq_comp + "G"
    print(seq_comp)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

inverse_adn("AAAGGGTTACCGTTTTACCCCAGGGGAATTGCCCCGTTAA")

for s in seq_mouche:
    inverse_adn(s)

for s in seq_escargot:
    inverse_adn(s)

for s in seq_limaces:
    inverse_adn(s)