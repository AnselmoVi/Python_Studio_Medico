# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import agenda
import appuntamento
import appuntamentoNoTicket
import appuntamentoTicket
import tariff
import visita


def menu():
    print(
        "1. crea tariffario \n 2. stamoa tarifarrio \n 3. cerca nel tariffario \n 4.Crea l'agenda per un determinato giorno  \n 6. emetti fattura per il tuo appuntamento")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    v = visita.Visita(1, 100, "vermi1")
    t = tariff.Tarifarrio()
    a = agenda.Agenda()
    scelta = True

    while (scelta):
        menu()
        scelta = int(input("Cosa desideri fare?"))
        if scelta == 1:

            t.InserisciVisita()
        if scelta == 2:
            t.stampa()
        if scelta == 3:
            tipo = int(input("Cosa vuoi cercare? 1. Per il costo 2. per tipo "))
            if tipo == 1:
                costo = input("inserisci il costo")
                t.cercaCosto(costo)
            if tipo == 2:
                ctipO = input("inserisci il tipo")
                t.cercaTipo(ctipO)
        if scelta == 4:
            giorno = int(input("Inserts il giorno della settimana"))
            g="lunedì"
            if giorno == 1:
                g = "Lunedì"
            if giorno == 2:
                g = "Martedì"
            if (giorno == 3):
                g = "Mercoledì"
            if (giorno == 4):
                g = "Giovedì"
            if (giorno == 5):
                g = "Venerdì"
            else:
                g = "Sabato"
            nome = str(input("nome"))
            cv = input("cv")
            ctipo = input("tipovisita")
            orario = input("orario")
            ticket = int(input("1 per ticker, 2. per intero "))
            if (ticket == 1):
                app = appuntamentoTicket.AppuntamentoTicket(nome, cv, ctipo, orario)

                v=t.cercaTipo(ctipo)
                a.inserisciAppuntamento(app, g,v.durata)
            if (ticket == 2):
                app = appuntamentoNoTicket.AppuntamentoNoTicket(nome, cv, ctipo, orario)
                v = t.cercaTipo(ctipo)
                a.inserisciAppuntamento(app, g, v.durata)

        if scelta == 6:


            g = str(input("inserisci il tuo nome"))
            fattura = a.cercaAppuntamento(g,t)
            print(fattura)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
