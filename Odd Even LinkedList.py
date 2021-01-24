class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def odd_even_ll(head):
  '''
  head: ListNode
  return ListNode
  '''
  #based case
  if(not(head)):
    return(None) 
  elif(not(head.next)):
    return(head) 


  curr_node = head.next.next
  odd_head = head
  even_head = head.next

  curr_even = even_head
  curr_odd = odd_head


  counter = 1

  while(curr_node):
    if(counter % 2 == 0):
      curr_even.next = curr_node
      curr_even = curr_even.next

    else:
      curr_odd.next = curr_node
      curr_odd = curr_odd.next


    counter +=1
    curr_node = curr_node.next

  #remove the last trailing node, and link them
  curr_odd.next = even_head
  curr_even.next = None

  return odd_head
