from LinkedList import LinkedList


def backFromLast(node, n):
    if node == None:
        return 0
    else:
        index = backFromLast(node.next, n) + 1
        if index == n:
            print(n, "th is ", node.value)
        return index


def kth_to_last(ll, n):
    backFromLast(ll.head, n)


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
kth_to_last(ll, 3)
