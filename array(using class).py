class Array:

    def __init__(self):
        self.length = 0
        self.array = {}


    def ourArray(self, index):
        return self.array[index]


    def push(self, item):
        self.array[self.length] = item
        self.length = self.length + 1
        return self.array


    def pop(self):
        del(self.array[self.length - 1])
        self.length = self.length - 1
        return self.array


    def delete(self, indices):
        item = self.array[indices]             # O(1)
        while(indices < self.length - 1):      # O(n)

            self.array[indices] = self.array[indices + 1]
            indices = indices + 1

        self.length = self.length - 1          # O(1)
        self.array[self.length] = item         # O(1)
        del(self.array[self.length])           # O(1)
        return self.array                      # O(1)

    # time complexity will be O(5 + n) = O(n)


arr = Array()
arr.push('hi')
arr.push('my')
arr.push('name')
arr.push('is')
arr.push('Ariz')
print(arr.push('khan'))
print(arr.delete(5))








