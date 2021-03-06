import unittest


#singlyLinkedList
class LinkedList():
    def __init__(self, val):
        self.value = val
        self.child = None

    def updateChild(self, node):
        self.child = node

    def next(self):
        return self.child

    def removeNode(self,node):
        #delete passed in node
        self.child = node.child

class doublyLinkedList():
    def __init__(self, val):
        self.value = val
        self.child = None
        self.parent = None

    def updateChild(self, node):
        self.child  = node
        self.child.parent = self

    def updateParent(self, node):
        self.parent = node
        self.parent.child = self

    def removeNode(self):
        self.parent = self.child

    def next(self):
        return self.child

def makeLinkedList(arr):
    root = LinkedList(arr[0])
    curr = root
    for x in arr[1:]:
        newNode = LinkedList(x)
        curr.updateChild(newNode)
        curr = newNode
    return root

def makeDoublyLinkedList(arr):
    root = doublyLinkedList(arr[0])
    curr = root
    for x in arr[1:]:
        newNode = doublyLinkedList(x)
        curr.updateChild(newNode)
        curr = newNode
    return root


def removeDuplicates(head):
    """
    Implement an algorith to remove duplicates from an unsorted linked LinkedList
    how would you solve this problem if a temp buffer was not allowed
    """
    p1, p2 = head, head.next()
    while not (p1 == None):
        while not (p2 == None):
            if p1.val == p2.val:
                p1.removeNode(p2)
            p2 = p2.next()
        p1 = p1.next()
    return head


def findKthLastItem(head, k):
    """
    Implement an algorithm to find the kth to last element of a singly linked List
    """
    p1,p2 = head, head.next()
    steps,kCopy = 0, k
    while not p2 is None:
        steps += 1
        p2 = p2.next()
    if k > steps:
        #subtract one since its 0 index from the right
        kCopy = k%steps - 1
    while not steps == kCopy:
        steps -= 1
        p1= p1.next()
    return p1.value

def deleteMiddle(head):
    """
    Implement an algorithm to delete a node in the middle of a singly linked list, give only access to that node
    """
    pass

def partionList(head):
    """
    partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x
    """
    pass

def linkedListRep(head1, head):
    """
    input --> linked list representation fo a number
    output --> added values of these numbers
    """
    pass

def startLoop(head):
    """
    Given a circular linkedList, return the one that is at the beginning of the loop
    """
    pass

def palindromeCheck(head):
    """
    given a linkedList check to see if the linkedList a palindrome
    """
    pass


class  LinkedListTest(unittest.TestCase):

    def test_setup(self):
        arr = [1,"a",3,4,"bc","!.",7,1,2,3]
        print "testing linkedlist"
        root = makeLinkedList(arr)
        while root:
            print root.value
            root = root.child
        arr = [1,2,3,4,"a",6,"!",1,2,3]
        print "testing doublyLinkedList"
        root = makeDoublyLinkedList(arr)
        while root:
            print "value:" + str(root.value) +" | parent "+ str(root.parent)
            root = root.next()
        pass

    def test_q1(self):
        pass

    def test_q2(self):
        arr = [1,2,3,4,5,6,7,8,9]
        root = makeLinkedList(arr)
        k = 1
        sol = len(arr) - k - 1
        self.assertEqual(findKthLastItem(root,k), arr[sol])
        k = 0
        sol = len(arr) - k - 1
        self.assertEqual(findKthLastItem(root,k), arr[sol])
        k = 9
        sol = len(arr) - k - 1
        self.assertEqual(findKthLastItem(root,k), arr[sol])
        k = len(arr)
        sol = len(arr) - k - 1
        self.assertEqual(findKthLastItem(root,k), arr[sol])

    def test_q3(self):
        pass

    def test_q4(self):
        pass

    def test_q5(self):
        pass

    def test_q6(self):

        pass
