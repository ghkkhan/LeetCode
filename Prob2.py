# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getllValue(self, li):
        num = 0
        ind = 1
        while li != None:
            num += li.val * ind
            ind *= 10
            li = li.next
        return num
    def generatell(self, s):
        li = None
        pli = None

        for i in range(len(s)):
            li = ListNode()
            li.val= int(s[i])
            li.next = pli
            pli = li
        
        return li
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.getllValue(l1)
        num2 = self.getllValue(l2)
        num3 = num1 + num2
        return(self.generatell(str(num3)))