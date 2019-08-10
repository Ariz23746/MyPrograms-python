class Array:
    
# Constructing a Constructor
    def __init__(self):
        self.length = 0
        self.array = {}

# --------------------------------------------------------------------#
# Function to return our array:-
    def ourArray(self, index):
        return self.array[index]

# --------------------------------------------------------------------#
# Function to add element at the last index of an array :-
    def push(self, item):
        self.array[self.length] = item
        self.length = self.length + 1
        return self.array

# --------------------------------------------------------------------#
# Function to remove element from the last index of an array :-
    def pop(self):
        del(self.array[self.length - 1])
        self.length = self.length - 1
        return self.array

# --------------------------------------------------------------------#
# Function to delete an element from desire index of an array
    def delete(self, index):
        item = self.array[index]             # O(1)
        while(index < self.length - 1):      # O(n)

            self.array[index] = self.array[index + 1]
            index = index + 1

        self.length = self.length - 1          # O(1)
        self.array[self.length] = item         # O(1)
        del(self.array[self.length])           # O(1)
        return self.array                      # O(1)

    # time complexity will be O(5 + n) = O(n)
# --------------------------------------------------------------------#

arr = Array()
arr.push('hi')
arr.push('my')
arr.push('name')
arr.push('is')
arr.push('Ariz')
print(arr.push('khan'))
print(arr.delete(5))








