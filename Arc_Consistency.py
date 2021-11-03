import heapq
import copy
import random
class Node:
    def __init__(self,list_dominios,day,hour,cat):
        self.dominio = list_dominios
        self.value=None
        self.conflict_List = []
        self.neighbours=[]
        self.day=day
        self.hour=hour
        self.category=cat
    def set_neighbours(self,node):
        self.neighbours.append(node)
    def __lt__(ob1, ob2):
        return len(ob1.dominio) < len(ob2.dominio)

class Speakers:
    def __init__(self,name,international,category,quantity_conference,day,hour):
        self.name = name
        self.international=international
        self.quantity_conference=quantity_conference
        self.category = category
        self.preference_day=day
        self.preference_hour=hour

class Speaker:
    def __init__(self,name,international,category,day,hour):
        self.name = name
        self.international=international
        self.category = category
        self.day=day
        self.hour=hour
    def __lt__(ob1, ob2):
            return False
        
def change_Dominio(node,value):
    node.dominio=value
    return node


def compare_2_speakers(speaker,value):
    return speaker.name==value.name and speaker.international==value.international and  speaker.category==value.category and  speaker.day== value.day and speaker.hour== value.hour  

def forward_checking(node, value,list_dominios):
    node.value=value
    nodes_to_delete=[]
    new_Dominio=copy.deepcopy(node.dominio)
    for speaker in new_Dominio:
        if not compare_2_speakers(speaker,value):
            nodes_to_delete.append(speaker)
    
    for i in range(len(nodes_to_delete)):
        new_Dominio.remove(nodes_to_delete[i])
    node.dominio=new_Dominio
    for neighbour in node.neighbours:            
        for speak in neighbour.dominio:
            if compare_2_speakers(value,speak):
                neighbour.dominio.remove(speak)
                break    
    for speak in list_dominios:
        if compare_2_speakers(speak,value):
            list_dominios.remove(speak)
    return node


def domain_touched(xi,xj):
    touched=False
    for value in xj.neighbours:
        if 

def arc_consistency(node,value):
    queue=[]

    nodes_to_delete=[]
    new_Dominio=copy.deepcopy(node.dominio)
    for speaker in new_Dominio:
        if not compare_2_speakers(speaker,value):
            nodes_to_delete.append(speaker)
    
    for i in range(len(nodes_to_delete)):
        new_Dominio.remove(nodes_to_delete[i])
    node.dominio=new_Dominio

    for neigh in node.neighbours:
        if neigh.value!=None:
            queue.append((node,neigh))
    while len(queue)!=0:
        (xi,xj)=queue.pop(0)
        if domain_touched(xi,xj):
            if len(xj.dominio)==0:
                return False
            for neigh in xj.neighbours:
                if neigh.value!=None:
                    queue.append(xj,neigh)
    return True
def asignation_complete(list_Nodes,list_dominios):
    
    if len(list_dominios)==0:
        return True
    for node in list_Nodes:
       if node.value==None:
           return False
        
    
def count_speaker_in_day_hour(node):
    sum=0
    for speaker in node.dominio:
        if speaker.hour==node.hour and speaker.day==node.day:
            sum=sum+1
    return sum

def most_Constrained_Value(list_Nodes):
    ordered_variables=[]
    for node in list_Nodes: #por cada variable sin asgzinaar
        if node.value==None:
           ordered_variables.append((count_speaker_in_day_hour(node),node))
    ordered_variables.sort(reverse=True)
    return (ordered_variables.pop(0))[1]

#REVISAR
def least_Contrained_Value(node):
    allconsistentvalues= []
    for value in node.dominio: #para cada speaker
        temp_Node=copy.deepcopy(node)
        forward_checking(temp_Node,value,copy.deepcopy(temp_Node.dominio))
        consistent_values=0
        for neighbour in temp_Node.neighbours:
            consistent_values+=len(neighbour.dominio)   
        heapq.heappush(allconsistentvalues,(consistent_values,value))     
    newall=[]
    for el in allconsistentvalues:
        newall.append(el[1])
    return newall

def verify_restrictions(node,value):   
    if node.category!=value.category: #Un speaker solo puede dar charlas de su categoria
        return 0
    if node.day!= value.day: #Un speaker solo puede dar su charla el dia de su preferencia
        return 0
    if node.hour!= value.hour: #Un speaker solo puede dar su charla a la hora de su preferencia
        return 0
    for neighbour in node.neighbours:
        if neighbour.value!=None:
            if value == neighbour.value: #Un spekaer no puede tener 2 charlas seguidas o en el mismo horario
                return 0
            if neighbour.hour==value.hour:
                if neighbour.international==value.international: # 2 speakers internacionales no pueden dar en el mismo horario
                    return 0
    return 1  

def update_list_Nodes(node, list_Nodes):
    print("")


def backTrack(list_Nodes,weight,list_dominios):
    if asignation_complete(list_Nodes,list_dominios): #todos los nodos estan asignados
        return list_Nodes
    node_to_assign_value=most_Constrained_Value(list_Nodes) #Escoger variable no asignada
    node_to_assign_value=change_Dominio(node_to_assign_value,least_Contrained_Value(node_to_assign_value)) #ordenar el dominio de la variable
    for v in node_to_assign_value.dominio:
        if verify_restrictions(node_to_assign_value,v)==0 :# Es Invalido no cumple las resctricciones
            continue
        node_to_assign_value=forward_checking(node_to_assign_value,v,list_dominios)  #Actualizo su dominio
        #list_Nodes=update_list_Nodes(node_to_assign_value,list_Nodes) #Actualizo la lista de nodos
        backTrack(list_Nodes,weight,list_dominios)  #llamda recursiva`


def generate_list_Nodes(list_dominios):
    list_Nodes=[]
    for i in range (18*5):
        day=int(i/18)
        hour=int((i%18)/3)
        hour= hour+9 if hour<3 else hour+12
        if (i%18)%3==0:
            cat="Informatic Security"
        elif (i%18)%3==1:
            cat="Software Enginering"
        elif (i%18)%3==2:
            cat="Artificial Intelligence"
        list_Nodes.append(Node(list_dominios,day,hour,cat))
    for j in range(5):
        for i in range(5):
            #mismo horario
            list_Nodes[(i*3)+18*j].set_neighbours(list_Nodes[(i*3+1)+18*j])
            list_Nodes[(i*3+1)+18*j].set_neighbours(list_Nodes[(i*3+2)+18*j])
            list_Nodes[(i*3+2)+18*j].set_neighbours(list_Nodes[(i*3)+18*j])
            list_Nodes[(i*3+1)+18*j].set_neighbours(list_Nodes[(i*3)+18*j])
            list_Nodes[(i*3+2)+18*j].set_neighbours(list_Nodes[(i*3+1)+18*j])
            list_Nodes[(i*3)+18*j].set_neighbours(list_Nodes[(i*3+2)+18*j])
            #entre horarios 
            list_Nodes[(i*3)+18*j].set_neighbours(list_Nodes[(i*3+3)+18*j])
            list_Nodes[(i*3+1)+18*j].set_neighbours(list_Nodes[(i*3+4)+18*j])
            list_Nodes[(i*3+2)+18*j].set_neighbours(list_Nodes[(i*3+5)+18*j])
            list_Nodes[(i*3+3)+18*j].set_neighbours(list_Nodes[(i*3)+18*j])
            list_Nodes[(i*3+4)+18*j].set_neighbours(list_Nodes[(i*3+1)+18*j])
            list_Nodes[(i*3+5)+18*j].set_neighbours(list_Nodes[(i*3+2)+18*j])
    return list_Nodes

def generate_list_domains():
    list_speakers=[]
    n=input("Insert the quantity of speakers that will be\n")
    for i in range(n):
        name=input("Insert the name of speaker")
        inter=input("Insert if the speakers is International ( Y / N )")
        cat=input("Insert the category of the speaker")
        day=input("Insert the preference day of the speaker (0-Monday, 1-Tuesday, 2-Wednesday, 3-Thursday, 4-Friday )")
        hour=input("Insert the preference hour of the speaker")
        list_speakers.append(Speaker(name,(inter=='Y'),cat,day,hour))

    #- Informatic Security
    #- Software Enginering
    #- Artificial intelligence
def dummy_speakers():
    list_speakers=[]
    #NOMBRE,ES INTERNACIONAL, CATEGORIA, CANTIDAD_CHARLAS, HORAS DE PREFERENCIA( X CHARLA), DIAS DE PREFERENCIA (X CHARLA)
    list_speakers.append(Speakers("Jorge",True,"Informatic Security",2,[1,2],[8,10]))
    list_speakers.append(Speakers("Ivan",False,"Software Enginering",3,[2,0,8],[15,17,9]))
    list_speakers.append(Speakers("Jorges Cre",True,"Informatic Security",1,[1],[8]))
    list_speakers.append(Speakers("Jorges Cre",True,"Informatic Security",1,[0],[9]))
    return list_speakers

def redifined_domain(list_speakers):
    domain=[]
    for speaker in list_speakers:
        for i in range(speaker.quantity_conference):
            domain.append(Speaker(speaker.name,speaker.international,speaker.category,speaker.preference_day[i],speaker.preference_hour[i]))
    return domain
# Main Function
def main():    
   
    #list_dominios=generate_list_domains()
    list_dominios=dummy_speakers()
    list_dominios=redifined_domain(list_dominios)
    list_Nodes=generate_list_Nodes(list_dominios)
    w=1
    backTrack(list_Nodes,w,list_dominios)
    


if __name__ == '__main__':
    main()

