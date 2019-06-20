
import queue

class Conteneur:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        
class GestionnaireConteneur:
    def __init__(self, N, L, H):
        self.N = N
        self.H = H
        self.L = L
        self.tab_pile = []
    
    def addPile(self):
        Q = queue.LifoQueue()
        self.tab_pile.append(Q)
    
def main():
    print("c'est le main")
    conteneur = Conteneur(10,5,1)
    gestion = GestionnaireConteneur(10,5,5)
    gestion.addPile()
    gestion.tab_pile[0].put(conteneur)
    print(gestion.tab_pile[0].get().name)
    
if __name__ == "__main__":
    main()   