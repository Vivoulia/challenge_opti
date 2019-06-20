import conteneur
import lecture


def first_fit_heuristic(gestionnaire):
    for operation in gestionaire.operation:
        conteneur_id = operation[0]
        conteneur_operation = operation[1]
        if conteneur_operation == "A":
            addLastNonFullPile(conteneur_id)
        else:
            while(estAccessible(conteneur_id) == False):
                for i in range(self.L):
                    for j in range(self.H):
                        if(self.tab_pile[i][j] == conteneur_id):
                            conteneur_bloquant = j-1
                            addLastNonFullPile(conteneur_bloquant)
            

def main():
    print("c'est le main")
<<<<<<< Updated upstream
     

    gestionnaire = lecture.lecture_donnee(1)
    gestionnaire.initPile()
    gestionnaire.printAll()
=======

>>>>>>> Stashed changes
    
if __name__ == "__main__":
    main()   