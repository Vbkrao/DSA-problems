
class Node:
    def __init__(self, data=0, next=None, down=None):
        self.data = data
        self.next = next
        self.down = down
     
def mergeTwoLists(head1, head2):
    temp1 = head1
    temp2 = head2
    dummy = Node()
    cur = dummy

    while temp1 and temp2:
        if temp1.data <= temp2.data:
            cur.down = temp1
            cur = cur.down
            temp1 = temp1.down
        else:
            cur.down = temp2
            cur = cur.down
            temp2 = temp2.down

    if temp1:
        cur.down = temp1
    else:
        cur.down = temp2

    return dummy.down
    
class solution:
    def flattenLL(self, Node, head):
        #Write your code here...
        temp1 = head
        temp2 = temp1.next
    
        if not temp2:
            return head
    
        next_node = None
    
        while temp1 and temp2:
            next_node = temp2.next
            temp1 = mergeTwoLists(temp1, temp2)
            temp2 = next_node
    
        return temp1
        
