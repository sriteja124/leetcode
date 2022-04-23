class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self,l1,l2):
        carry = 0
        result = ListNode(0)
        pointer = result

        while (l1 or l2 or carry):
            first_num = l1.val if l1.val else 0
            second_num = l2.val if l2.val else 0

            summation = first_num + second_num + carry

            num = summation % 10
            carry = summation // 10

            pointer.next = ListNode(num)

            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
a,a.next,a.next.next= ListNode(2), ListNode(4), ListNode(3)
b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
result = Solution()
result.addTwoNumbers(a, b)
print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))
