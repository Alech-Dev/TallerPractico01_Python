import turtle
import elevar

class Figura:
    def __init__(self):
        pass

    def desplazar(self):
        print("Desplazar para realizar una figura")

    def calcularVolumen(self):
        print("Calcular el volumen de la figura")

    def calcularArea(self):
        print("Calcular el area de la figura")


class Circulo(Figura) :
    def __init__(self, *args):
        if len(args) == 0:
            self.__color = "green"
            self.__rad = 70
        elif len(args) == 2:
            self.__color = args[0]
            self.__rad = args[1]
        else:
            print("Error, los atributos son incorrectos.")       

    def desplazar(self):
        turtle.color(self.__color)
        turtle.speed(3)
        turtle.setup(600, 600)
        turtle.bgcolor("black")
        turtle.speed(0)
        turtle.width(4)
        turtle.circle(self.__rad)
        turtle.hideturtle()
        turtle.Screen().exitonclick()
        
    def calcularArea(self):
        #El área de un circulo  se calcula A = π r²
        print("El área del circulo es: ", 3.1416 * elevar.numElevator(self.__rad, 2))

    def calcularVolumen(self):
        #El calculo del volumen de una esfera es V = 4/3 πr³
        print("El volumen de la esfera es: ", 4/3 * (3.1416 * elevar.numElevator(self.__rad, 3)))

class   Triangulo(Figura):
    def __init__(self, *args):
        if len( args ) == 0:
            self.__color = "green"
            self.__base = 10
            self.__altura = 10
        elif len( args ) == 3:
            self.__color = args[0]
            self.__base = args[1]
            self.__altura = args[2]
        else:
            print("Error, los atributos son incorrectos.") 

    def desplazar(self):
        turtle.color(self.__color)
        turtle.speed(3)
        turtle.setup(600, 600)
        turtle.bgcolor("black")
        turtle.speed(0)
        turtle.width(4)
        for i in range(3):
            turtle.forward(100)
            turtle.left(120)
        turtle.hideturtle()
        turtle.Screen().exitonclick()
    
    def calcularArea(self):
        #El área o superficie de un triángulo cualquiera es igual al producto de la base por la altura dividido por dos.
        print("El área del triangulo es: ", (self.__base * self.__altura)/2)

    def calcularVolumen(self):
        opc = input("Desea calcular el área del prisma? (S/N): ")
        if opc == "S" or opc == "s":
            #El calculo del volumen de un prisma triangular es igual al producto del área de la base por la altura del cuerpo
            hc = int( input("Por favor ingrese la altura del cuerpo: ") )
            print( "El volumen del prisma triangular es: ", ((self.__base * self.__altura)/2) * hc )
        elif opc == "N" or opc == "n":
            print("Eso es todo, gracias!")
        else:
            print("La opcion indicada es incorrecta. Eso es todo, gracias!")

class Rectangulo(Figura):
    def __init__(self, *args):
        if len( args ) == 0:
            self.__color = "green"
            self.__base = 10
            self.__altura = 10
        elif len( args ) == 3:
            self.__color = args[0]
            self.__base = args[1]
            self.__altura = args[2]
        else:
            print("Error, los atributos son incorrectos.")
            
    def desplazar(self):
        turtle.color( self.__color)
        turtle.speed(1)
        turtle.setup(600, 600)
        turtle.bgcolor("black")
        turtle.speed(0)
        turtle.width(4)
        for i in range(4):
            if (i % 2) == 0:
                turtle.forward(50)
            else:
                turtle.forward(100)
            turtle.left(90)
        turtle.hideturtle()
        turtle.Screen().exitonclick()
    
    def calcularArea(self):
        #El area de un rectangulo es igual a la altura por la base
        print( "El área del rectángulo es: ", ( self.__altura * self.__base ) )
    
    def calcularVolumen(self):
        #El volumen de un prisma rectangular es igual al producto del área de la base por la altura del cuerpo
        opc = input("Desea calcular el área del prisma? (S/N): ")
        if opc == "S" or opc == "s":
            #El calculo del volumen de un prisma triangular es igual al producto del área de la base por la altura del cuerpo
            hc = int( input("Por favor ingrese la altura del cuerpo: ") )
            print( "El volumen del prisma triangular es: ", ( self.__base * self.__altura ) * hc )
        elif opc == "N" or opc == "n":
            print("Eso es todo, gracias!")
        else:
            print("La opcion indicada es incorrecta. Eso es todo, gracias!")
        
class Rombo(Figura):
    def __init__(self, *args):
        if len( args ) == 0 :
            self.__color = "green"
            self.__diagonalMayor = 10
            self.__diagonalMenor = 10
        elif len( args ) == 3:
            self.__color = args[0]
            self.__diagonalMayor = args[1]
            self.__diagonalMenor = args[2]
        else:
            print("Error, los atributos son incorrectos.")
    
    def desplazar(self):
        turtle.color(self.__color)
        turtle.speed(3)
        turtle.setup(600, 600)
        turtle.bgcolor("black")
        turtle.speed(0)
        turtle.width(4)
        turtle.right(-45)
        for i in range(4):
            turtle.forward(150)
            turtle.right(90)
        turtle.hideturtle()
        turtle.Screen().exitonclick()
    
    def calcularArea(self):
        #El área de de un rombo es igual al producto de la diagonal mayor por la diagonal menor entre 2
        print( "El área del rombo es: ", ( self.__diagonalMayor * self.__diagonalMenor ) / 2 )
    
    def calcularVolumen(self):
        #El volumen de un prisma romboidal es igual al producto del área de la base entre 2 por la altura del cuerpo
        opc = input("Desea calcular el área del prisma? (S/N): ")
        if opc == "S" or opc == "s":
            #El calculo del volumen de un prisma triangular es igual al producto del área de la base por la altura del cuerpo
            hc = int( input("Por favor ingrese la altura del cuerpo: ") )
            print( "El volumen del prisma romboidal es: ", ( ( self.__diagonalMayor * self.__diagonalMenor ) / 2 ) * hc )
        elif opc == "N" or opc == "n":
            print("Eso es todo, gracias!")
        else:
            print("La opcion indicada es incorrecta. Eso es todo, gracias!")

#MENU PARA EL USUARIO
print("Bienvenido, por favor elija una de las siguentes opciones:")
print("1. Círculo")
print("2. Triángulo")
print("3. Rectángulo")
print("4. Rombo")
opc = int(input("Ingrese su opción: "))

if opc == 1:
    opc = input("Desea ingresar datos para el circulo? (S/N): ")
    if opc == "S" or opc == "s":
        rad = int(input("Valor del radio del circulo: "))
        color = input( "Digite el color que desea ver en la figura: " )
        fig = Circulo(color, rad)
        print( "Por favor, al ver la figura, de clic en cualquier parte de la ventana nueva para continuar." )
        fig.desplazar()
        fig.calcularArea()
        fig.calcularVolumen()
    elif opc == "N" or opc == "n":
        fig = Circulo()
        print( "Por favor, al ver la figura, de clic en cualquier parte de la ventana nueva para continuar." )
        fig.desplazar()
        print( "Eso es todo, gracias!" )
    else:
        print( "La opción es incorrecta." )
elif opc == 2:
    #Pregutar si el usuario quiere ingresar datos, si la respuesta es afirmativa (S), se pregunta y capturan los datos
    opc = input("Desea ingresar datos para el triángulo? (S/N): ")
    if opc == "S" or opc == "s":
        base = int( input( "Valor de la base del triángulo: " ) )
        altura = int( input( "Valor de la altura del triángulo: " ) )
        color = input( "Digite el color que desea ver en la figura: " )
        fig = Triangulo(color, base, altura)
        print( "Por favor, al ver la figura, de clic en cualquier parte de la ventana nueva para continuar." )
        fig.desplazar()
        fig.calcularArea()
        fig.calcularVolumen()
    elif opc == "N" or opc == "n":
        #Si la opción es negativa (N), solo se muestra la figura
        fig = Triangulo()
        print( "Por favor, al ver la figura, de clic en cualquier parte de la ventana nueva para continuar." )
        fig.desplazar()
        print( "Eso es todo, gracias!" )
    else:
        #Si la respuesta no es nunguna de las dos, Se termina el proceso.
        print( "La opción es incorrecta." )
elif opc == 3:
    opc = input("Desea ingresar datos para el rectángulo? (S/N): ")
    if opc == "S" or opc == "s":
        base = int( input( "Valor de la base del rectángulo: " ) )
        altura = int( input( "Valor de la altura del rectángulo: " ) )
        color = input( "Digite el color que desea ver en la figura: " )
        fig = Rectangulo(color, base, altura)
        print( "Por favor, al ver la figura, de clic en cualquier parte de la ventana nueva para continuar." )
        fig.desplazar()
        fig.calcularArea()
        fig.calcularVolumen()
    elif opc == "N" or opc == "n":
        fig = Rectangulo()
        print( "Por favor, al ver la figura, de clic en cualquier parte de la ventana nueva para continuar." )
        fig.desplazar()
        print( "Eso es todo, gracias!" )
    else:
        print( "La opción es incorrecta." )
elif opc == 4:
    opc = input("Desea ingresar datos para el rombo? (S/N): ")
    if opc == "S" or opc == "s":
        diagonalMayor = int( input( "Valor de la diagonal mayor del rombo: " ) )
        diagonalMenor = int( input( "Valor de la diagonal menor del rombo: " ) )
        color = input( "Digite el color que desea ver en la figura: " )
        fig = Rombo(color, diagonalMayor, diagonalMenor)
        print( "Por favor, al ver la figura, de clic en cualquier parte de la ventana nueva para continuar." )
        fig.desplazar()
        fig.calcularArea()
        fig.calcularVolumen()
    elif opc == "N" or opc == "n":
        fig = Rombo()
        print( "Por favor, al ver la figura, de clic en cualquier parte de la ventana nueva para continuar." )
        fig.desplazar()
        print( "Eso es todo, gracias!" )
    else:
        print( "La opción es incorrecta." )
else:
    print( "La opción es incorrecta." )
