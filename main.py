import conteneur
import lecture


def first_fit_heuristic(gestionnaire):
    deplacement = 0
    estDeplace = False
    for operation in gestionnaire.tab_operation:
        conteneur_id = operation[0]
        conteneur_operation = operation[1]
        print(conteneur_operation, conteneur_id)
        gestionnaire.printAll()
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
                                deplacement = deplacement + 1
                                estDaplace = False
            gestionnaire.enleverConteneur(conteneur_id)
    print("deplacement ", deplacement)

 
def lucas_heuristic(gestionnaire):
    for operation in gestionnaire.tab_operation:
        gestionnaire.croiss_ncroiss()
        print(gestionnaire.info_pile)
        conteneur_id = operation[0]
        conteneur_operation = operation[1]
        print(conteneur_operation, conteneur_id)
        gestionnaire.printAll()
        if conteneur_operation == " A":
            gestionnaire.addLastNonFullPile(conteneur_id)
        else:
            while(gestionnaire.estAccessible(conteneur_id) == False):
                #On prends le bloquant
                for i in range(gestionnaire.L):
                    for j in range(gestionnaire.H):
                        if(gestionnaire.tab_pile[i][j] == conteneur_id):
                            conteneur_bloquant = gestionnaire.getSommetPile(i)
                            print("Bloque", conteneur_id)
                            print("Bloquant", conteneur_bloquant)
                            #On essait pile vide
                            premiere_pile_vide = gestionnaire.findPremPilevide()
                            if(premiere_pile_vide != -1):
                                print("Pile vide")
                                gestionnaire.putConteneurIntoPile(premiere_pile_vide, conteneur_bloquant)
                            else:
                                #Sommet min pile croissante
                                pile_sommet_min = gestionnaire.findMinSommetCroissant(conteneur_bloquant)
                                if(pile_sommet_min != -1):
                                    print("Sommet croissant min")
                                    gestionnaire.putConteneurIntoPile(pile_sommet_min, conteneur_bloquant)
                                else:
                                    #Sommet min pile non croissante
                                    pile_sommet_min = gestionnaire.findMinSommetNonCroissant(conteneur_bloquant)
                                    if(pile_sommet_min != -1):
                                        print("Sommet non croissant min")
                                        gestionnaire.putConteneurIntoPile(pile_sommet_min, conteneur_bloquant) 
                                    else:
                                        pile_pire = gestionnaire.pireCas(conteneur_bloquant)
                                        #Pire cas
                                        if(pile_pire != -1):
                                            print("Pire cas")
                                            gestionnaire.putConteneurIntoPile(pile_pire, conteneur_bloquant) 
                                        else:
                                            print("Oulala grosse erreur")
                            gestionnaire.printAll()
            gestionnaire.enleverConteneur(conteneur_id)

def main():
    numero = 13
    print("c'est le main")
    gestionnaire = lecture.lecture_donnee(numero)
    gestionnaire.initPile()
    gestionnaire.printAll()
    lucas_heuristic(gestionnaire)
    print(gestionnaire.save_solution)
    lecture.save_solution_file(numero, gestionnaire.save_solution)
    gestionnaire.croiss_ncroiss()

if __name__ == "__main__":
    main()   