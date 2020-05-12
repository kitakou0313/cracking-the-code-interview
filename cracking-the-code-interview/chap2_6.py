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


def is_palindrome(ll):
    lenLL = getLengthLL(ll)
    valSet = set([])
    for node in ll:
        if node.value not in valSet:
            valSet.add(node.value)
        else:
            valSet.remove(node.value)

    return len(valSet) == 1 if lenLL % 2 == 1 else len(valSet) == 0


ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))
