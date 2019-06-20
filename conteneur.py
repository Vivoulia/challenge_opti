
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
        self.save_solution = []
        self.info_pile = [] # 0 si non croissant et 1 si croissant (initialisé à 1)
    
    def initPile(self):
        for i in range(self.L):
            Q = []
            for j in range(self.H):
                Q.append(-1)
            self.tab_pile.append(Q)
            self.info_pile.append(1) 
        
        for i in range(self.N):
            cont = self.tab_conteneur[i]
            if (cont.x != 0 and cont.y != 0):
                #Si x et y sont différents de 0 on peut ajouter le conteneur a une pile
                self.tab_pile[cont.x-1][cont.y-1] = cont.conteneur_id
                self.tab_conteneur[cont.conteneur_id].ajouter = True

        
    def addConteneurPile(cont, pile_id, conteneur_id):
        for j in range(self.H):
            if(self.tab_pile[pile_id][j] == -1):
                #Sommet de la pile
                if j != 0:
                    #Le sommet est a l'indice j-1
                    self.tab_pile[pile_id][j-1] = conteneur_id
                    self.tab_conteneur[conteneur_id].ajouter = True
                else:
                    #On ajoute le conteneneur a l'indice 0
                    self.tab_pile[pile_id][0] = conteneur_id
                    self.tab_conteneur[conteneur_id].ajouter = True
                
                    
    
    def createConteneur(self, x, y, conteneur_id):
        conteneur = Conteneur(x, y, conteneur_id)
        self.tab_conteneur.append(conteneur)
        
    def addOperation(self, operation):
        self.tab_operation.append(operation)
    
    def estAccessible(self, conteneur_id):
        accessible = False
        for i in range(self.L):
            for j in range(self.H-1, -1, -1):
                if(self.tab_pile[i][j] != -1 and self.tab_pile[i][j] != conteneur_id):
                    break
                elif(self.tab_pile[i][j] == conteneur_id):
                    return True
        return False
                
    
    def findPileConteneur(self, conteneur_id):
        for i in range(self.L):
            for j in range(self.H):
                if(self.tab_pile[i][j] == conteneur_id):
                    return i
        return -1
            
    def addLastNonFullPile(self, conteneur_id):
        pile_id = self.findPileConteneur(conteneur_id)
        for i in range(self.L):
            for j in range(self.H):
                if (self.tab_pile[i][j] == -1 and pile_id != i):
                    self.tab_pile[i][j] = conteneur_id
                    self.tab_pile[self.tab_conteneur[conteneur_id].x-1][self.tab_conteneur[conteneur_id].y-1] = -1
                    self.tab_conteneur[conteneur_id].x = i+1
                    self.tab_conteneur[conteneur_id].y = j+1
                    self.tab_conteneur[conteneur_id].ajouter = True
                    #deplacement de pile_id+1 a i+1
                    self.save_solution.append([pile_id+1, i+1])
                    return True
        return False
            
    def printTabConteneur(self):
        print("Affichage des conteneurs")
        for cont in self.tab_conteneur:
            print("id:", cont.conteneur_id, "| x:", cont.x, "| y:",  cont.y)
            
    def enleverConteneur(self, conteneur_id):
        for i in range(self.L):
            for j in range(self.H):
                if (self.tab_pile[i][j] == conteneur_id):
                    self.tab_pile[i][j] = -1
                    self.save_solution.append([i+1, 0])
                    return True
        return False
            
    def getSommetPile(self, pile_id):
        #Renvoie l'id du sommet au dessus de la pile pile_id
        for j in range(self.H):
            if(self.tab_pile[pile_id][j] == -1):
                #Sommet de la pile
                if j > 0:
                    return self.tab_pile[pile_id][j-1]
                else:
                    return self.tab_pile[pile_id][0]
            
        return self.tab_pile[pile_id][-1]
            
    def printAll(self):
        for h in range(self.H-1,-1,-1):
            for l in range(self.L):
                print(self.tab_pile[l][h], "    ", end = '')
            print('')
    
    def croiss_ncroiss(self):
        #Rempli le tableau d'info pile (1 croissant / 0 non croissant)
        for i_pile in range(self.L):
            croissante = 1
            for i_conteneur in range(1, self.H):
                if (self.tab_pile[i_pile][i_conteneur] != -1):
                    if not(self.tab_pile[i_pile][i_conteneur] < self.tab_pile[i_pile][i_conteneur-1]):
                        croissante = 0
                        break
                else:
                    if (i_conteneur == 1):
                        croissante = 0
                        break
            self.info_pile[i_pile] = croissante
            
    def findPremPilevide(self):
        #renvoie 1er pile vide
        for l in range(self.L):
            if(self.tab_pile[l][0] == -1):
                return l
        return -1
    

    def pireCas(self, conteneur_id):
        maximum = 0
        colonne_destination = -1
        print(self.info_pile)
        for l in range(self.L):
            if (l != self.tab_conteneur[conteneur_id].x-1):
                print(self.tab_conteneur[conteneur_id].x-1, l)
                if(self.info_pile[l] == 0): #parcours des piles non croissantes
                    for h in range(self.H-1):
                        print("maximum", maximum ," compare", self.tab_pile[l][h] )
                        if(self.tab_pile[l][h] > maximum and self.tab_pile[l][-1] == -1):
                            colonne_destination = l
                            maximum = self.tab_pile[l][h]
        return colonne_destination

    def findMinSommetCroissant(self, conteneur_bloquant_id):
        #Renvoie les coordonnées de la case au dessus du minimum des sommets des piles croissantes (renvoie [-1, -1] en cas de non existence
        mini = 0
        pile_id = -1
        for i_pile in range(self.L):
            if(self.info_pile[i_pile] == 1):
                conteneur_id = self.getSommetPile(i_pile)
                if(conteneur_bloquant_id < conteneur_id and conteneur_id > mini):
                    #C'est un minimum
                    if(self.tab_conteneur[conteneur_id].y < self.H-1):
                        #Si le sommet de la pile est 
                        mini = conteneur_id
                        #On renvoie la case libre
                        pile_id = self.tab_conteneur[conteneur_id].x-1
        return pile_id
    
    def findMax(self, conteneur_id):
        maximum = 0
        pile_id = -1
        for l in range(self.L):
            if(self.tab_conteneur[conteneur_id].x-1 != l and self.tab_pile[l][-1] == -1):
                sommet_id = self.getSommetPile(pile_id)
                if sommet_id > maximum:
                    maximum = sommet_id
                    pile_id = l
        return pile_id
    
    def findMinSommetNonCroissant(self, conteneur_bloquant_id):
        #Renvoie les coordonnées de la case au dessus du minimum des sommets des piles croissantes (renvoie [-1, -1] en cas de non existence
        maxi = 0
        pile_id = -1
        for i_pile in range(self.L):
            if(self.info_pile[i_pile] == 0):
                conteneur_id = self.getSommetPile(i_pile)
                print("Sommet non croissant", conteneur_id)
                if(conteneur_bloquant_id < conteneur_id and conteneur_id > maxi):
                    #C'est un minimum
                    if(self.tab_conteneur[conteneur_id].y < self.H):
                        #Si le sommet de la pile est 
                        maxi = conteneur_id
                        #On renvoie la case libre
                        pile_id = self.tab_conteneur[conteneur_id].x-1
        return pile_id  
    
    def putConteneurIntoPile(self, pile_id, conteneur_id):
         #Ajoute un conteneur dans une pile 
        for j in range(self.H):
            if(self.tab_pile[pile_id][j] == -1):
                self.tab_pile[pile_id][j] = conteneur_id
                if (self.tab_conteneur[conteneur_id].x != 0 and self.tab_conteneur[conteneur_id].y != 0):
                    #Si le conteneur était deja placé on met a jour son ancienne position
                    self.tab_pile[self.tab_conteneur[conteneur_id].x-1][self.tab_conteneur[conteneur_id].y-1] = -1
                #On met a jour la position du conteneur
                self.save_solution.append([self.tab_conteneur[conteneur_id].x, pile_id+1])
                self.tab_conteneur[conteneur_id].x = pile_id+1
                self.tab_conteneur[conteneur_id].y = j+1
                return True #L'insertion a bien fonctionné
        return False #L'insertion est un echec
    
        
                    
        
    
        
    
        
            
        
        
            
    