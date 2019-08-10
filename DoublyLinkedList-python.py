# Creating our Nodes for LinkedList :-
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
# --------------------------------------------------------------------# 

# Creating our DoubleLinkedList Function :-    
class DoubleLinkedList:

# Creating our Constructor :-
    def __init__(self):
        self.start = None
        self.tail = self.start

# --------------------------------------------------------------------#

#  Function to Calculate length in DoubleLinkedList:-
    def length(self):
        total = 0
        temp = self.start
        while True:
            if temp.next == None:
                total = total + 1
                break
            else:
                temp = temp.next
            total = total + 1
        return total

    # TimeComplexity = O(n)
    
# --------------------------------------------------------------------#

# Function for Lookups:-
    def view(self):
        temp = self.start
        arr = []
        len = self.length()
        while len!=0:
            arr.append(temp.data)
            temp = temp.next
            len = len - 1
        print(arr)

# TimeComplexity = O(n)
# --------------------------------------------------------------------#

# Function to insert element in the last index of LinkedList:-

    def append(self,value):
        NodeObject = Node(value)

        if self.start == None:
            self.start = NodeObject
            self.tail = self.start


        else:
            self.tail.next = NodeObject
            self.tail = NodeObject
            self.tail.next = None
        

# --------------------------------------------------------------------#

# Function to delete an element from the desired index of the linkedList :-

    def delete(self,index):
        if index > self.length() or self.start == None:
            print('\nEither dont have that much element in linkedlist or linkedlist is empty')

        else:
            if index == 0:
                self.start = self.start.next
                self.start.prev = None
                


            else:
               temp = self.start
               cur_index = 0
               while True:
                current_node = temp
                temp = temp.next
                if cur_index == index - 1:
                    current_node.next = temp.next
                    break

                else:
                    cur_index = cur_index + 1

# TimeComplexity = O(n)

# --------------------------------------------------------------------#

#Function to insert any value on desired index in LinkedList:-

    def insert(self,index,value):
        cur_index = 0
        if index > self.length():
            print("please insert correct index")
        else:

            if index == 0:
                temp = self.start
                newelement = Node(value)
                self.start = newelement
                self.start.next = temp
                self.prev = None
            
            elif index == self.length():
                temp = self.tail
                newelement = Node(value)
                self.tail = newelement
                self.tail.next = None
                self.tail.prev = temp
                temp.next = self.tail


            else:

                temp = self.start
                current_node = temp
                while cur_index != index:
                    current_node = temp
                    temp = temp.next
                    cur_index+=1

                
                newelement = Node(value)
                current_node.next = newelement
                newelement.next = temp
                newelement.prev = current_node

# TimeComplexity = O(n)
# --------------------------------------------------------------------#

mylinkedlist = DoubleLinkedList()
mylinkedlist.append(23)
mylinkedlist.append(25)
mylinkedlist.append(68)
mylinkedlist.view()
print(mylinkedlist.length())
mylinkedlist.insert(3,45)
mylinkedlist.view()
mylinkedlist.append(27)
mylinkedlist.view()
mylinkedlist.delete(4)
mylinkedlist.view()


