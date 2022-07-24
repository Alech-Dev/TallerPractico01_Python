from clsLlanta import Llanta

class Carro :
    #Cosntructor de la clase
    def __init__(self, marca, modelo, matricula):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula

    def diametroLlanta(self):
        resp = input("Digite el valor del radio de la llanta para calcular su diametro: ")
        diamLlanta = Llanta(int(resp))
        print(diamLlanta.calcularDiametro())