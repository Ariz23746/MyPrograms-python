import random
class HashTable:

    def __init__(self,array):
        self.array = array
        self.length = 0


    '''def _Hash(self,key):
        
        self.address = random.randint(1,100)
        self.length = self.address'''

    def set(self,array_item1,array_item2):
        self.array[self.length] = [array_item1,array_item2]
        self.length = self.length + 1
        return self.array



r1 = HashTable([])
print(r1.set('grapes',10000))



