#Sari Stissi
#Assignment 3

class Circ_Queue():
    #initialize variables
    def __init__(self, capacity=10): #creates a default capacity of 10
        #create array to store elements
        self.queueArray = []
        #front will be set to -1 because there are no elements in the array yet
        self.front = -1
        #rear will be set to -1 because there are no elements in the array yet
        self.rear = -1
        #sets the capactiy of the array
        self.size = capacity
        #set temp vars in the stackArray according to capacity
        for i in range(capacity):
            self.queueArray.append(0)
        if not isinstance(capacity, (int)):
            raise TypeError("Size of an array can't be a string or a float number")

    def isEmpty(self):
        #if the front and rear are at the same place then there shouldn't be any elements
        return self.front == -1 and self.rear == -1

    def enqueue(self, e):
        #check to see if the queue is full
        if (self.rear + 1 == self.size and self.front == 0) or (self.rear + 1 == self.front):
            #if rear is at the end of the queue
            if self.rear == self.size -1:
                #append placeholder to increase size
                self.queueArray.append(0)
                #increase the size by number of elements which is one
                self.size +=1
                #insert element at the end
                self.queueArray[(self.rear + 1)] = e
                #increment rear
                self.rear += 1
            #if rear is at the 0 index
            elif self.rear >= 0 and self.front == self.rear + 1:
                #append placeholder to increase the size
                self.queueArray.append(0)
                #increase the size by number of elements which is one
                self.size += 1
                #shift all the elements at rear + 1 over to the right
                for index in range(self.size - 1, self.rear +1, -1):
                    self.queueArray[index] = self.queueArray[index -1]
                #add in new element
                self.queueArray[self.rear + 1] = e
                #increment rear and front
                self.rear +=1
                self.front += 1
        #This is for if we're add the first element to the queue
        elif self.front == -1:
            #move front and rear to 0
            self.front = 0
            self.rear = 0
            #put element in the queue
            self.queueArray[self.rear] = e
        #if front is no longer at index 0 and the rear is at the last possible index    
        elif self.rear == self.size -1 and self.front != 0:
            #this makes it circular
            self.rear = 0
            self.queueArray[self.rear] = e
        #every other case 
        else:
            self.rear += 1
            self.queueArray[self.rear] = e

    def dequeue(self):
        #check to see if queue is emepty
        if self.isEmpty():
            return("There are no elements to remove!")
        #Save the data that we're removing so that we can return it
        dataToReturn = self.queueArray[self.front]
        #Remove the data by putting the zero placeholder in it
        self.queueArray[self.front] = 0
        #check if the queue is empty
        if self.front == self.rear:
            #if yes make front and rear -1 to show that there is no elements
            self.front = -1
            self.rear = -1
        #if the front is at the end and we remove it
        elif self.front == self.size - 1:
            #we have to go back to 0 b/c it's circular
            self.front = 0
        else:
            self.front += 1
        return dataToReturn
            



    


