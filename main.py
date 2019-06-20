import conteneur
import lecture


def first_fit_heuristic(gestionnaire):
    deplacement = 0
    estDeplace = False
    for operation in gestionnaire.tab_operation:
        conteneur_id = operation[0]
        conteneur_operation = operation[1]
        print(conteneur_operation)
        if conteneur_operation == " A":
            gestionnaire.addLastNonFullPile(conteneur_id)
        else:
            while(gestionnaire.estAccessible(conteneur_id) == False):
                print("Bloque", conteneur_id)
                for i in range(gestionnaire.L):
                    for j in range(gestionnaire.H):
                        if(gestionnaire.tab_pile[i][j] == conteneur_id):
                            conteneur_bloquant = gestionnaire.getSommetPile(i)                           
                            estDeplace = gestionnaire.addLastNonFullPile(conteneur_bloquant)
                            if(estDeplace):
                                print("Bloquant", conteneur_bloquant)
                                gestionnaire.printAll()
                                deplacement = deplacement + 1
                                estDaplace = False
            gestionnaire.enleverConteneur(conteneur_id)
    print("deplacement ", deplacement)

            

def main():
    print("c'est le main")
    gestionnaire = lecture.lecture_donnee(20)
    gestionnaire.initPile()
    gestionnaire.printAll()
<<<<<<< Updated upstream
    first_fit_heuristic(gestionnaire)
    print(gestionnaire.save_solution)
    lecture.save_solution_file(20, gestionnaire.save_solution)
=======
    gestionnaire.croiss_ncroiss()
    
>>>>>>> Stashed changes
if __name__ == "__main__":
    main()   