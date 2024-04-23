"""
Binaru tree traversal.
"""

# Pre-order traversal
def pre_order(node):
    """
    Binary tree traversal in pre order.
    """
    lst = []
    if node is not None:
        lst.append(node.data)
        lst = lst + pre_order(node.left)
        lst = lst + pre_order(node.right)
    return lst

# In-order traversal
def in_order(node):
    """
    Binary tree traversal (in) in order.
    """
    lst = []
    if node is not None:
        lst = in_order(node.left)
        lst.append(node.data)
        lst = lst + in_order(node.right)
    return lst

# Post-order traversal
def post_order(node):
    """
    Binary tree traversal in post order.
    """
    lst = []
    if node is not None:
        lst = post_order(node.left)
        lst = lst + post_order(node.right)
        lst.append(node.data)
    return lst
