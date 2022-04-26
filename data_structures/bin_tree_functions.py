from queue import Queue
def breadth_first_search(root, target):
    if root == None:
        return False
    q = Queue(maxsize = 0)
    q.put(root)

    while q.qsize() > 0:
        current = q.get()
        if current.val == target:
            return True
        if current.left:
            q.put(current.left)
        if current.right:
            q.put(current.right)
    
    return False

def tree_includes_recurse(root, target):
    if root == None:
        return False
    if root.val == target:
        return True
    return tree_includes_recurse(root.left, target) or tree_includes_recurse(root.right, target)

def tree_sum_recurse(root):
    if root == None:
        return 0
    return root.val + tree_sum_recurse(root.left) + tree_sum_recurse(root.right)