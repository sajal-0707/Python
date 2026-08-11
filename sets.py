# s={1,2,3,4,5}
# s.add(6)
# print(s)
# s.update({7,8,9})
# s.remove(3)
# s.discard(4)
# s.pop()
# s.clear()
# print(s)
s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
print(s1 | s2) # s1.union(s2)
print(s1 & s2) # s1.intersection(s2)
print(s1 - s2) # s1.difference(s2)
print(s1.isdisjoint(s2))