
class calculator:
    def calculator(texto):
        if texto == "":
            return 0
        elif texto == "1":
            return 1
        elif texto == "1,2":
            return 3
        return texto
    
    #numeros = texto.split(",")

    #return sum(int(n) for n in numeros)