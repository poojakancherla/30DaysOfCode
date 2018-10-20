class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
            #     if root.left is None:
            #         root.left = root.data
            #     else:
            #         self.insert(root.left, root.data)
                root.left=self.insert(root.left,data)
                # root.left=cur
            else:
                # if root.right is None:
                #     root.right = root.data
                # else:
                #     self.insert(root.right, data)
                root.right=self.insert(root.right,data)
                # root.right=cur
        return root

    def getHeight(self,root):
        if root == None:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
