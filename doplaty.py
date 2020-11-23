from tkinter import *
root = Tk()
root.title("Dopłaty")

def woda():
    wilg = w.get()
    wilg = float(wilg)
    baza=b.get()
    baza = float(baza)
    global wynik_woda
    wynik_woda=0.0
    if((wilg<9.0) and (wilg>6.0)):
        wynik_woda=(((9.0-wilg)*0.5)/100.0)*baza
    elif(wilg > 9.0):
        wynik_woda = ((wilg - 9.0) / 100) * baza
        wynik_woda*=-1
    wynik_wilg.delete(0, END)
    wynik_wilg.insert(0, "%.3f" % wynik_woda)

def syf():
    brud = z.get()
    brud = float(brud)
    baza = b.get()
    baza = float(baza)
    global wynik_syf
    wynik_syf=0.0
    if (brud<2.0):
        wynik_syf = (((2.0 - brud) * 0.5) / 100.0) * baza
    elif(brud>2.0):
        wynik_syf = ((brud - 2.0) / 100.0) * baza
        wynik_syf *= -1
    wynik_zan.delete(0, END)
    wynik_zan.insert(0, "%.3f" % wynik_syf)


def oil():
    olej = o.get()
    olej = float(olej)
    baza = b.get()
    baza = float(baza)
    global wynik_oil
    wynik_oil = 0.0
    if (olej > 40.0):
        wynik_oil = (((olej - 40.0) * 1.5) / 100.0) * baza
    elif(olej < 40.0):
        wynik_oil = (((40.0 - olej) * 1.5) / 100.0) * baza
        wynik_oil *= -1
    wynik_o.delete(0, END)
    wynik_o.insert(0, "%.3f" % wynik_oil)

def oblicz_i_pokaz():
    baza = b.get()
    baza = float(baza)
    oil()
    syf()
    woda()
    cena= baza + wynik_oil + wynik_syf + wynik_woda
    wynik_final.delete(0, END)
    wynik_final.insert(0, "%.2f" % cena)


tytul = Label(root, text="Dopłaty!", font = ("Calibri", 40))
tytul.grid(row=0, column=0, columnspan=4)

napis_baza = Label(root, text="Cena Bazowa:", font = ("Calibri", 20)).grid(row=1, column=0)
b = Entry(root, width=10, borderwidth=3, font = ("Calibri", 20))
b.grid(row=1,column=1)


napis_wilgotnosc = Label(root, text="Wilgotność:", font = ("Calibri", 20)).grid(row=2, column=0)
w = Entry(root, width=10, borderwidth=3, font = ("Calibri", 20))
w.grid(row=2,column=1)


napis_zanieczyszczenia = Label(root, text="Zanieczyszczenia:", font = ("Calibri", 20)).grid(row=3, column=0)
z = Entry(root, width=10, borderwidth=3, font = ("Calibri", 20))
z.grid(row=3,column=1)


napis_olej = Label(root, text="Olej:", font = ("Calibri", 20)).grid(row=4, column=0)
o = Entry(root, width=10, borderwidth=3, font = ("Calibri", 20))
o.grid(row=4,column=1)





przycisk=Button(root, text="Oblicz", padx=150, pady=5, bg="LightGrey", font = ("Calibri", 20), command=oblicz_i_pokaz)
przycisk.grid(row=5, column=0, columnspan=4)

napis_wilgotnosc2 = Label(root, text="Cena wilg.:", font = ("Calibri", 20)).grid(row=2, column=2)
wynik_wilg = Entry(root, width=10, borderwidth=3, font = ("Calibri", 20))
wynik_wilg.grid(row=2,column=3)

napis_zanieczyszczenia2 = Label(root, text="Cena zan.:", font = ("Calibri", 20)).grid(row=3, column=2)
wynik_zan = Entry(root, width=10, borderwidth=3, font = ("Calibri", 20))
wynik_zan.grid(row=3,column=3)

napis_olej2 = Label(root, text="Cena olej:", font = ("Calibri", 20)).grid(row=4, column=2)
wynik_o = Entry(root, width=10, borderwidth=3, font = ("Calibri", 20))
wynik_o.grid(row=4,column=3)

napis_cena = Label(root, text="Finalna Cena:", font = ("Calibri", 20)).grid(row=9, column=0)
wynik_final = Entry(root, width=10, borderwidth=3, font = ("Calibri", 20))
wynik_final.grid(row=9,column=1)


root.mainloop()
