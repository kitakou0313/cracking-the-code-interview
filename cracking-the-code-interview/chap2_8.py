from LinkedList import LinkedList


def getLoopStartNode(ll):
    slow = fast = ll.head

    while not(slow == fast):
        if fast is None or slow is None:
            return False

        fast = fast.next.next
        slow = slow.next

    slow = ll.head

    while not(slow == fast):
        slow = slow.next
        fast = fast.next

    return slow
