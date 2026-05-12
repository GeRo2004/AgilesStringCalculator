
class calculator:
    #def calculator(texto):
    #    if texto == "":
    #        return 0
    #    elif texto == "1":
    #        return 1
    #    elif texto == "1,2":
    #        return 3
    #    elif texto == "3,5":
    #        return 8
    #    return texto
    
    #numeros = texto.split(",")

    #return sum(int(n) for n in numeros)

    #Refactor luego de detectar el patron de sumas
    def calculator(texto):
        if texto == "":
            return 0
        numeros = texto.split(",")
        if len(numeros) == 1:
            return int(texto)
        else:
            num1, num2 = numeros
            return int(num1) + int(num2)