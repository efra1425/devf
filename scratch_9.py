def numeros_divisibles():
    my_dict = []
    for x in range (2000 , 3200 ,  ) :
        if x %7==0 and x %5 != 0:
            my_dict.append(x)
    print my_dict

numeros_divisibles()