from LinkedList import LinkedList


def remove_dups(ll):
    if ll.head == None:
        return False

    currrent = ll.head
    seen = set([ll.head.value])
    while currrent.next:
        if ((currrent.next.value in seen)):
            currrent.next = currrent.next.next
        else:
            seen.add(currrent.next.value)
            currrent = currrent.next


def remove_dups_followup(ll):
    if ll.head == None:
        return False
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if(runner.next.value == current.value):
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
print(len(ll))
remove_dups(ll)
print(ll)
print(len(ll))

ll.generate(100, 0, 9)
print(ll)
remove_dups_followup(ll)
print(ll)
print(len(ll))
