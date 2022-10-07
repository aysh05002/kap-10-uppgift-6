def raknare(tal1,tal2,operator):
    if operator=="+":
        resultat=tal1+tal2
        return resultat
    elif operator=="-":
        resultat=tal1-tal2
        return resultat
    elif operator=="*":
        resultat=tal1*tal2
        return resultat
    elif operator=="/":
        resultat=tal1/tal2
        return resultat
    else:
        print("felaktikt opretor")
print(raknare(int(input("tal1= ")),int(input("tal2= ")),input("operator, (+ - * /) ")))