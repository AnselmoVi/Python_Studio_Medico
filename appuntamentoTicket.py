import appuntamento
import tariff
import visita
from visita import Visita


class AppuntamentoTicket(appuntamento.Appuntamento):



    def __init__(self, nome, cv, ctipo, orario):
        self.nomePaziente = nome
        self.cv = cv
        self.ctipo = ctipo
        self.orario = orario

    def getOrario(self):
        pass

    def emettiFattura(self,costo):

        print(costo * 15 / 100)




    def cercaVisita(self) -> object:
        pass