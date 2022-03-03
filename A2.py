#What is the main difference between Stack and Queue?
    #The main difference between stacks and queues is how items are added to each. Stacks are first in, last out, as each item added pushes the previous items further and further down. Queues are first in, first out, as each new item is added to the bottom instead.

#What are the main operations in both Stack and Queue?
    #Stack operations: push, pop, peek
    #Queue operations: enqueue, dequeue, front

#Using Python, implement Queue data structure as explained in the lecture.
class Node:
    #Function to initalize node
    def __init__(self,data):
        self.data = data #Assign data
        self.next = None #Intialize next as null
class LinkedList:
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None
        self.tail = None
    def front(self):
        return self.head
    def end(self):
        return self.tail
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def enqueue(self,Node):
        if self.isEmpty():
            self.head = Node
            self.tail = Node
        else:
            self.tail.next = Node
            self.tail = Node
    def dequeue(self):
        if self.head == None:
            self.head = None
            self.tail = None
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
    def size(self):
        count = 0
        current = self.head
        if current != None:
            count += 1
            while current.next != None:
                count += 1
        return count
queue = LinkedList()
queue.enqueue(Node(1))
queue.dequeue()
queue.dequeue()
print(queue.isEmpty())
print(queue.front())
print(queue.end())
print(queue.size())
    
#Apply merge sort on this list [1, 6, 3, 2, 7, 5, 8, 4] and show your work as in Figure 1.
    #[1,6,3,2,7,5,8,4] - DIVIDE
    #[1,6,3,2] - [7,5,8,4] - DIVIDE
    #[1,6] - [3,2] - [7,5] - [8,4] - DIVIDE
    #[1] - [6] - [3] - [2] - [7] - [5] - [8] - [4] - MERGE
    #[1,6] - [2,3] - [5,7] - [4,8] - MERGE
    #[1,2,3,6] - [4,5,7,8] - MERGE
    #[1,2,3,4,5,6,7,8]

#Using recursion tree, find O(.) for T(n) in each of the following recurrences assuming that T(n) is 0 for n=1:
    #1. T(n) = 2T(n/2) + 𝛉(n)
        #n --> n/2 n/2 --> n/4 n/4 n/4 n/4 --> n/k...
        #n = 2^k --> k = log(n)
        #2T(n/2) + 𝛉(n) = nk times, O(nlog(n))
    #2. T(n) = 2T(n/2) + 𝛉(n^2)
        #n^2 --> n^2/2 n^2/2 --> n^2/4 n^2/4 n^2/4 n^2/4 --> n^2/k...
        #I am not sure how to do this, but it seems like a geometric series so I am going to say it is O(n^2)
    #3. T(n) = T(n/3) + T(2n/3) + 𝛉(n)
        #n --> n/3 2n/3 --> n/9 2n/9 2n/9 4n/9 --> ...
        #The longest side becomes log(3/2) n, so O(nlog(n)) is closest
    #4. T(n) = 3T(n/4) + 𝛉(n^2)
        #n --> n/4 n/4 n/4 --> n/16 n/16 n/16 n/16 n/16 n/16 n/16 n/16 n/16 --> . . .
        #Each time the length increases by n^2
        #O(n^2)
    #5. T(n) = 2T(n/2) + 𝛉(nlog(n))
        #As with #1, it will come out to k = log(n).
        #This means that instead of nk times, it will be nlog(n)k times for O(nlog^2(n))