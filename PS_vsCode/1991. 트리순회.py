class Node:
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def preorder(node):
    print(node.data, end='')
    if node.left_node != '.':
        preorder(tree[node.left_node])
    if node.right_node != '.':
        preorder(tree[node.right_node])

def inorder(node):
    if node.left_node != '.':
        inorder(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        inorder(tree[node.right_node])

def postorder(node):
    if node.left_node != '.':
        postorder(tree[node.left_node])
    if node.right_node != '.':
        postorder(tree[node.right_node])
    print(node.data, end='')

N = int(input())

tree = {}

for i in range(N):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
