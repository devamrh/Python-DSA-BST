class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertNode(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insertNode(root.left, data)
    elif data > root.data:
        root.right = insertNode(root.right, data)
    return root

def preOrderTraversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def postOrderTraversal(root):
    if root is None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end=" ")

def inOrderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.data, end=" ")
    inOrderTraversal(root.right)

def isBinarySearchTree(root):
    if root is None:
        return True
    if (root.left is not None and root.left.data > root.data) or (root.right is not None and root.right.data < root.data):
        return False
    if not isBinarySearchTree(root.left) or not isBinarySearchTree(root.right):
        return False
    return True

def countNodesNeeded(root, minValue, maxValue):
    if root is None:
        return 0
    if root.data < minValue or root.data > maxValue:
        return 1 + countNodesNeeded(root.left, minValue, root.data - 1) + countNodesNeeded(root.right, root.data + 1, maxValue)
    return countNodesNeeded(root.left, minValue, root.data - 1) + countNodesNeeded(root.right, root.data + 1, maxValue)

root = None
n = int(input("Enter the number of nodes: "))
for i in range(n):
    x = int(input("Enter the value of node " + str(i+1) + ": "))
    root = insertNode(root, x)

print("Pre-order traversal: ", end="")
preOrderTraversal(root)
print()
print("Post-order traversal: ", end="")
postOrderTraversal(root)
print()
print("In-order traversal: ", end="")
inOrderTraversal(root)
print()

if isBinarySearchTree(root):
    print("The tree is a binary search tree.")
else:
    nodesNeeded = countNodesNeeded(root, -float('inf'), float('inf'))
    print("The tree is not a binary search tree.")
    print("Number of nodes needed to make the tree a binary search tree:", nodesNeeded)
    choice = input("Would you like to re-enter the values to create a binary search tree? (y/n): ")
    if choice == 'y' or choice == 'Y':
        root = None
        for i in range(n):
            x = int(input("Enter the value of node " + str(i+1) + ": "))
            root = insertNode(root, x)
        if isBinarySearchTree(root):
            print("The tree is now a binary search tree.")
        else:
            print("The tree is still not a binary search tree.")
