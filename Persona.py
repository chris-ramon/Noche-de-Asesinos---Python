# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="christian"
__date__ ="$23/08/2011 08:09:36 PM$"
import random
import Vaso
   
class Persona():
    def __init__(self, nombre):
        self.__nombre = nombre
   
    def getName(self):
        return self.__nombre
    
    def setName(self, name):
        self.__nombre = name
    
    def beberVaso(self, numero, envenenado):
        if numero == envenenado:               
            return "Estoy bebiendo!, (y nose que el vaso esta envenenado!)"
        else:
            return "Estoy bebiendo!"
    def envenenarVaso(self,invitados):
        envenenado = random.randint(2,invitados)
        return envenenado
    
    name = property(getName,setName)