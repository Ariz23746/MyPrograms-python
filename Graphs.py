# Creating adjacentList:

class Graphs:
    def __init__(self):
        self.numberofNodes = 0
        self.adjacentList = {}
#----------------------------------------------------------------------------------#
# Creating a Add vertex Function:-
    def AddVertex(self,value):
        self.adjacentList[value] = []
        self.numberofNodes = self.numberofNodes + 1
#----------------------------------------------------------------------------------#
# creating a Add Edge Function i.e. Connection between two Vertex:-

    def AddEdge(self,value1,value2):
            self.adjacentList[value1].append(value2)
            self.adjacentList[value2].append(value1)

#----------------------------------------------------------------------------------#
# Creating a View Function:-
       
    def showconnections(self):

        for key,value in self.adjacentList.items():
            i=0
            print(key,"-->",end=" ")
            while i < len(value):
                print(value[i],end=" ")
                i+=1
            print("\t")    
#----------------------------------------------------------------------------------#


Element = Graphs()
Element.AddVertex(0)
Element.AddVertex(1)
Element.AddVertex(2)
Element.AddVertex(3)
Element.AddEdge(0,1)
Element.AddEdge(0,2)
Element.AddEdge(0,3)
Element.AddEdge(2,3)
Element.showconnections()



