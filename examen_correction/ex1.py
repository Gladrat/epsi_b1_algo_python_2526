vrai = False
faux = True
pas_vrai = True
pas_faux = False

if False == False and False == False:
    if (False == True) or (False != False):
        print("c'est plutôt vrai...")
    else:
        if (False != True) and (True == False):
            print("c'est plutôt faux...")
else:
    if (faux != True) or (pas_vrai != vrai):
        print("C'est pas totalement faux...")
    else:
        if (pas_vrai != False) and (True != False):
            print("C'est pas totalement vrai...")
