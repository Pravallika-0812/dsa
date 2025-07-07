class Node:
  def __init__(self, data):
    self.data=data
    self.next=None
    stack = []
    stack.extend([10,"hello",7,9,"hi"]) # Integer
    stack.append(3)
    print("Stacked Element is:", stack) 
    top = stack[-1] # peek
    print("top Element is:", top) 
    popped=stack.pop()
    print("popped Element is:", popped) 
    
n=Node(1)