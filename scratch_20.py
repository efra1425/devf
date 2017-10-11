



class Carros(object):
    def __init__(self,rines,aireacondicion,motor,puertas, llave):
        self.rines = rines
        self.aireacondicion = aireacondicion
        self.motor = motor
        self.puertas = puertas
        self.llave = llave





    def prender(self, key):
        print dos #valor =
        self.__llave = "12345"
        if self.__llave == key:
            print "esta prendido"
        else:
            print "imposible prender"

    def confirma_prendido(self,prendido = False):
        if self.motor == prendido :
            print "coche apagado "

    def contar_rines(self):
        return "numeros de rines es" + str(self.rines)

class Coches_Del_Aio(Carros):
    def __init__(self,rines,aireacondicion,motor,puertas, llave, electrico,color,size):
        super(Coches_Del_Aio,self).__init__(rines,aireacondicion,motor,puertas, llave)
        self.electrico = electrico
        self.color = color
        self.size = size


    def electrico_and_safe(self,):






bmw = Carros(2,True, False ,4,"abcde")
print bmw.contar_rines()
print bmw.confirma_prendido(bmw.motor)

new = Coches_Del_Aio(2,True, False ,4,"abcde",True,"azul","grande")
print new.electrico
print new.motor