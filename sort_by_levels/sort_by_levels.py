"""
Sort binary tree by levels.
"""

class Nd:
    """
    Base class for an instance of Node.
    (renamed to avoid confusion)
    """
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    """
    Class for instances of the queue data structure.
    """
    def __init__(self):
        self.front = None
        self.back = None

    def empty(self):
        """
        Case for an empty queue.
        """
        return self.front is None and self.back is None

    def push(self, item):
        """
        Add an element to the queue.
        """
        nd = Nd(item)
        if self.empty():
            self.front = nd
        else:
            self.back.next = nd

        self.back = nd

    def pop(self):
        """
        Delete an element from the queue.
        """
        if self.empty():
            raise Exception("Queue is empty")

        current = self.front
        item = current.item
        self.front = self.front.next
        del current

        if self.front is None:
            self.back = None

        return item


def tree_by_levels(node):
    """
    Main sorting function for the tree levels.
    """
    if node is None:
        return []
    lst = []
    q = Queue()
    q.push(node)
    while not q.empty():
        nde = q.pop()
        if nde is not None:
            lst.append(nde.value)
            q.push(nde.left)
            q.push(nde.right)

    return lst
