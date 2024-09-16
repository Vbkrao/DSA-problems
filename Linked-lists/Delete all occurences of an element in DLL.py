def deleteAllOccurrences(self, head, val):
  cur=head
  while cur:
    if cur.data==val:
      if cur.prev:
        cur.prev.next=cur.next
      if cur.next:
        cur.next.prev=cur.prev
      if cur==head:
        head=cur.next
      cur=cur.next
    else:
      cur=cur.next
  return head
