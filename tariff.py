import visita
from visita import Visita


class Tarifarrio():




    def __init__(self):
        self.listaVisite=[]



    def getListaVisite(self):
        return self.listaVisite

    def setListaVisite(self,visita):
        pass

    def getVisita(self,ctipo):
        x: Visita
        for x in self.listaVisite:
            if x.getEquals(ctipo):
                return x
        
        return None

    def stampa(self):
        for x in self.listaVisite:
            print(str(x.ctipo) +" "+ str(x.costo) +" " + str(x.durata) + " \n")

    def cercaCosto(self,costo):
        for x in self.listaVisite:
            if x.costo==costo:
                print(str(x.ctipo) +" "+ str(x.costo) +" " + str(x.durata) + " \n")
                print(x.costo)

    def cercaTipo(self,tipo) :
        x:visita.Visita
        for x in self.listaVisite:
            if(x.ctipo==tipo):
                print(x.ctipo +" "+ str(x.costo) + str(x.durata) )
                return x
    def InserisciVisita(self):
        n=int(input("inserisci la durata"))
        c=int(input("inserisci il costo"))
        ctipo=input("inserisci il codice")
        self.listaVisite.append(visita.Visita(n,c,ctipo))




