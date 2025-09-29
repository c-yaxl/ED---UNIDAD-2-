class Stack:
  def __init__(self):
    self.stack = []

  def agregar(self, element):
    self.stack.append(element)

  def eliminar(self):
    if self.existencia():
      return "Stack is empty"
    return self.stack.pop()

  def ver(self):
    if self.existencia():
      return "Stack is empty"
    return self.stack[-1]

  def existencia(self):
    return len(self.stack) == 0

  def tamano(self):
    return len(self.stack)
  
myStack = Stack()

myStack.agregar('A')
myStack.agregar('B')
myStack.agregar('C')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.eliminar())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.ver())
print("isEmpty: ", myStack.existencia())
print("Size: ", myStack.tamano())

