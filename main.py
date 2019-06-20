import conteneur
import lecture


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
     

    gestionnaire = lecture.lecture_donnee(1)
    gestionnaire.initPile()
    gestionnaire.printAll()
    
if __name__ == "__main__":
    main()   