class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    start = None
    #  function to display the linked list
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    # function to insert the nodes to the linked list
    def insert(self,head,data):
        if head == None:
            return Node(data)
        elif head.next == None:
            head.next = Node(data)
        else:
            mylist.insert(head.next, data)
        return head


#inputs and testing the solution
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)

mylist.display(head);
