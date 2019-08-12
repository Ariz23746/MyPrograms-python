# Creating a class Node :-
class Node:

# Creating a Constructor :-    
    
    def __init__(self,data):
        self.data = data
        self.next = None
# --------------------------------------------------------------------#

# Creating a class Stack
class Stack:

# Creating a Constructor :-

    def __init__(self):
        self.top = None
        self.bottom = None
        
# --------------------------------------------------------------------#

# creating a Function for pushing element :-  
      
    def push(self,value):
        NewElement = Node(value)
    
        #previous.next = self.bottom
        if self.top == None:
            self.top = NewElement
            self.bottom = self.top
            
        
        else:
            temp1 = NewElement 
            temp2 = self.top
            self.top = temp1
            self.top.next = temp2
            
       

# --------------------------------------------------------------------# 

#  # creating a Function for deleting from top element :- 
    
    def pop(self):
        self.top = self.top.next


# --------------------------------------------------------------------#           

# Creating a function to calculate the length :-
    
    def length(self):
        total = 0
        temp = self.top
        while True:
            if temp.next == None:
                total = total + 1
                break
            else:
                temp = temp.next
                total = total + 1        
        return total        

# --------------------------------------------------------------------#

# Creating a function to view :-
    def view(self):
        temp = self.top
        arr = []
        index = 0
        while index <= self.length() - 1:
            arr.append(temp.data)
            temp = temp.next
            index = index + 1
        print(arr)  

# --------------------------------------------------------------------#

mystack = Stack()
mystack.push('google')
mystack.push('facebook')
mystack.push('twitter')
mystack.push('wooo')
mystack.push('wooooooo')
print(mystack.length())
mystack.view()
mystack.pop()
mystack.view()




