
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
        self.pile_possible = L
    
    def initPile(self):
        for i in range(self.L):
            Q = []
            for j in range(self.H):
                Q.append(-1)
            self.tab_pile.append(Q)
        
        for i in range(self.N):
            cont = self.tab_conteneur[i]
            self.tab_pile[cont.x-1][cont.y-1] = cont.conteneur_id
        
    def addConteneurPile(cont, id_pile):
        #Ajoute un conteneur dans la pile d'id id_pile
        pass
    
    def createConteneur(self, x, y, conteneur_id):
        conteneur = Conteneur(x, y, conteneur_id)
        self.tab_conteneur.append(conteneur)
        
    def addOperation(self, operation):
        self.tab_operation.append(operation)
    
    def estAccessible(self, conteneur_id):
        for i in range(self.L):
            for j in range(self.H):
                if(self.tab_pile[i][j] == -1):
                    #Sommet de la pile
                    if j != 0:
                        #Le sommet est a l'indice j-1
                        if self.tab_pile[i][j-1] == conteneur_id:
                            return True
        return False
            
    def printTabConteneur(self):
        print("Affichage des conteneurs")
        for cont in self.tab_conteneur:
            print("id:", cont.conteneur_id, "| x:", cont.x, "| y:",  cont.y)
            
    def printAll(self):
        pass
        
            
    