class Stack:
    
    def __init__(self):
        self.array = []

# --------------------------------------------------------------------# 
# creating a Function for pushing element :-  
      
    def push(self,value):
        self.array.append(value)
        return self.view()
        

# --------------------------------------------------------------------# 
# creating a function for viewing :-
    def view(self):
        print(self.array)
# --------------------------------------------------------------------#
# creating a Function for pushing element :-  
      
    def pop(self):
        self.array.pop()
        return self.view()

# --------------------------------------------------------------------#     
    

mystack = Stack()
mystack.push('google')
mystack.push('facebook')
mystack.push('facebook')
mystack.pop()

