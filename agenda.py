import appuntamento
import tariff


class Agenda():


    def __init__(self):
        self.appuntamenti=[None] * 12


    def inserisciAppuntamento(self, a, giorno,slot):

        if giorno == "Lunedì":
            print("lunedi")
            self.inserimento(0, a,slot)
        elif giorno == "Martedì":
            print("maer")
            self.inserimento(1,a, slot)
        elif giorno == "Mercoledì":
            self.inserimento(2, a,slot)
        elif giorno == "Giovedì":
            self.inserimento(3, a,slot)
        elif giorno == "Venerdì":
            self.inserimento(4, a,slot)
        else:
            self.inserimento(5, a,slot)

    def stampa(self, giorno):
        x:appuntamento.Appuntamento
        for x in self.appuntamenti:
            x.stampa()

    def inserimento(self, n, app,nslot):
        app: appuntamento.Appuntamento
        for x in range(0,nslot):
            self.appuntamenti.insert(n, app)






    def cercaAppuntamento(self,nome,t):
        noccupati=0
        x: appuntamento.Appuntamento
        t:tariff.Tarifarrio

        for x in self.appuntamenti:
            if x:

                if(x.nomePaziente==nome):
                    costo=t.getVisita(x.ctipo).costo
                    x.emettiFattura(costo)
                    return x.emettiFattura(costo)
