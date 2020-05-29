#Sari Stissi
#Assingment 4

from Assignment4_singlyLinkedList import *
from Assignment3_circqueueClass import *
import time

class LinkedQueue():

    #initialize the linked queue
    def __init__(self):
        self.queueList = SinglyLinkedList()
        self.front = self.queueList.head
        self.rear = self.queueList.tail
        self.size = self.queueList.size

    #return whether the LinkedQueue is empty or not
    def isEmpty(self):
        return self.front == "None" and self.rear == "None"

    #add a node to the linked queue
    def enqueue(self, e):
        newNode = Node(e)

        #if there are no nodes in the queue
        if self.size == 0:
            #make the new node both the front and the rear of the queue
            self.front = newNode
            self.rear = newNode

        #if there are nodes already in the queue
        else:
            #link the rear node to the new node and make the new node the new rear
            self.rear.nextNode = newNode
            self.rear = newNode

        #update the size of the queue
        self.size += 1

    #remove a node from the linked queue
    def dequeue(self):
        #check if there is anything to remove from the queue
        if self.size == 0:
            print("There are no nodes to remove in the list")
        else:
            #need to delink the front node that we are removing
            #get the front node from the queue
            oldHead = self.front

            #if the front node was the only node in the list
            if oldHead.nextNode == "None":
                #make both the front and rear none since the node is being removed
                self.front = "None"
                self.rear = "None"

            #if there is more than one node in the list
            else:
                #make the front of the queue the next node in the queue
                self.front = oldHead.nextNode

            #update the size of the queue
            self.size -= 1

            #return the node that was removed
            return oldHead.data
            
    #function to print what is currently in the queue
    def printQueue(self):
        #get the current node
        current = self.front

        #string to be printed with the node data
        linkedListString = ""

        #check if the queue is empty
        if self.size == 0:
            print("There are no nodes in the queue")
        else:
            #while there is a next  emelment in the queue
            while current.nextNode != "None":
                #add the data to the string
                linkedListString += str(current.data) + ", "
                #move the next element
                current = current.nextNode
            #add the last element to the list
            linkedListString += str(self.rear.data)
            #print the string form of the queue
            print(linkedListString) 

if __name__ == "__main__":
    #using time to find the length of time needed to add and remove things from a linked queue and a circle queue
    startTimeOfEntireProcess = time.clock()
    lq = LinkedQueue()
    cq = Circ_Queue()
    startTimeEnqueueLinked = time.clock()
    for i in range(50000):
        lq.enqueue(i)
    endTimeEnqueueLinked = time.clock()
    
    startTimeEnqueueCirc = time.clock()
    for i in range(50000):
        cq.enqueue(i)
    endTimeEnqueueCirc = time.clock()
    
    startTimeDequeueLinked = time.clock()
    for i in range(25000):
        lq.dequeue()
    endTimeDequeueLinked = time.clock()
    
    startTimeDequeueCirc = time.clock()
    for i in range(25000):
        cq.dequeue()
    endTimeDequeueCirc = time.clock()
    
    startTimeEnqueue2Linked = time.clock()
    for i in range(50000, 100000):
        lq.enqueue(i)
    endTimeEnqueue2Linked = time.clock()
    
    startTimeEnqueue2Circ = time.clock()
    for i in range(50000, 100000):
        cq.enqueue(i)
    endTimeEnqueue2Circ = time.clock()
   
    startTimeRemoveLinked = time.clock()
    for i in range(lq.size):
        lq.dequeue()
    endTimeRemoveLinked = time.clock()
    
    startTimeRemoveCirc = time.clock()
    for i in range(cq.size):
        cq.dequeue()
    endTimeRemoveCirc = time.clock()

    endTimeOfEntireProcess = time.clock()

    print("Time required for enqueue on the LinkedQueue is " + str(endTimeEnqueueLinked - startTimeEnqueueLinked) + " seconds")
    print("Time required for enqueue on the CircularQueue is " + str(endTimeEnqueueCirc - startTimeEnqueueCirc) + " seconds")
    print()
    print("-----------------------------------------------------------------------------")
    print()
    print("The time required for dequeue on the LinkedQueue is " + str(endTimeDequeueLinked - startTimeDequeueLinked) + " seconds")
    print("The time required for dequeue on the CircularQueue is " + str(endTimeDequeueCirc - startTimeDequeueCirc) + " seconds")
    print()
    print("------------------------------------------------------------------------------")
    print()
    print("The time required for the 2nd enqueue on the LinkedQueue is " + str(endTimeEnqueue2Linked - startTimeEnqueue2Linked) + " seconds")
    print("The time required for the 2nd enqueue on the CircularQueue is " + str(endTimeEnqueue2Circ - startTimeEnqueue2Circ) + " seconds")
    print()
    print("------------------------------------------------------------------------------")
    print()
    print("The time required to remove everything from LinkedQueue " + str(endTimeRemoveLinked - startTimeRemoveLinked) + " seconds")
    print("The time required to remove everything from CircularQueue " + str(endTimeRemoveCirc - startTimeRemoveCirc) +  " seconds")
    print()
    print("-------------------------------------------------------------------------------")
    print()
    print("Total time it took to run all of this " + str(endTimeOfEntireProcess - startTimeOfEntireProcess) + " seconds")
    
   
