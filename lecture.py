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
        ligne = 0
        for row in csv_reader:
            if(ligne>0):
                gestionnaire = conteneur.GestionnaireConteneur(int(row[0]), int(row[1]), int(row[2]))
                print(int(row[0]), int(row[1]), int(row[2]))
            ligne = ligne + 1
    csv_file.close()
    
    
    
    #lecture de position
    with open(filename + "\\" + str(numero) +"_position.csv", newline='') as csv_file:
        conteneur_id = 0
        csv_reader = csv.reader(csv_file, delimiter=',')
        ligne = 0
        for row in csv_reader:
            if(ligne>0):
                print(row)
                gestionnaire.createConteneur(int(row[1]), int(row[2]), int(conteneur_id))
                conteneur_id = conteneur_id + 1   
            ligne = ligne + 1
    csv_file.close()
    
    #lecture
    with open(filename + "\\" + str(numero) +"_operations.csv", newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        ligne = 0
        conteneur_id = 0
        for row in csv_reader:
            if(ligne>0):
                op = row[0][2:]
                print(op)
                gestionnaire.addOperation([int(op) - 1, row[1]])
                conteneur_id = conteneur_id + 1
            ligne = ligne + 1
    csv_file.close()  

    return gestionnaire
            
def save_solution_file(numero, tab_solution):
    filename_save = os.path.join(dirname, 'solution')
        
    with open(filename + "\\" + str(numero) +"_solution.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(["FROM ", " TO"])
        for solution in tab_solution:
            writer.writerow([str(solution[0])+" ", " " + str(solution[1])])
        
    csv_file.close()    

        
        
    