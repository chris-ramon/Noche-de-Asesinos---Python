# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="christian"
__date__ ="$23/08/2011 08:20:31 PM$"

class Vaso:
    def __init__(self,cantidad):
        self.__cantidad = cantidad
    def getCantidad(self):
        return self.__cantidad
    def setCantidad(self, cant):
        self.__cantidad = cant    
    def reducirCantidad(self):
        self.__cantidad = self.__cantidad - 1
    cantidad = property(getCantidad, setCantidad)