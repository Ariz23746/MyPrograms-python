# creating node of LinkedList

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
# --------------------------------------------------------------------#

# Creating Our Own LinkedList:-

class LinkedList:

    # Creating Constructor having initially start set to None

    def __init__(self):
        self.start = None
        self.tail = self.start

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

# --------------------------------------------------------------------#
    # Function to calculate length of the LinkedList:-

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

# Function to delete an element from the desired index of the linkedList :-

    def delete(self,index):
        if index > self.length() or self.start == None:
            print('\nEither dont have that much element in linkedlist or linkedlist is empty')

        else:
            if index == 0:
                self.start = self.start.next
            else:
                temp = self.start
                cur_index = 0

                while True:
                    previous = temp
                    temp = temp.next
                    if cur_index == index - 1:
                        previous.next = temp.next
                        break

                    else:
                        print('ariz')
                        cur_index = cur_index + 1

# TimeComplexity = O(n)

# --------------------------------------------------------------------#
# Function to insert any value on desired index in LinkedList:-

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

            else:

                temp = self.start
                previous = temp
                while cur_index != index:
                    previous = temp
                    temp = temp.next
                    cur_index+=1
                newelement = Node(value)
                previous.next = newelement
                newelement.next = temp

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


mylinkedlist = LinkedList()
mylinkedlist.append(23)
mylinkedlist.append(25)
mylinkedlist.append(26)
mylinkedlist.append(28)
mylinkedlist.append(30)
mylinkedlist.insert(5,11)
mylinkedlist.delete(0)
length=mylinkedlist.length()
mylinkedlist.view()



