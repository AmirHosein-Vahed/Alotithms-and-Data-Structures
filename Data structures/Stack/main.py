from Stack import Stack

s = Stack()
print(s.is_empty())
s.push(12)
s.push(13)
s.push(14)
print(s)
top = s.pop()
print(top)
print(s)
top = s.peek()
print(top)
print(s)
print(s.is_empty())