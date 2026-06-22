myset = {'book','pen','suun','moon','mountain',4,True,True} # set does not have order, duplicate item will be ignored, unchangable   
print(myset)

myset.add(False)
print(myset)

newset= {3,5,6}
myset.update(newset)
myset.remove("suun") # other methods clear() discard() pop()
print(myset)

set1 = myset.union(newset) # give the union of two sets or use set3 = set1 | set2
