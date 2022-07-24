#Clase String
#Es un objeto, con lo cual, disponemos de metodos para manipular de una mejor manera las cadenas de caracteres.

def claseString():
    """
    En python no hay necesidad de declarar que la nueva variable sea de tipo String,
    unicamente solo establecer la nueva variable y asignarle una cadena de caracteres.
    """

    print( "¡Clase String!" )

    cadena = "Ingeniería de Software"
    #Podemos saber el tipo de dato de la variable "cadena" con la siguente linea.
    print( type( cadena ) )

    #Uno de los mentodos de la clase String es el comprobar si la cadena de caracteres empienza o finaliza por cierta letra o plabra
    #Este nos devuelve vedadero o falso.
    inicioCadena = cadena.startswith( "Inge" )
    finalCadena = cadena.endswith( "Adios" )
    print( inicioCadena )
    print( finalCadena )

    #Así mismo, podemos buscar un subtring o subcadena de caracteres.
    buscarCadena = cadena.find( "Software" ) 

    #Tambien podemos reemplazar una parte de la cadena de caracteres por una nueva.
    reemplazoCadena = cadena.replace( "de", "en" )
    print( "La cadena -", cadena, "- Se reemplazo por -", reemplazoCadena, "-."  )

    #Al igual, podemos unir dos o más cadenas de caracteres.
    unionCadena = " y ".join(["A", "B", "C"])
    print( unionCadena )

    #Finalmente, podemos dividir una cadena, indicando un ccaracter como referencia de división
    dividirCadena = cadena.split( " " )
    print( dividirCadena )

#Clase StringBuffer
def claseStringBuffer():
    print( "¡Clase StringBuffer!" )
    #En una clase StringBuffer el tamaño de la cadena de caracteres puede variar.
    print( "En Python no existe una clase StringBuffer." )

#Clase StringTokenizer
def claseStringTokenizer():
    print( "¡Clase StringTokenizer!" )
    #Sirve para separar una cadena de caracteres en una serie de elementos o tokens
    print( "En Python no existe una clase StringTokenizer." )


claseString()
claseStringBuffer()
claseStringTokenizer()