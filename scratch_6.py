def numeros_intermedios():
    my_lista = []

    h = 0
    numero = input("cuantos numeros quieres ingresar")


    for x in range(numero):
        if numero > h :
            numeros = input("ingresa el numero")
        my_lista.append(numeros)
        h = +1

    print len(my_lista)
    if numero >  0:
        print my_lista [1:numero -1 ]
    print my_lista [0: -1 ]

    #print

numeros_intermedios()
