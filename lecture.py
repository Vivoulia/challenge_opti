import csv
import os
import conteneur

dirname = os.path.dirname(__file__)
print(__file__)
filename = os.path.join(dirname, 'instancesChallengeCRP')

def lecture_donnee(numero):
    #lecture de global
    
    with open(filename + "\\" + str(numero) +"_global.csv", newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            gestionnaire = conteneur.GestionnaireConteneur(row[0], row[1], row[2])
    csv_file.close()
    
    
    
    #lecture de position
    with open(filename + "\\" + str(numero) +"_position.csv", newline='') as csv_file:
        conteneur_id = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)
            print(row[1])
            gestionnaire.createConteneur(row[1], row[2], conteneur_id)
            conteneur_id = conteneur_id + 1          
    csv_file.close()
    
    #lecture
    with open(filename + "\\" + str(numero) +"_operations.csv", newline='') as csv_file:
        conteneur_id = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
       
                  
    csv_file.close()    

        
        
    