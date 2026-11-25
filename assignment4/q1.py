
# Q.1 E-Commerce Product Search System Using BST

# Create a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 1. Insert product IDs into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# 2. Display product IDs in ascending order
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# 3. Search product ID
def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# 4. Delete product ID
def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# 5. Preorder Traversal
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# 6. Find Minimum Product ID
def find_min(root):
    while root.left:
        root = root.left
    return root.data


# Find Maximum Product ID
def find_max(root):
    while root.right:
        root = root.right
    return root.data


# Main Program
root = None

product_ids = [150, 100, 200, 75, 125, 175, 250, 60, 90, 110]

# Create BST
for id in product_ids:
    root = insert(root, id)

print("BST Created Successfully")

# Display in ascending order
print("\nProduct IDs in Ascending Order:")
inorder(root)

# Search product ID 175
print("\n\nSearching Product ID 175:")
if search(root, 175):
    print("Product ID 175 exists")
else:
    print("Product ID 175 does not exist")

# Delete product ID 100
root = delete(root, 100)

print("\nAfter Deleting Product ID 100:")
inorder(root)

# Display all traversals after deletion
print("\n\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)

# Find minimum and maximum
print("\n\nMinimum Product ID:", find_min(root))
print("Maximum Product ID:", find_max(root))

