

class Calculadora(object):
    def __init__(self,marca_param ):
        self.marca = marca_param

    def sumar(self,numero1,numero2):
        resultado = numero1 + numero2
        return resultado

    def restar(self,numero1,numero2):
        resultado = numero1 - numero2
        return resultado

    def multiplicar(self,numero1,numero2):
        resultado = numero1 * numero2
        return resultado


casio = Calculadora ("casio")

print casio.sumar(3,4)

