#drugi zadatak

def ocjena_raspodjela(broj):
    if 0.9 <= broj <= 1.0:
        return "A"
    elif 0.8<= broj < 0.9:
        return "B"
    elif 0.7<= broj < 0.8:
        return "C"
    elif 0.6<= broj < 0.7:
        return "D"
    elif 0.0 <= broj < 0.6:
        return "F"
    else:
        return "Broj nije iz zadanog intervala"
    
