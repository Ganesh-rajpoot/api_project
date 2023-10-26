class Node:

  def __init__(self,value):
    self.data = value
    self.next = None
class Stack:

  def __init__(self):
    self.top = None

  def push(self, value):

    new_node = Node(value)

    new_node.next = self.top

    self.top = new_node

  def pop(self):

    if self.top is None:
      return "Stack Empty"
    else:
      data = self.top.data
      self.top = self.top.next
      return data

  def is_empty(self):
    return self.top == None

  def peek(self):

    if self.top is None:
      return "Stack Empty"
    else:
      return self.top.data

  def traverse(self):

    temp = self.top

    while temp is not None:
      print(temp.data,end=' ')
      temp = temp.next

  def size(self):

    temp = self.top
    counter = 0

    while temp is not None:
      temp = temp.next
      counter+=1

    return counter



def balance_brackets(text):
    s  = Stack()
    for i in text:
        if i in ['(','{','[']:
            s.push(i)
        elif i in ['}',')',']']:
            if not s:
               return "Not Balanced"
            if (s.peek() == '{' and i == '}') or (s.peek() == '(' and i == ')') or (s.peek() == '[' and i == ']'):
                s.pop()
            else:
               return "nottt Balanced"
        else:
           return "No Balancedd"
        
    if (s.is_empty()):
        return "Balanced"
    else:
        return "Not ffBalanced"
    

a = ['[','(','[',']',')',']']     
print(balance_brackets(a))
