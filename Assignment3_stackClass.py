#Sari Stissi
#Assignment 3

class Stack():
    #initialize variables
    def __init__(self, capacity=10): #creates a default capacity of 10
        #create array to store elements
        self.stackArray = []
        #top var will initially be at -1 b/c there are no items in the array yet
        self.top = -1
        #sets new capacity for size
        self.size = capacity
        #I'm going to set temp vars in the stackArray according to capacity
        for i in range(capacity):
            self.stackArray.append(0)
        if not isinstance(capacity, (int)):
            raise TypeError("Size of an array can't be a string or a float number")

    def isEmpty(self):
        #if top hasn't been moved yet, there's nothing in the list
        return self.top == -1

    def push(self, e):
        #check to make sure it won't go past capacity
        if len(self.stackArray) <= self.size:
            #add element to stack
            self.stackArray[(self.top + 1)] = e
            #change top now that there's something in it
            self.top += 1
        else:
            return("You can't add anymore elements to the stack")

    def pop(self):
        #checks to make sure there are elements in the list
        if not self.isEmpty():
            #saves the element we're taking out in a temp var
            oldTop = self.stackArray[self.top]
            #replace with a placeholder 0
            self.stackArray[self.top] = 0
            #change the top
            self.top -= 1
            #return the element we got rid of
            return oldTop

    def peek(self):
        return self.stackArray[self.top]
            
        
            
            
            
