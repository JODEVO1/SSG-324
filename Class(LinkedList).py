class Node:
    def __init__(self, data=None, next=None)
        self.data = data
        self.next = next

#self is referring to the instance of the class
#init defines the constructor. the = means you're giving it a defult valu//

class LinkedList: 
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode 
        self.length = 1
def insert_art_end(self, data):
    newNode = Node(data)
    if self.head is None:
        self.head = newNode
        self.tail = newNode
    else:
        self.tail.nexy = newNode
        self.tail = newNode
    self.length+=1

    return self
if __name__ == 'main':
    myList = LinkedList(5)
    myList.insert_at_end(10)

    print(myList.head.data)