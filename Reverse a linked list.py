def reverse_iterative(self):
  prev = None 
  cur = self.head
  while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur 
    cur = nxt 
  self.head = prev

def reverse_recursive(self):

  def _reverse_recursive(cur, prev):
    if not cur:
      return prev

    nxt = cur.next
    cur.next = prev
    prev = cur 
    cur = nxt 
    return _reverse_recursive(cur, prev)

  self.head = _reverse_recursive(cur=self.head, prev=None)