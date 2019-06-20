
import queue

class Conteneur:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.ajouter = False
        
class GestionnaireConteneur:
    def __init__(self, N, L, H):
        self.N = N
        self.H = H
        self.L = L
        self.tab_pile = []
        self.tab_conteneur = []
    
    def addPile(self):
        Q = queue.LifoQueue()
        self.tab_pile.append(Q)
    
    def createConteneur(self, x, y, name):
        conteneur = Conteneur(x, y, name)
        tab_conteneur.append(conteneur)