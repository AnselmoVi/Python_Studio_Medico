import abc
from abc import abstractmethod

import tariff


class Appuntamento():
    @abstractmethod
    def __init__(self,nome,cv,ctipo,orario):
        self.nomePaziente=nome
        self.cv=cv
        self.ctipo=ctipo
        self.orario=orario


    @abstractmethod
    def emettiFattura(self,costo):
      pass


    @abstractmethod
    def getOrario(self,durata):
        ora=self.orario

        print("La durata è " +durata)
        ora=(ora.spilt(":"))
        h=int((ora[0]-8))
        print(h)
        m=int((ora[1]))
        print(m)
        sum=h+m
        return sum


    def stampa(self):
        print(self.nomePaziente)
        print(self.cv)
        print(self.ctipo)
        print(self.orario)

