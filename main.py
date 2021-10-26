import heapq
import copy
class Node:
    def __init__(self,list_dominios):
        self.dominio = list_dominios
        self.value=None
        self.conflict_List = []
        self.neighbours=[]
    def set_neighbours(self,node):
        self.neighbours.append(node)
    def __lt__(ob1, ob2):
        return len(ob1.dominio) < len(ob2.dominio)

class Speakers:
    def __init__(self,name,international,category,day,hour):
        self.name = name
        self.international=international
        self.quantity_conference=0
        self.category = category
        self.preference_day=day
        self.preference_hour=hour

        
def change_Dominio(node,value):
    node.dominio.append(value)
    return node

def forward_checking(node, value):
    node.dominio.append(value)
    for neighbour in node.neighbours:
        neighbour.dominio.remove(value)
    return node


def asignation_complete(list_Nodes,list_dominios):
    for speaker in list_dominios:
        if speaker.quantity_conference!=5:
            return False
    return True
   # for node in list_Nodes:
    #    if node.value==None:
     #       return False
    #return True

def most_Constrained_Value(list_Nodes):
    ordered_variables=[]
    for node in list_Nodes: #por cada variable sin asginaar
        if node.value==None:
            heapq.heappush(ordered_variables,node)    
    return heapq.heappop(ordered_variables)

#REVISAR
def least_Contrained_Value(node,list_Speakers):
    allconsistentvalues= []
    for value in node.dominio:
        temp_list_Nodes=copy.deepcopy(list_Speakers)
        forward_checking(node,value)
        consistent_values=0
        for neighbour in node.neighbours:
            consistent_values+=len(neighbour.dominio)   
        heapq.heappush(allconsistentvalues,(consistent_values,value))     
        list_Speakers=temp_list_Nodes
    return allconsistentvalues[0]

def verify_restrictions(node,value):
    print(0)
def update_list_Nodes(node, list_Nodes):
    print("")


def backTrack(list_Nodes,weight,list_dominios):
    if asignation_complete(list_Nodes,list_dominios): #todos los nodos estan asignados
        return list_Nodes
    node_to_assign_value=most_Constrained_Value(list_Nodes) #Escoger variable no asignada
    values=change_Dominio(node_to_assign_value,least_Contrained_Value(node_to_assign_value,node_to_assign_value.dominio)) #ordenar el dominio de la variable
    for v in values.dominio:
        if verify_restrictions(node_to_assign_value,v)==0 :# Es Invalido no cumple las resctricciones
            continue
    node_to_assign_value=forward_checking(node_to_assign_value,v)  #Actualizo su dominio
    list_Nodes=update_list_Nodes(node_to_assign_value,list_Nodes) #Actualizo la lista de nodos
    backTrack(list_Nodes,weight,list_dominios)  #llamda recursiva


def generate_list_Nodes(list_dominios):
    list_Nodes=[]
    for i in range (25):
        list_Nodes.append(Node(list_dominios))
    for j in range(5):
        for i in range(4):
            list_Nodes[i+j*5].set_neighbours(list_Nodes[(i+1)+j*5])
            list_Nodes[i+1 +j*5].set_neighbours(list_Nodes[i+ j*5])
    return list_Nodes

def generate_list_domains():
    list_speakers=[]
    n=input("Insert the quantity of speakers that will be\n")
    for i in range(n):
        name=input("Insert the name of speaker")
        inter=input("Insert if the speakers is International ( Y / N )")
        cat=input("Insert the category of the speaker")
        day=input("Insert the preference day of the speaker (0-Monday, 1-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday )")
        hour=input("Insert the preference hour of the speaker")
        list_speakers.append(Speakers(name,(inter=='Y'),cat,day,hour))

    #- Informatic Security
    #- Software Enginering
    #- Artificial intelligence
def dummy_speakers():
    list_speakers=[]
    list_speakers.append(Speakers("Jorge",True,"Informatic Security",3,10))
    list_speakers.append(Speakers("Ivan",False,"Software Enginering",2,15))
    list_speakers.append(Speakers("Jorge",True,"Informatic Security",0,17))
    return list_speakers
# Main Function
def main():    
   
    #list_dominios=generate_list_domains()
    list_dominios=dummy_speakers()
    list_Nodes=generate_list_Nodes(list_dominios)
    w=1
    backTrack(list_Nodes,w,list_dominios)
    


if __name__ == '__main__':
    main()

