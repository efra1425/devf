
import os


def impor_imag():
    print os.getcwd()
    list_imagen= os.listdir("C:\Users\EFRA\Desktop\prank")
    os.chdir("C:\Users\EFRA\Desktop\prank")
    for x in range (len(list_imagen)):
        os.rename(list_imagen[x],list_imagen[x].translate(None,"0123456789"))

    print list_imagen
    print os.getcwd()
    # list_imagen.translate(None,"0123456789")
impor_imag()







       # print "".join([x for x in (list_imagen) if x.isdigit()])
    # print x

