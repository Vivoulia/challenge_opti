
import queue

class Conteneur:
    def __init__(self, x, y, conteneur_id):
        self.x = x
        self.y = y
        self.conteneur_id = conteneur_id
        self.ajouter = False
        
class GestionnaireConteneur:
    def __init__(self, N, L, H):
        self.N = N
        self.H = H
        self.L = L
        self.tab_pile = []
        self.tab_conteneur = []
        self.tab_operation = []
    
    def addPile(self):
        Q = queue.LifoQueue()
        self.tab_pile.append(Q)
        
    def addConteneurPile(cont, id_pile):
        #Ajoute un conteneur dans la pile d'id id_pile
        pass
    
    def createConteneur(self, x, y, conteneur_id):
        conteneur = Conteneur(x, y, conteneur_id)
        self.tab_conteneur.append(conteneur)
        
    def addOperation(self, operation):
        self.tab_operation.append(operation)
    
    def estAccessible(self, conteneur_id):
        for i in range(len(self.tab_pile)):
            if self.tab_pile[i].empty() == False:
                contenenur_sommet = self.tab_pile[i].get_nowait()
                if (contenenur_sommet.conteneur_id == conteneur_id):
                    return True
        return False
            
            
    