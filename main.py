import heapq
import copy
class Node:
    def __init__(self):
        self.dominio = []
        self.value=None
        self.conflict_List = []
        


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

def least_Contrained_Value(node,list_Nodes):
    allconsistentvalues= []
    for value in node.dominio:
        temp_x=copy(x)
        forward_checking(Xi,v)
        consistent_values=0
        foreach Xe in Xi.neighbours{
            consisten_values+=len(Xe.dominio)
        }
        allconsistentvalues.push(v,consistentvalues)
        x=temp_x
    }
    return allconsistentValues.pop

def backTrack(list_Nodes,weight,list_dominios):
    if asignation_complete(list_Nodes): #todos los nodos estan asignados
        return list_Nodes
    node_to_assign_value=most_Constrained_Value(list_Nodes) #Escoger variable no asignada
    node_to_assign_value=change_Dominio(node_to_assign_value,least_Contrained_Value(node_to_assign_value,x))
    foreach v in dominios
    if(asginacion_es_correcta(node_to_assign_value,v)==0)//Invalido
        continue
    node_to_assign_value=arcConsitency_Back_jump(node_to_assign_value,v)
    jump(xe.conflict.pop())
    list_Nodes.upgrade(node_to_assign_value)
    Backtrack(x,1,dominios)





list_Nodes=[]
w=1
list_dominios=[]