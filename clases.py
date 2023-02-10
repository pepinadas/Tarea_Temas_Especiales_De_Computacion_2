class Automovil:
    def __init__(self, marca, sub_marca, anio, kms, transmision):
        self.__marca = marca
        self.__sub_marca = sub_marca
        self.__anio = anio
        self.__kms = kms
        self.__transmision = transmision
    def set_marca(self, m):
        self.__marca=m
    def get_marca(self):
        return self.__marca
    def set_sub_marca(self, sm):
        self.__sub_marca = sm
    def get_sub_marca(self):
        return self.__sub_marca
    def set_anio(self, a):
        self.__anio = a
    def get_anio(self):
        return self.__anio
    def set_kms(self, km):
        self.__kms = km
    def get_kms(self):
        return self.__kms
    def set_transmision(self, t):
        self.__transmision = t
    def get_transmision(self):
        return self.__transmision
    
    def __str__(self):
        resultado = self.__marca + "," + self.__sub_marca + "," + str(self.__anio) + "," + str(self.__kms) + "," + self.__transmision
        return resultado