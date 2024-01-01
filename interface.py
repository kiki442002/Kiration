import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Créer une fenêtre
fenetre = tk.Tk()

pointVitesse=[[0,1,2,3,4],[0,2,3,3,5]]
pointAngle=[[0,1,2,3,4],[0,2,3,3,5]]
pointPosition=[[0,1,2,3,4],[0,2,3,3,5]]

# Créer une figure et un axe avec matplotlib
fig = Figure(figsize=(5, 4), dpi=100)
ax=fig.add_subplot(111)
 # Créer un Canvas tkinter pour afficher la figure
canvas = FigureCanvasTkAgg(fig, master=fenetre)  # A tk.DrawingArea.
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def afficher_graphique(point, title,label):
    ax.clear()
    t = np.arange(0, len(point[0]), 1)*10
    ax.plot(t, point[0], label='Consigne')
    ax.plot(t, point[1], label='Mesure')
    ax.set_xlabel('Temps en ms')
    ax.set_ylabel(label)
    ax.set_title(title)
    ax.legend()
    canvas.draw()
   
# Définir le titre de la fenêtre
fenetre.title("Kiration")

# Mettre la fenêtre en plein écran
fenetre.attributes('-fullscreen', True)

# Créer une variable tkinter IntVar pour stocker la valeur sélectionnée
var = tk.IntVar()
var.set(1)

# Créer un titre
titre = tk.Label(fenetre, text="Graphique PID:")
titre.pack()

# Créer un Frame pour contenir les boutons radio avec un espacement
frame = tk.Frame(fenetre, padx=5, pady=5)
frame.pack()

# Créer trois boutons radio avec une taille de police plus grande
rb1 = tk.Radiobutton(frame, text="Vitesse", variable=var, value=1, command=lambda: afficher_graphique(pointVitesse, "PID Vitesse", "Vitesse en cm/s"), font=("Helvetica", 22))
rb2 = tk.Radiobutton(frame, text="Angle", variable=var, value=2, command=lambda: afficher_graphique(pointVitesse, "PID Angle", "Angle en degré"), font=("Helvetica", 22))
rb3 = tk.Radiobutton(frame, text="Position", variable=var, value=3, command=lambda: afficher_graphique(pointVitesse, "PID Position", "Postion en cm"), font=("Helvetica", 22))

# Ajouter les boutons radio à la fenêtre avec un espacement différent sur les côtés gauche et droit
rb1.grid(row=0, column=0, padx=(10, 20), pady=10)
rb2.grid(row=0, column=1, padx=(10, 20), pady=10)
rb3.grid(row=0, column=2, padx=(10, 20), pady=10)


# Lancer la boucle principale de la fenêtre
afficher_graphique(pointVitesse, "PID Vitesse", "Vitesse en cm/s")
fenetre.mainloop()


