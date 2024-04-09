from tkinter import *

def registreerimine():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    if kasutajanimi and parool:  
        with open("kasutajad.txt", "a") as f:
            f.write(f"{kasutajanimi},{parool}\n")
        registreerimise_teade.config(text="Kasutaja registreeritud!", fg="green")
    else:
        registreerimise_teade.config(text="Kasutajanimi või parool puudub!", fg="red")

def autoriseerimine():
    kasutajanimi = kasutajanime_sisestus.get()
    parool = parooli_sisestus.get()

    with open("kasutajad.txt", "r") as f:
        kasutajad = f.readlines()

    kasutajad = [kasutaja.strip().split(",") for kasutaja in kasutajad]
    if [kasutajanimi, parool] in kasutajad:
        autoriseerimise_teade.config(text="Kasutaja autoriseeritud!", fg="green")
    else:
        autoriseerimise_teade.config(text="Vale kasutajanimi või parool!", fg="red")

def muuda_parool_window():
    muuda_parool_aken = Tk()
    muuda_parool_aken.title("Muuda parool")
    muuda_parool_aken.geometry("300x200")

    def muuda_parool():
        kasutajanimi = kasutajanimi_entry.get()
        vana_parool = vana_parooli_entry.get()
        uus_parool = uus_parooli_entry.get()
        kinnita_parool = kinnita_parooli_entry.get()

        if uus_parool != kinnita_parool:
            muuda_parooli_teade.config(text="Uued paroolid ei kattu!", fg="red")
            return

        with open("kasutajad.txt", "r") as f:
            kasutajid = f.readlines()

        kasutajid = [kasutaja.strip().split(",") for kasutaja in kasutajid]
        for kasutaja in kasutajid:
            if kasutaja[0] == kasutajanimi:
                if kasutaja[1] == vana_parool:
                    kasutaja[1] = uus_parool
                    muuda_parooli_teade.config(text="Parool edukalt muudetud!", fg="green")
                    with open("kasutajad.txt", "w") as f:
                        for kasutaja in kasutajid:
                            f.write(','.join(kasutaja) + '\n')
                    muuda_parool_aken.destroy()
                    break
                else:
                    muuda_parooli_teade.config(text="Vale vana parool!", fg="red")
                    break
        else:
            muuda_parooli_teade.config(text="Kasutajanimi ei leitud!", fg="red")

    kasutajanimi_label = Label(muuda_parool_aken, text="Kasutajanimi:")
    vana_parooli_label = Label(muuda_parool_aken, text="Vana parool:")
    uus_parooli_label = Label(muuda_parool_aken, text="Uus parool:")
    kinnita_parooli_label = Label(muuda_parool_aken, text="Kinnita uus parool:")

    kasutajanimi_entry = Entry(muuda_parool_aken)
    vana_parooli_entry = Entry(muuda_parool_aken, show="*")
    uus_parooli_entry = Entry(muuda_parool_aken, show="*")
    kinnita_parooli_entry = Entry(muuda_parool_aken, show="*")

    muuda_button = Button(muuda_parool_aken, text="Muuda parool", command=muuda_parool)

    kasutajanimi_label.grid(row=0, column=0)
    vana_parooli_label.grid(row=1, column=0)
    uus_parooli_label.grid(row=2, column=0)
    kinnita_parooli_label.grid(row=3, column=0)

    kasutajanimi_entry.grid(row=0, column=1)
    vana_parooli_entry.grid(row=1, column=1)
    uus_parooli_entry.grid(row=2, column=1)
    kinnita_parooli_entry.grid(row=3, column=1)

    muuda_button.grid(row=4, columnspan=2)

    muuda_parool_aken.mainloop()

aken = Tk()
aken.geometry("500x500")
aken.title("Programma")
aken.configure(bg="#9cd0db")
aken.iconbitmap("mushroom.ico")

pealkiri = Label(aken,
                 text="Tere Tulemast!!",
                 bg="#329ba8",
                 fg="#111211",
                 cursor="star",
                 font="Times_New_Roman 16",
                 justify=CENTER,
                 height=3,width=26)

raam = Frame(aken)

kasutajanime_silt = Label(raam, text="Kasutajanimi:")
parooli_silt = Label(raam, text="Parool:")

kasutajanime_sisestus = Entry(raam,
                              bg="#84d1e3",
                              fg="#111211",
                              font="Times_New_Roman 16",
                              width=16)

parooli_sisestus = Entry(raam,
                         bg="#84d1e3",
                         fg="#111211",
                         font="Times_New_Roman 16",
                         width=16,
                         show="*")

parooli_naita_checkbox = Checkbutton(raam,
                                     text="Näita parooli",
                                     bg="#84d1e3",
                                     fg="#111211",
                                     font="Times_New_Roman 12",
                                     command=lambda: toggle_parool_visibility(parooli_sisestus))

registreeri_nupp = Button(raam,
                          text="Registreeri",
                          bg="#19849c",
                          fg="#111211",
                          font="Times_New_Roman 16",
                          width=16,
                          command=registreerimine)

autoriseeri_nupp = Button(raam,
                          text="Autoriseeri",
                          bg="#19849c",
                          fg="#111211",
                          font="Times_New_Roman 16",
                          width=16,
                          command=autoriseerimine)

muuda_parool_nupp = Button(raam,
                           text="Muuda parool",
                           bg="#19849c",
                           fg="#111211",
                           font="Times_New_Roman 16",
                           width=16,
                           command=muuda_parool_window)

registreerimise_teade = Label(raam, text="", font="Times_New_Roman 12")
autoriseerimise_teade = Label(raam, text="", font="Times_New_Roman 12")
muuda_parooli_teade = Label(raam, text="", font="Times_New_Roman 12")

pealkiri.pack()
raam.pack()
kasutajanime_silt.grid(row=0,column=0)
kasutajanime_sisestus.grid(row=0,column=1)
parooli_silt.grid(row=1,column=0)
parooli_sisestus.grid(row=1,column=1)
parooli_naita_checkbox.grid(row=2, columnspan=2)
registreeri_nupp.grid(row=3,column=0)
autoriseeri_nupp.grid(row=3,column=1)
muuda_parool_nupp.grid(row=4,columnspan=2)
registreerimise_teade.grid(row=5, columnspan=2)
autoriseerimise_teade.grid(row=6, columnspan=2)
muuda_parooli_teade.grid(row=7, columnspan=2)

def toggle_parool_visibility(entry):
    if entry["show"] == "*":
        entry["show"] = ""
    else:
        entry["show"] = "*"

aken.mainloop()
