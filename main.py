import conteneur

#def first_fit_heuristic(gestionnaire):
    #for operation in gestionaire.operation:
        #conteneur_id = operation[0]
        #conteneur_operation = operation[1]
        #if conteneur_operation == "Ajout":
            #for i in range(len(gestionnaire.tab_pile)):
                #if (gestionnaire.tab_pile[i].empty()):
                    #gestionnaire.tab_pile[i].put(tab_conteneur[conteneur_id])
        #else:
            #while():

def main():
    print("c'est le main")
    gestionnaire = conteneur.GestionnaireConteneur(4,3,5)
    gestionnaire.addPile()
    gestionnaire.createConteneur(1,1,0)
    gestionnaire.tab_pile[0].put(gestionnaire.tab_conteneur[0])
    print(gestionnaire.estAccessible(0))
    
if __name__ == "__main__":
    main()   