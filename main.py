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

def most_Constrained_Value

def backTrack(list_Nodes,weight,list_dominios):
    if asignation_complete(list_Nodes): #todos los nodos estan asignados
        return list_Nodes
    node_to_assign_value=most_Constrained_Value(list_Nodes) #Escoger variable no asignada
    node_to_assign_value=pintar(node_to_assign_value,leastContrainedValue(node_to_assign_value,x))
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