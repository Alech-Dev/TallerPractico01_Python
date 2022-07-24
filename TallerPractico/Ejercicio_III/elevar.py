# Recursividad ->  una función se llama a si misma para resolverse.

#Funcion para elevar un numero a un exponente.
def numElevator(base, exponente) :
    #Condición que da fin a las llamadas recursivas.
    if(exponente < 1) :
        #Devuelve 1 cuando el exponente es menor que 1, es decir 0.
        return 1
    else :
        #La multiplicación y el llamado a la recursividad se guardan en una variable.
        res = base * numElevator(base, exponente -1)
        #Devuelve el resultado guardado
        return res