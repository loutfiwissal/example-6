NP=int(input("taper le nombre de photocopier: "))
if NP>=0 and NP<=10 :
    print("le prix est:",NP*0.30,"DH")
elif NP>=11 and NP<=30 :
    print(" le prix est:",NP*0.25,"DH")
else :
    print("le prix est:",NP*0.20,"DH")
