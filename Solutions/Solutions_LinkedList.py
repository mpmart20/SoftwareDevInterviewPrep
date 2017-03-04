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
        self.val = val
        self.child = None
        self.parent = None

    def appendTo(self, node):
        self.child  = node
        self.child.parent = self

    def insertInto(self, node):
        self.parent = node
        self.parent.child = self

    def removeNode(self):
        self.parent = self.child




def removeDuplicates(head):
    """
    Implement an algorith to remove duplicates from an unsorted linked LinkedListhow would you solve this problem if a temp buffer was not allowed
    """
    p1, p2 = head, head.next()
    while not (p1 == None):
        while not (p2 == None):
            if p1.val == p2.val:
                p1.removeNode(p2)
            p2 = p2.next()
        p1.next() = p1.next()
    return head


def findKthLastItem(head, k):
    """
    Implement an algorithm to find the kth to last element of a singly linked List
    """
    p1,p2 = head, head.next()
    steps = 0
    while not p2 is None:
        steps += 1
        p2 = p2.next()
    while not steps == k:
        steps -= 1
        p1= p1.next()
    return p1.val

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

    def test_q1(self):
        pass

    def test_q2(self):
        pass

    def test_q3(self):
        pass

    def test_q4(self):
        pass

    def test_q5(self):
        pass

    def test_q6(self):

        pass
