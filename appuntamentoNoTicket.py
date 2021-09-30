import appuntamento
import tariff


class AppuntamentoNoTicket(appuntamento.Appuntamento):


    def getOrario(self):
        pass

    def __init__(self, nome, cv, ctipo, orario):
        self.nomePaziente = nome
        self.cv = cv
        self.ctipo = ctipo
        self.orario = orario

    def emettiFattura(self,costo):

      print(costo)

    def cercaVisita(self):
        pass

