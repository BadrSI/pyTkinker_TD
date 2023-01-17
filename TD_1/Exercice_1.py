from tkinter import * 

fen = Tk()  # On crée la fenêtre principale (vous la verrez apparaître !). Pour cela, on crée une instance de la classe Tk dans la variable fen.

# L'instruction fen.mainloop() va lancer le gestionnaire d'événements que nous avons évoqué ci-dessus. 
# C'est lui qui interceptera la moindre action de l'utilisateur, et qui lancera les portions de code associées à 
# chacune de ses actions. Bien sûr, comme nous développerons dans ce qui va suivre toutes nos applications Tkinter 
# dans des scripts (et non pas dans l'interpréteur), cette ligne sera systématiquement présente. Elle sera souvent 
# à la fin du script, puisque, à l'image de ce script, on écrit d'abord le code construisant l'interface, et on 
# lance le gestionnaire d'événements une fois l'interface complètement décrite, ce qui lancera au final l'application.
fen.mainloop() 