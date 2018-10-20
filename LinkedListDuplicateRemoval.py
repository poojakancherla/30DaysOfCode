class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self, head):
        lookup = {}
        node = head
        if node:
            while(node):
                lookup[node.data] = 1 # Add every node not present in lookup
                while(node.next and node.next.data in lookup): # If next node is in lookup
                    node.next = node.next.next # Skip the link to that node
                node = node.next # If the next node is not in lookup, assign it to current node
        return head




mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);
