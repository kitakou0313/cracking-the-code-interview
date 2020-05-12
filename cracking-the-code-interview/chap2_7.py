from LinkedList import LinkedList


def getLengthLL(ll):
    if ll.head is None:
        return 0
    current = ll.head
    ans = 0
    while current != None:
        ans += 1
        current = current.next
    return ans


def isIntersection(ll1, ll2):
    if ll1.tail != ll2.tail:
        return False

    len1 = getLengthLL(ll1)
    len2 = getLengthLL(ll2)

    currentL1 = ll1.head
    currentL2 = ll2.head

    if len1 >= len2:
        for i in range(len1 - len2):
            currentL1 = currentL1.next
    else:
        for in range(len2 - len1):
            currentL2 = currentL2.next

    ans = LinkedList()
    while not(currentL1 is None and currentL2 is None):
        if currentL1 == currentL2:
            ans.add(currentL1)

    return ans
