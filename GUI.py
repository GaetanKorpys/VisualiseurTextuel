import tkinter as tk
from ivy.ivy import *
from Turtle import Turtle


class GUI():
    def __init__(self, master, queue, endCommand):

        self.queue = queue
        self.master = master

        self.orderReceive = tk.Label(self.master)
        self.orderReceive.pack()

        self.oldStateTurtle = tk.Label(self.master)
        self.oldStateTurtle.pack()

        self.newStateTurtle = tk.Label(self.master)
        self.newStateTurtle.pack()

        console = tk.Button(self.master, text='Close', command=endCommand)
        console.pack()

        #Position de la tortue selon la fenetre graphique du Visualiseur Graphique
        x = 400
        y = 300

        self.turtle = Turtle(x, y, -90)

    def processIncoming(self):
        """
        Handle all the messages currently in the queue (if any).
        """
        while self.queue.qsize():
            if not self.queue.empty():
                msg = self.queue.get()
                self.readCmdFromQueue(msg)


    def readCmdFromQueue(self, args):

        command = args[1]

        self.orderReceive.config(text=("Ordre reçu : " + str(args)))

        if re.match("^AVANCE [1-9][0-9]?$|^AVANCE 100$", args[1]):

            self.oldStateTurtle.config(text=("Position initale de la tortue : " + self.turtle.getPos()))

            message_parts = args[1].split(" ")
            nb = message_parts[1]

            self.turtle.avance(int(nb))

            self.newStateTurtle.config(text=("Nouvelle position : " + self.turtle.getPos()))



        elif re.match("^RECULE [1-9][0-9]?$|^RECULE 100$", command):

            self.oldStateTurtle.config(text=("Position initale de la tortue : " + self.turtle.getPos()))

            message_parts = args[1].split(" ")
            nb = message_parts[1]

            self.turtle.recule(int(nb))

            self.newStateTurtle.config(text=("Nouvelle position : " + self.turtle.getPos()))

        elif re.match("^TOURNEDROITE (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$", command):

            self.oldStateTurtle.config(text=("Angle initale de la tortue : " + str(self.turtle.angle)))

            message_parts = args[1].split(" ")
            nb = message_parts[1]

            self.turtle.tourne_droite(int(nb))

            self.newStateTurtle.config(text=("Nouvel angle : " + str(self.turtle.angle)))

        elif re.match("^TOURNEGAUCHE (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$", command):

            self.oldStateTurtle.config(text=("Angle inital de la tortue : " + str(self.turtle.angle)))

            message_parts = args[1].split(" ")
            nb = message_parts[1]

            self.turtle.tourne_gauche(int(nb))

            self.newStateTurtle.config(text=("Nouvel angle : " + str(self.turtle.angle)))

        elif re.match("^LEVECRAYON$", command):

            if self.turtle.crayon_leve :
                self.oldStateTurtle.config(text="Etat inital du crayon : levé")
            else:
                self.oldStateTurtle.config(text="Etat inital du crayon : baissé")

            self.turtle.leve_crayon()

            self.newStateTurtle.config(text="Nouvel etat du crayon : levé" )

        elif re.match("^BAISSECRAYON$", command):

            if self.turtle.crayon_leve:
                self.oldStateTurtle.config(text="Etat inital du crayon : levé")
            else:
                self.oldStateTurtle.config(text="Etat inital du crayon : baissé")

            self.turtle.baisse_crayon()

            self.newStateTurtle.config(text="Nouvel etat du crayon : baissé")

        elif re.match("^ORIGINE$", command):

            self.oldStateTurtle.config(text=("Position initale de la tortue : " + self.turtle.getPos()))

            self.turtle.origine()

            self.newStateTurtle.config(text=("Position initale de la tortue : " + self.turtle.getPos()))

        elif re.match("^RESTAURE", command):

            self.oldStateTurtle.config(text=("Position initale de la tortue : " + self.turtle.getPos() + "Angle initale de la tortue : " + str(self.turtle.angle)))

            self.turtle.restaure()

            self.newStateTurtle.config(text=("Position initale de la tortue : " + self.turtle.getPos() + "Angle initale de la tortue : " + str(self.turtle.angle)))

        elif re.match("^NETTOIE$", command):

            self.oldStateTurtle.config(text="Rien à nettoyer")

        elif re.match("^FCC (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]) (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]) (?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$", command):

            message_parts = command.split(" ")

            r = int(message_parts[1])
            g = int(message_parts[2])
            b = int(message_parts[3])

            self.oldStateTurtle.config(text=("Couleur initale du crayon : " + self.rgbToColor(self.turtle.couleur)))

            self.turtle.fcc(r, g, b)

            self.newStateTurtle.config(text=("Nouvelle couleur du crayon : " + self.rgbToColor(self.turtle.couleur)))

        elif re.match("^FCAP (?:36[0]|3[0-5][0-9]|[12][0-9][0-9]|[1-9]?[0-9])?$", command):

            message_parts = command.split(" ")
            direction = message_parts[1]

            self.oldStateTurtle.config(text=("Angle initial de la tortue : "+ str(self.turtle.angle)))

            self.turtle.fcap(-int(direction))

            self.newStateTurtle.config(text=("Nouvel angle de la tortue : " + str(self.turtle.angle)))

        elif re.match("^FPOS*", command):

            message_parts = command.split(" ")
            x = message_parts[1]
            y = message_parts[2]

            self.oldStateTurtle.config(text=("Position initiale de la tortue : " + self.turtle.getPos()))

            self.turtle.fpos(int(x), int(y))

            self.newStateTurtle.config(text=("Nouvelle position de la tortue : " + self.turtle.getPos()))

    def rgbToColor(self, rgb):
        return "#%02x%02x%02x" % rgb




