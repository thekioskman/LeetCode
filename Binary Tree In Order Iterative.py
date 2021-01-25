class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(6)
root.left.right = TreeNode(11)
root.right.right = TreeNode(5)
root.right.left = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(8)

def in_order(root):
  #check based cases
  if(not(root)):
    return(None)



  curr_node = root
  return_list = []
  q = []
  while(True):
    if(curr_node):
      q.insert(0,curr_node)
      curr_node = curr_node.left
      continue
    else:
      if(not(q)):
        break
      else:
        #go to memory 
        return_node = q.pop(0)
        return_list.append(return_node.val)
        #do not update curr_node unless it is to a right node, since all the left ones are in memory

        if return_node.right:
          curr_node = return_node.right
        else:
          continue


  return(return_list)
