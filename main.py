import conteneur
import lecture
import random


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
            #Sommet min pile croissante
            pile_sommet_min = gestionnaire.findMinSommetCroissant(conteneur_id)
            if(pile_sommet_min != -1):
                print("Sommet croissant min")
                gestionnaire.putConteneurIntoPile(pile_sommet_min, conteneur_id)            
            else:
                #On essait pile vide
                premiere_pile_vide = gestionnaire.findPremPilevide()
                if(premiere_pile_vide != -1):
                    print("Pile vide")
                    gestionnaire.putConteneurIntoPile(premiere_pile_vide, conteneur_id)                
                
                else:
                    #Sommet min pile non croissante
                    pile_sommet_min = gestionnaire.findMinSommetNonCroissant(conteneur_id)
                    if(pile_sommet_min != -1):
                        print("Sommet non croissant min")
                        gestionnaire.putConteneurIntoPile(pile_sommet_min, conteneur_id) 
                    else:
                        trouve = False
                        for i in range(gestionnaire.L):
                            hauteur_sommet = gestionnaire.getHauteurSommetPile(i)
                            sommet = gestionnaire.getSommetPile(i)
                            print("hauteur", hauteur_sommet, "sommet", sommet)
                            for j in range(gestionnaire.H):
                                if (gestionnaire.tab_pile[i][j] == conteneur_id+1 or gestionnaire.tab_pile[i][j] == conteneur_id-1):
                                    distance = abs(hauteur_sommet - j)
                                    pile_sommet_min = gestionnaire.findMinSommetCroissant(sommet)
                                    if (pile_sommet_min != -1):
                                        gestionnaire.putConteneurIntoPile(premiere_pile_vide, sommet)
                                        trouve = True
                                        gestionnaire.putConteneurIntoPile(i, conteneur_id)
                        if (trouve == False):
                            pile_id = 0
                            while (gestionnaire.putConteneurIntoPile(pile_id, conteneur_id) == False):
                                pile_id = pile_id + 1
                            
        else:
            while(gestionnaire.estAccessible(conteneur_id) == False):
                #On prends le bloquant
                for i in range(gestionnaire.L):
                    for j in range(gestionnaire.H):
                        if(gestionnaire.tab_pile[i][j] == conteneur_id):
                            conteneur_bloquant = gestionnaire.getSommetPile(i)
                            print("Bloque", conteneur_id)
                            print("Bloquant", conteneur_bloquant)
                            #Sommet min pile croissante
                            pile_sommet_min = gestionnaire.findMinSommetCroissant(conteneur_bloquant)
                            if(pile_sommet_min != -1):
                                print("Sommet croissant min")
                                gestionnaire.putConteneurIntoPile(pile_sommet_min, conteneur_bloquant)                            
                            
                            else:
                                #On essait pile vide
                                premiere_pile_vide = gestionnaire.findPremPilevide()
                                if(premiere_pile_vide != -1):
                                    print("Pile vide")
                                    gestionnaire.putConteneurIntoPile(premiere_pile_vide, conteneur_bloquant)                                
                                
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
                                            pile_encore_pire = gestionnaire.findMax(conteneur_bloquant)
                                            if (pile_encore_pire != -1):
                                                gestionnaire.putConteneurIntoPile(pile_encore_pire, conteneur_bloquant)
                                            else:
                                                print("Oulalala erreur grave ya encore un cas non gere")
                            gestionnaire.printAll()
            gestionnaire.enleverConteneur(conteneur_id)

def main():

    #for numero in range(1, 21):
        #print("#NUMERO", numero)
        #gestionnaire = lecture.lecture_donnee(numero)
        #gestionnaire.initPile()
        #gestionnaire.printAll()
        #lucas_heuristic(gestionnaire)
        #print(gestionnaire.save_solution)
        #lecture.save_solution_file(numero, gestionnaire.save_solution)
    numero = 8
    print("#NUMERO", numero)
    gestionnaire = lecture.lecture_donnee(numero)
    gestionnaire.initPile()
    gestionnaire.printAll()
    lucas_heuristic(gestionnaire)
    print(gestionnaire.save_solution)
    lecture.save_solution_file(numero, gestionnaire.save_solution)    

if __name__ == "__main__":
    main()   