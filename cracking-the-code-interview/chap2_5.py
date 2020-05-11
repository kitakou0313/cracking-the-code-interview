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


def sum_lists(ll_a, ll_b):
    currentA = ll_a.head
    currentB = ll_b.head

    if getLengthLL(ll_a) < getLengthLL(ll_b):
        for i in range(getLengthLL(ll_b) - getLengthLL(ll_a)):
            ll_a.add(0)
    elif getLengthLL(ll_a) > getLengthLL(ll_b):
        for i in range(getLengthLL(ll_a) - getLengthLL(ll_b)):
            ll_b.add(0)

    ll_a.add(0)
    ll_b.add(0)

    carry = 0
    ans = LinkedList()

    while not(currentA is None and currentB is None):

        value = currentA.value + currentB.value + carry

        ans.add(value % 10)

        carry = value // 10

        currentA = currentA.next
        currentB = currentB.next

    return ans


def addLLRe(nodeA, nodeB, carry):
    if nodeA is None and nodeB is None:
        return LinkedList()
    val = nodeA.value + nodeB.value
    return (addLLRe(nodeA.next, nodeB.next, val // 10)).add(val % 10)


def sum_lists_followup(ll_a, ll_b):
    if getLengthLL(ll_a) < getLengthLL(ll_b):
        for i in range(getLengthLL(ll_b) - getLengthLL(ll_a)):
            ll_a.add_to_begining(0)
    elif getLengthLL(ll_a) > getLengthLL(ll_b):
        for i in range(getLengthLL(ll_a) - getLengthLL(ll_b)):
            ll_b.add_to_begining(0)

    return addLLRe(ll_a.head, ll_b.head, 0)


ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(4, 0, 9)
print(ll_a)
print(ll_b)
print(sum_lists(ll_a, ll_b))
#print(sum_lists_followup(ll_a, ll_b))
