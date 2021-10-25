import heapq
import copy
class Node:
    def __init__(self):
        self.dominio = []
        self.value=None
        self.conflict_List = []
        self.neighbours=[]
        
def change_Dominio(node,value):
    node.dominio.append(value)
    return node

def forward_checking(node, value):
    node.dominio.append(value)
    for neighbour in node.neighbours:
        neighbour.dominio.remove(value)
    return node


def asignation_complete(list_Nodes):
    for node in list_Nodes:
        if node.value==None:
            return False
    return True

def most_Constrained_Value(list_Nodes):
    ordered_variables=[]
    for node in list_Nodes: #por cada variable sin asginaar
        heapq.heappush(ordered_variables,(len(node.dominio),node))    
    return heapq.heappop(ordered_variables)[1]

#REVISAR
def least_Contrained_Value(node,list_Nodes):
    allconsistentvalues= []
    for value in node.dominio:
        temp_list_Nodes=copy.deepcopy(list_Nodes)
        forward_checking(node,value)
        consistent_values=0
        for neighbour in node.neighbours:
            consistent_values+=len(neighbour.dominio)   
        heapq.heappush(allconsistentvalues,(consistent_values,value))     
        list_Nodes=temp_list_Nodes
    return allconsistentvalues[0]

def verify_restrictions(node,value):
    print(0)
def update_list_Nodes(node, list_Nodes):
    print("")


def backTrack(list_Nodes,weight,list_dominios):
    if asignation_complete(list_Nodes): #todos los nodos estan asignados
        return list_Nodes
    node_to_assign_value=most_Constrained_Value(list_Nodes) #Escoger variable no asignada
    values=change_Dominio(node_to_assign_value,least_Contrained_Value(node_to_assign_value,node_to_assign_value.dominio)) #ordenar el dominio de la variable
    for v in values.dominio:
        if verify_restrictions(node_to_assign_value,v)==0 :# Es Invalido no cumple las resctricciones
            continue
    node_to_assign_value=forward_checking(node_to_assign_value,v)  #Actualizo su dominio
    list_Nodes=update_list_Nodes(node_to_assign_value,list_Nodes) #Actualizo la lista de nodos
    backTrack(list_Nodes,weight,list_dominios)  #llamda recursiva




list_Nodes=[]
w=1
list_dominios=[]