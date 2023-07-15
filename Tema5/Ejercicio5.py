def añoBisiesti(añoEnviado):
    if añoEnviado%4==0:
        return "Es bisiesto"
    elif (añoEnviado%100==0 and añoEnviado%400==0):
        return "Es bisiesto"
    elif añoEnviado==366:
        return "Es bisiesto"
    else:
        return "No es bisiesto"

año=añoBisiesti(int(input("Ingresa el año actual: ")))
