class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cnt = 1

        while head is not None:
            if cnt % 2 != 0:
                temp = head.val
                head.val = head.next.val
                head.next.val = temp
            if head.next is not None:
                head = head.next
                break
            cnt += 1

        return head

sol = Solution()
test = None
test = ListNode(4, test)
test = ListNode(3, test)
test = ListNode(2, test)
test = ListNode(1, test)

print(sol.swapPairs(test))
