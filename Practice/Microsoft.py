def BST(key, node):
     if node == None:
          return False
     elif key == node.data:
          return True
     elif key < node.data:
          BST(key, node.leftChild)
