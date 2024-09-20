# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def getKth(cur, k):
    count = 0
    while cur and count != k - 1:
        count += 1
        cur = cur.next
    
    if count == k - 1:
        return cur
    else:
        return None

def reverse(head):
    back = None
    cur = head
    front = None
    
    while cur:
        front = cur.next
        cur.next = back
        back = cur
        cur = front
    
    return back
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            kth = getKth(cur, k)
            
            if kth:
                next = kth.next
                kth.next = None
                reverse(cur)
                
                if cur == head:
                    head = kth
                else:
                    prev.next = kth
                
                prev = cur
                cur = next
            else:
                if prev:
                    prev.next = cur
                    break

                prev = cur
                cur = next
        
        return head
            