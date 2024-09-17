# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getkth(cur,k):
    count=0
    while cur and count!=k-1:
        count+=1
        cur=cur.next
    return cur if count==k-1 else None
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length=1
        tail=head
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        if k==0:
            return head
        cur=getkth(head,length-k)
        tail.next=head
        head=cur.next
        cur.next=None
        return head



