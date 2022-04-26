class node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class binary_tree(object):
    def __init__(self, root):
        self.root = node(root)


a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')
f = node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#           a
#          /  \
#        b      c
#       /  \      \
#      d    e       f

#------------------------------ Iterative Solution --------------------------------------------------------------------------------------
#
#def depth_first_values(root):
#    stack = [root]
#    result = []
#    if root == None:
#        return []
#    while len(stack) > 0:
#        current = stack.pop()
#        result.append(current.val)
#        if current.right:
#            stack.append(current.right)
#        if current.left:
#            stack.append(current.left)
#    return result
#
#depth_first_values(a)


#------------------------------------ Recursive Solution ----------------------------------------------------------------------------------

def depth_first_values(root):
    if root == None:
        return []
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val, *left_values, *right_values]

# ----------------------------------------------------------------------------------------------------------------------------------------------
#requires Queue ds (from built in module)
from queue import Queue


def breadth_first_search(root):

    if root == None:
        return []
    q = Queue(maxsize = 0)
    q.put(root)

    values = []

    while q.qsize() > 0:

       current = q.get()
       values.append(current.val)
       if current.left:
           q.put(current.left)
       if current.right:
            q.put(current.right)
    
    return values

def tree_sum_recurse(root):
    if root == None:
        return 0
    return root.val + tree_sum_recurse(root.left) + tree_sum_recurse(root.right)