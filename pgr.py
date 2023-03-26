#Modules
from tkinter import Tk , Menu , Canvas , Label , Entry , StringVar , Button , Text
from PIL import Image, ImageTk
from random import randint
from winsound import PlaySound

#Functions
def creer_fenetre():
    fenetre = Tk()
    fenetre.title("Quiz")
    return fenetre

def creer_widgets():
    zone_graphique = Canvas(fenetre, width=1300, height=700, bg='black')
    zone_graphique.grid(row=0, column=0, columnspan=3)

    mon_texte = Label(fenetre, text="Entre ton pseudo : ")
    mon_texte.grid(row=1, column=0)

    champ_saisie = Text(fenetre, height=1, width=14)
    champ_saisie.grid(row=1, column=1)

    bouton_valider = Button(fenetre, text="Valider", width=12, command = saisir)
    bouton_valider.grid(row=1, column=2)

    return zone_graphique, mon_texte, champ_saisie, bouton_valider

def saisir():
    global nom1
    nom1 = champ_saisie.get("1.0", "end-1c")
    text2 = "Bienvenue à toi : " + nom1
    nom = "Joueur : " + nom1
    mon_texte.configure(text = nom1)
    champ_saisie.destroy()
    ztext = zone_graphique.create_text(650, 20, anchor = "n", text = text2, fill = "gold", font = "arial 25")
    textes.append(ztext)
    ztext2 = zone_graphique.create_text(650, 85, anchor = "n", text = "Les règles sont simples :", fill = "white", font = "arial 25")
    textes.append(ztext2)
    ztext3 = zone_graphique.create_text(650, 150, anchor = "n", text = "- vous devez répondre aux questions correctement pour gagner jusqu'à 20 points !", fill = "white", font = "arial 25")
    textes.append(ztext3)
    ztext4 = zone_graphique.create_text(650, 215, anchor = "n", text = "- vous avez un maximum de 3 fautes ! faites attention !", fill = "white", font = "arial 25")
    textes.append(ztext4)
    ztext5 = zone_graphique.create_text(650, 280, anchor = "n", text = "Bonne chance !", fill = "white", font = "arial 25")
    textes.append(ztext5)
    ztext6 = zone_graphique.create_text(650, 320, anchor = "n", text = "Classement :", fill = "royalblue", font = "arial 20")
    textes.append(ztext6)
    burec = zone_graphique.create_rectangle(460,525,840,600, fill="black", width=4, outline="cyan")
    textes.append(burec)
    ztext7 = zone_graphique.create_text(650, 540, anchor = "n", text = "Commencer", fill = "royalblue", font = "arial 25")
    textes.append(ztext7)
    fichier()
    textd()
    fichier2()

def click(event):
    x = event.x
    y = event.y
    xmin , xmax , ymin , ymax = limites()
    if x > xmin and x < xmax and y > ymin and y < ymax :
        zone_graphique.delete('all')
        questions()

def limites():
    xmin, ymin = 460, 525
    xmax = xmin + 460
    ymax = ymin + 75
    return xmin, xmax, ymin, ymax

def textd():
    taille = 320
    if len(l) > 5 :
        n = 5
    else :
        n = len(l)
    for i in range(n):
        cl = str(l[i]) + " " + str(nom[i][0])
        text45 = "ztextcl" + str(i)
        taille += 30
        text45 = zone_graphique.create_text(650, taille, anchor = "n", text = cl, fill = "light blue", font = "arial 15")

def fichier():
    global a
    global l
    global nom
    fichier = open("classement.txt", "r", encoding = "utf-8")
    c = fichier.readline()
    while c != "":
        a.append(c.split(","))
        l.append(a[0][1][:2])
        nom.append(a[0])
        c = fichier.readline()
        a = []
    return l
def fichier2():
    global q
    global b
    fichier = open("questions.txt", "r", encoding = "utf-8")
    c = fichier.readline()
    while c != "":
        q.append(c.split(":"))
        c = fichier.readline()
    return q
def questions():
    global nb
    global fautes
    global score
    global btn1, btn2

    nb+=1
    tex="Question n° "+str(nb)
    atext = zone_graphique.create_text(650, 20, anchor = "n", text = tex, fill = "white", font = "arial 20")
    tex1="Pour l'instant vous avez "+str(fautes)+" faute(s)"
    atext45 = zone_graphique.create_text(280, 620, anchor = "n", text = tex1, fill = "white", font = "arial 20")
    tex2="Pour l'instant vous avez un score de : "+str(score)
    atext46 = zone_graphique.create_text(1000, 620, anchor = "n", text = tex2, fill = "white", font = "arial 20")
    nbq = randint(0,81)
    qmeme.append(nbq)
    while nbq in qmeme:
        nbq = randint(0,81)
    question = str(q[nbq][0])
    lbr = str(q[nbq][1])
    atext2 = zone_graphique.create_text(650, 85, anchor = "n", text = question, fill = "white", font = "arial 15")
    if lbr == "vrai\n" :
        btn1=Button(fenetre, text = "Vrai", width = 20, height = 3, activebackground='green', font = 'arial 20',command = scoregagne)
        btn1.place(x=500,y=200)
        btn2=Button(fenetre, text = "Faux", width = 20, height = 3, activebackground='red', font = 'arial 20',command = scoreperdu)
        btn2.place(x=500,y=400)

    else:
        btn1=Button(fenetre, text = "Vrai", width = 20, height = 3, activebackground='red',font = 'arial 20', command = scoreperdu)
        btn1.place(x=500,y=200)
        btn2=Button(fenetre, text = "Faux", width = 20, height = 3, font = 'arial 20', activebackground='green', command = scoregagne)
        btn2.place(x=500,y=400)
    return btn1, btn2
def scoregagne():
    global score
    score+=1
    zone_graphique.delete('all')
    if score >=20:
        zone_graphique.delete('all')
        btn4=Button(fenetre, text = "Quitter", width = 30, height = 8, font = 'arial 25',bg='yellow',command = close_window)
        btn4.place(x=390,y=190)
        atext6 = zone_graphique.create_text(650, 85, anchor = "n", text = "Bravo! Vous avez réussi à faire 20 points!", fill = "white", font = "arial 25")
        scorew()
    else:
        btn1, btn2 = questions()


def scoreperdu():
    global vie
    global fautes
    vie-=1
    fautes+=1
    if vie <= 0:
        perdu()
    else:
        zone_graphique.delete('all')
        btn1, btn2 = questions()


def perdu():
    zone_graphique.delete('all')
    btn5=Button(fenetre, text = "Quitter", width = 30, height = 8, font = 'arial 25',bg='yellow',command = fenetre.destroy)
    btn5.place(x=390,y=190)
    atext4 = zone_graphique.create_text(650, 85, anchor = "n", text = "Dommage vous avez déjà fait 3 fautes :(", fill = "white", font = "arial 25")
    tex3="Vous avez eu un score de : "+str(score)
    atext76 = zone_graphique.create_text(650, 620, anchor = "n", text = tex3, fill = "white", font = "arial 25")
    scorew()
def scorew():
    global score
    global vie
    global stop
    fichier3 = open("classement.txt", "a", encoding = 'utf-8')
    while stop == 1 :
        nomscore = str(nom1)
        fichier3.write(nomscore)
        fichier3.write(",")
        scorecla = str(score)
        fichier3.write(scorecla)
        fichier3.write("\n")
        stop +=1


#Variables
l = []
nom = []
a = []
textes = []
q = []
qmeme = []
score = 0
fautes = 0
vie = 3
nb = 0
stop = 1
#Main
fenetre = creer_fenetre()
zone_graphique, mon_texte, champ_saisie, bouton_valider = creer_widgets()
zone_graphique.bind("<ButtonPress-1>",click)

fenetre.mainloop()