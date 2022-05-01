from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from pyperclip import copy
from time import sleep
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.OKBLUE}LOG > Couleurs initialisées{bcolors.ENDC}")
closed = False

file = 'liste_mots_francais.txt'
f=open(file,'r')
data = f.read()
print(f"{bcolors.OKBLUE}LOG > Chargement de la liste de mots...{bcolors.ENDC}")
listemots = data.lower()
listemots = listemots.split(" ")
print(f"{bcolors.OKBLUE}LOG > Chargement terminé{bcolors.ENDC}")
found = []
count = 0
def quitter():
    print(f"{bcolors.WARNING}LOG > Demande de fermeture{bcolors.ENDC}")
    yesno = messagebox.askyesno("Annuler", "Êtes-vous sur de vouloir quitter?")
    if yesno == True:
        print(f"{bcolors.FAIL}LOG > FindWords quitté{bcolors.ENDC}")
        closed = True
        exit()
    else:
        print(f"{bcolors.OKGREEN}LOG > Demande de fermeture annulée{bcolors.ENDC}")
        closed = False
        return "cancelled"
def motsaleatoires():
    print(f"{bcolors.OKBLUE}LOG > Menu mots aléatoires ouvert{bcolors.ENDC}")
    nb = simpledialog.askinteger("Mots aléatoires", "Combien de mots aléatoires veux-tu générer?", minvalue=0, maxvalue=23066)
    if nb == None:
        print(f"{bcolors.WARNING}LOG > Mots aléatoires: annulé")
        quitter()
        if closed == False:
            nb = simpledialog.askinteger("Mots aléatoires", "Combien de mots aléatoires veux-tu générer? Cliquer sur annuler ou fermer cette fenêtre va générer une erreur.", minvalue=0, maxvalue=23066)
    try:
        rndwords = []
        foundmenu = Tk()
        foundmenu.title("Résultats")
        foundmenu.geometry("200x600")
        results = Text(foundmenu)
        print(f"{bcolors.OKBLUE}LOG > Recherche motsaleatoires{bcolors.ENDC}")
        for n in range(0, nb):
            arajouter = listemots[randint(0,len(listemots))]
            rndwords.append(arajouter)
            results.insert(1.0, arajouter + "\n")
        results.pack()
        ttk.Label(foundmenu, text="Mots trouvés: " + str(len(rndwords))).pack()
        ttk.Button(foundmenu, text="Copier liste python", command=lambda: copy(str(rndwords))).pack()
        ttk.Button(foundmenu, text="Copier liste", command=lambda: copy(results.get("1.0","end"))).pack()
        ttk.Button(foundmenu, text="Fermer", command=foundmenu.destroy).pack() 
    except:
        print(f"{bcolors.FAIL}LOG > Mots aléatoires: Erreur: Deuxième fenêtre de demande de nombre fermée ou annulée{bcolors.ENDC}")
def chercherwordsin(writedword):
    print(f"{bcolors.OKBLUE}LOG > Recherche wordsin{bcolors.ENDC}")
    found = []
    for x in range(0,len(listemots)):
        selected = listemots[x].lower()
        #print(str(x) + "/" + str(23066))
        if selected in writedword:
            found.append(selected)
    foundmenu = Tk()
    foundmenu.title("Résultats")
    foundmenu.geometry("200x600")
    foundmenu.resizable(False, False)
    results = Text(foundmenu)
    found = list(set(found))
    for i in range(0,len(found)):
        y = found[i]
        results.insert(1.0, y + '\n')
    results.pack()
    ttk.Label(foundmenu, text="Mots trouvés: " + str(len(found))).pack()
    ttk.Button(foundmenu, text="Copier liste python", command=lambda: copy(str(found))).pack()
    ttk.Button(foundmenu, text="Copier liste", command=lambda: copy(results.get("1.0","end"))).pack()
    ttk.Button(foundmenu, text="Fermer", command=foundmenu.destroy).pack()
def chercherwords(swith, ewith, wlen, contains):
    print(f"{bcolors.OKBLUE}LOG > Recherche chercherwords - Paramètres: swith: " + swith + " ewith: " + ewith + " wlen: " + wlen + " contains: " + contains + f"{bcolors.ENDC}")
    found = []
    count = 0
    if str(contains) == "":
        contains = True
    else:
        contains = list(contains)
    for z in range(0,len(listemots)):
        count = 0
        sel = listemots[z].lower()
        if sel.startswith(str(swith)) or str(swith) == "":
            if sel.endswith(str(ewith)) or str(ewith) == "":
                if str(len(sel)) == str(wlen) or str(wlen) == "":
                    if contains == True:
                        found.append(sel)
                    else:
                        for x in range(0,len(contains)):
                            if contains[x] in listemots[z]:
                                count += 1
                            if count == len(contains):
                                found.append(listemots[z])

    foundmenu = Tk()
    foundmenu.title("Résultats")
    foundmenu.geometry("200x600")
    foundmenu.resizable(False, False)
    results = Text(foundmenu)
    found = list(set(found))
    for i in range(0,len(found)):
        y = found[i]
        results.insert(1.0, y + '\n')
    results.pack()
    ttk.Label(foundmenu, text="Mots trouvés: " + str(len(found))).pack()
    ttk.Button(foundmenu, text="Copier liste python", command=lambda: copy(str(found))).pack()
    ttk.Button(foundmenu, text="Copier liste", command=lambda: copy(results.get("1.0","end"))).pack()
    ttk.Button(foundmenu, text="Fermer", command=foundmenu.destroy).pack()
def chercherwordsscrabble(swith, ewith, wlen, contains):
    print(f"{bcolors.OKBLUE}LOG > Recherche chercherwordsscrabble - Paramètres: swith: " + swith + " ewith: " + ewith + " wlen: " + wlen + " contains: " + contains + f"{bcolors.ENDC}")
    found = []
    count = 0
    if str(contains) == "":
        contains = True
    else:
        contains = list(contains)
    spacement = len(contains)-int(wlen)
    if int(len(contains)) > int(wlen):
        for x in range(0,spacement):
            del contains[0]
    for z in range(0,len(listemots)):
        count = 0
        sel = listemots[z].lower()
        if sel.startswith(str(swith)) or str(swith) == "":
            if sel.endswith(str(ewith)) or str(ewith) == "":
                if int(len(sel)) <= int(wlen) or str(wlen) == "":
                    if contains == True:
                        found.append(sel)
                    else:
                        for x in range(0,len(contains)):
                            if contains[x] in listemots[z]:
                                count += 1
                            if count == len(contains):
                                found.append(listemots[z])
                    
    foundmenu = Tk()
    foundmenu.title("Résultats")
    foundmenu.geometry("200x600")
    foundmenu.resizable(False, False)
    results = Text(foundmenu)
    found = list(set(found))
    for i in range(0,len(found)):
        y = found[i]
        results.insert(1.0, y + '\n')
    results.pack()
    ttk.Label(foundmenu, text="Mots trouvés: " + str(len(found))).pack()
    ttk.Button(foundmenu, text="Copier liste python", command=lambda: copy(str(found))).pack()
    ttk.Button(foundmenu, text="Copier liste", command=lambda: copy(results.get("1.0","end"))).pack()
    ttk.Button(foundmenu, text="Fermer", command=foundmenu.destroy).pack()
def opnmenuchercher():
    print(f"{bcolors.OKBLUE}LOG > Menu chercher ouvert{bcolors.ENDC}")
    menu.destroy()
    menuchercher = Tk()
    menuchercher.geometry("250x235")
    menuchercher.title("FindWords")
    menuchercher.resizable(False, False)
    ttk.Label(menuchercher, text="Commence par:").pack()
    commencepar = ttk.Entry(menuchercher)
    commencepar.pack()
    ttk.Label(menuchercher, text="Termine par:").pack()
    terminepar = ttk.Entry(menuchercher)
    terminepar.pack()
    ttk.Label(menuchercher, text="Contient les lettres: ").pack()
    contient = ttk.Entry(menuchercher)
    contient.pack()
    ttk.Label(menuchercher, text="Nombre de lettres:").pack()
    nbrdelettres = ttk.Entry(menuchercher)
    nbrdelettres.pack()
    ttk.Button(menuchercher, text="GO!", command=lambda: chercherwords(commencepar.get(), terminepar.get(), nbrdelettres.get(), contient.get())).pack()
    ttk.Button(menuchercher, text="GO! (MODE SCRABBLE)", command=lambda: chercherwordsscrabble(commencepar.get(), terminepar.get(), nbrdelettres.get(), contient.get())).pack()
    ttk.Button(menuchercher, text="Fermer", command=quitter).pack()
    menuchercher.mainloop()
def opnmenuwordsin():
    print(f"{bcolors.OKBLUE}LOG > Menu wordsinwords ouvert{bcolors.ENDC}")
    menu.destroy()
    menuwordsin = Tk()
    menuwordsin.geometry("250x200")
    menuwordsin.title("FindWords")
    menuwordsin.resizable(False, False)
    ttk.Label(menuwordsin, text="Mot:").pack()
    mot = ttk.Entry(menuwordsin)
    mot.pack()
    ttk.Button(menuwordsin, text="GO!", command=lambda: chercherwordsin(mot.get())).pack()
    ttk.Button(menuwordsin, text="Fermer", command=quitter).pack()
    menuwordsin.mainloop()

print(f"{bcolors.OKBLUE}LOG > Menu principal ouvert{bcolors.ENDC}")
menu = Tk()
menu.geometry("250x200")
menu.title("FindWords")
menu.protocol("WM_DELETE_WINDOW", quitter)
menu.resizable(False, False)
ttk.Button(menu, text="Chercher des mots", command=opnmenuchercher).pack()
ttk.Button(menu, text="Trouver des mots dans un mot", command=opnmenuwordsin).pack()
ttk.Button(menu, text="Mot aléatoire", command=motsaleatoires).pack()
ttk.Button(menu, text="Fermer", command=quitter).pack()
menu.mainloop()
