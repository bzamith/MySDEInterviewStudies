# Source: https://leetcode.com/problems/merge-two-sorted-lists/

# Problem: "Merge Two Sorted Linked Lists"

def mergeTwoLists(l1, l2):
    if not l1 and not l2:
        return None
    if not l1:
        return l2
    if not l2:
        return l1
    pointerFirst = l1
    pointerSecond = l2
    if l1 and l1.val <= l2.val:
        l3 = ListNode(l1.val)
        pointerFirst = pointerFirst.next
    else:
        l3 = ListNode(l2.val)
        pointerSecond = pointerSecond.next
    pointerThird = l3
    while pointerFirst or pointerSecond:
        if not pointerFirst:
            pointerThird.next = ListNode(pointerSecond.val)
            pointerSecond = pointerSecond.next
        elif not pointerSecond:
            pointerThird.next = ListNode(pointerFirst.val)
            pointerFirst = pointerFirst.next
        elif pointerFirst.val <= pointerSecond.val:
            pointerThird.next = ListNode(pointerFirst.val)
            pointerFirst = pointerFirst.next
        else:
            pointerThird.next = ListNode(pointerSecond.val)
            pointerSecond = pointerSecond.next
        pointerThird = pointerThird.next
    return l3