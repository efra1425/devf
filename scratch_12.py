

#class Empleado:
    #pass

#empleado_1 = Empleado()
#empleado_2 = Empleado()

class Empleado:

    monto_para_aumento = 1.04
    numero_de_empleado = 0

    def __init__(self,nombre,apellido,salario):
        #self->current instanse
        self.nombre=nombre
        self.apellido=apellido
        self.email=nombre + "," + apellido + " @company.com "
        self.salario = salario
        Empleado.numero_de_empleado += 1

    def nombre_completo(self):
        return '{} {}'.format(self.nombre,self.apellido)
    def obtener_salario(self):
        return self.salario
    def aplicar_aumento(self):
        self.salario = int(self.salario*self.monto_para_aumento)

empleado_1 = Empleado("hugo","mecalco","90000")
empleado_2 = Empleado("efra","deniz","80000")



print Empleado.__dict__
print empleado_1.__dict__



