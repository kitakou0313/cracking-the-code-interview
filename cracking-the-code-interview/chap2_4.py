from LinkedList import LinkedList


def partition(ll, n):
    srtLL = LinkedList()
    node = ll.head
    while node != None:
        if node.value < n:
            srtLL.add_to_beginning(node.value)
        else:
            srtLL.add(node.value)
        node = node.next
    return srtLL


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(partition(ll, ll.head.value))
