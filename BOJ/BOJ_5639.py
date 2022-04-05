import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.head = Node(None)

    def insert(self, val):
        if self.head.val == None:
            self.head.val = val
        else:
            curr = self.head
            prev = None
            while curr != None:
                prev = curr
                if curr.val < val:
                    curr = curr.right
                else:
                    curr = curr.left
            if prev.val < val:
                prev.right = Node(val)
            else:
                prev.left = Node(val)

    def post(self, curr):
        if curr == None:
            return
        self.post(curr.left)
        self.post(curr.right)
        print(curr.val)


sys.setrecursionlimit(10**6)
tree = Tree()
data = sys.stdin.read().split("\n")
for val in data:
    if val != "":
        tree.insert(int(val))
tree.post(tree.head)
