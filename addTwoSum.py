# Definition for singly-linked list.
import json


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        carry = 0
        p, q, curr = l1, l2, dummy
        if p.val == 0 and p.next == None:
            return q
        if q.val == 0 and q.next == None:
            return p
        while (p or q):
            x =  p.val if p != None else 0
            y = q.val if q != None else 0
            add_sum = carry + x + y
            carry = add_sum // 10
            curr.next = ListNode(add_sum % 10)
            curr = curr.next
            p = p.next if p != None else None
            q = q.next if q != None else None

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')

    # lines = readlines()
    #
    # line = lines.next()

    l1 = stringToListNode(" [0, 8, 6, 5, 6, 8, 3, 5, 7]")
    # line = lines.next()
    l2 = stringToListNode("[6, 7, 8, 0, 8, 5, 8, 9, 7]")

    ret = Solution().addTwoNumbers(l1, l2)

    out = listNodeToString(ret)
    print("result:", out)


if __name__ == '__main__':
    main()
