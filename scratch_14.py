



class persona(object):
    def __init__(self,nombre,email,age):
        self.nombre = nombre
        self.__email = email
        self.__age = age

    def update_email(self,new_email):
        self.__email = new_email

    def email(self):
        return self.__email

    def __show_age(self):
        return self.__age

    def show_age(self):
        return self.__get_age()

    def __get_age(self):
        return self.__age

    # sobre carga de metodos

    def update_email(self, new_email, algo_mas):
        self.__email = new_email + algo_mas

tk = persona ('tk','no_entiendonimergas@gmail.com','26')
print  (tk.email())
print (tk.show_age())