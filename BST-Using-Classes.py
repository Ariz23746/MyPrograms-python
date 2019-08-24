# Creating a Node :-

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
#---------------------------------------------------------------------------------#
# Creating a BST :-

class BST:

# creating a constructor :-
    def __init__(self):
        self.root = None
#--------------------------------------------------------------------------------#
# Creating an Insert Function :-

    def insert(self,value):
        NewElement = Node(value)

        if self.root == None:
            self.root = NewElement

        else:
            temp = self.root    
            while True:
                if self.root.data < value:
                    if temp.right == None:
                        temp.right = NewElement
                        break
                    temp = temp.right    
                
                else:
                    if temp.left == None:
                        temp.left = NewElement
                        break
                    temp = temp.left   
                        
       
        
#--------------------------------------------------------------------------------#
# creating a lookup function :-
    def view(self):
        temp = self.root
        print("\t",self.root.data)
        temp1 = temp.left
        temp2 = temp.right
        while temp1 != None:
            if temp1 != None and temp2 != None:
                print("      ",temp1.data,end="  ")
                print(temp2.data)
                if temp1.left != None and temp1.right != None:
                    print("   ",temp1.left.data,end=" ")
                    print(temp1.right.data)
                    temp1 = temp1.left
                    if temp2.left != None and temp2.right != None:    
                        print("   ",temp2.left.data,end=" ")
                        print(temp2.right.data)
                        temp2 = temp2.right
                        

            else:
                break    
            
                        

                                

BinarySearchTree = BST()
BinarySearchTree.insert(25)
BinarySearchTree.insert(10)
BinarySearchTree.insert(30)
BinarySearchTree.insert(9)
BinarySearchTree.insert(11)
BinarySearchTree.insert(28)
BinarySearchTree.insert(35)
BinarySearchTree.view()

            
            

        