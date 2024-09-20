print(" Clases V2 Roberto Gaytan 22308051281202 ")

# zona de clase
class Datos:
    # CONTRUCTOR DE FUNCION
    def __init__(self, estatura, peso):
        self.estatura=estatura
        self.peso=peso

    def mostrar_datos(self):
        print(f"Estatura : {self.estatura} mts, peso {self.peso} Kg")


    # LISTA 
    def mi_lista(self):
        Aeropuertos=["Aeropuerto 1 (FRA)","Aeropuerto 2 (ESP)","Aeropuerto 3 (ENG)"]
        print(Aeropuertos)
        for aer in Aeropuertos:
            print(aer)


    # TUPLA 
    def mi_tupla(self):
        Ciudades=("Paris","Barcelona","Manchester")
        print(Ciudades)
        for ciu in Ciudades:
            print(ciu)


    # CONJUNTO
    def mi_conjunto(self):
        paises={"Francia","España","Inglaterra"}
        print(paises)
        for pais in paises:
            print(pais)
    # DICCIONARIO    
    def mi_diccionario(self):
        thisdict = {
        "Partida:": "Manchester, Inglaterra",
        "Destino:": "Barcelona, España",
        "Fecha y Hora": 18.30
    }
        print(thisdict)
        for x, y in thisdict.items():
            print(x, y)

#CREACION DE OBJETO    
info=Datos(1.69,50)

#UTILIZACION DE OBJETOS
info.mostrar_datos()
print("LISTA DE AEROPUERTOS")
print("")
info.mi_lista()
print("")
print("")
print("Tupla DE Ciudades")
print("")
info.mi_tupla()
print("")
print("")
print("Conjunto DE Paises")
print("")
info.mi_conjunto()
print("")
print("")
print("Diccionario DE Boleto")
print("")
info.mi_diccionario()
