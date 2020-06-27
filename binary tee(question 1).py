class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(root, n1, n2):
    # Base Case
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if (root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

        # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if (root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)

    return root


# Driver program to test above function

# Let us construct the BST shown in the figure
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)


n1 = 10;
n2 = 14
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

n1 = 14
n2 = 8
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

n1 = 10
n2 = 22
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))