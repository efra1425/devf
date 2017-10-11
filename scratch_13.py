
class Tv():
    iva= 0.10
    def __init__(self,color,marca,tamaio,pantalla,precio):

        self.color = color
        self.marca = marca
        self.tamaio = tamaio
        self.pantalla = pantalla
        self.precio = precio
        self.preciototal=precio


    def precio_de_pantalla(self):
        self.precio = int(self.precio*self.iva)

    def precio_mas_iva(self):
        self.preciototal = float(self.preciototal + self.iva)

    def todas_en_una(self):
        return '{}{} {} {} {}'.format(self.color,self.marca,self.tamaio,self.pantalla,self.precio)

    def color(self):
        return self.color

tv1= Tv ("azul","samsum","45","plana",2500)
tv2= Tv ("amarillo","panasonic","50","curva",3000)

#print tv1.__dict__
#print tv2.__dict__

print tv1.precio
tv1.precio_de_pantalla()
print tv1.precio
tv1.precio_mas_iva()
print tv1.preciototal


