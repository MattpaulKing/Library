from collections import Counter

c = Counter('insufferable')
print(c.elements())
# Prints the list of elements given to the counter + their frequency
print(c.most_common())
# Prints the most common element + its frquency (may print more than one element if they have the same frequency)

a = Counter(a=1, b=2, c=3, d=4)
mylist = ['a', 'b', 'c', 'd']
a.subtract(mylist) # counter value's frequency - parameter's frequency (mylist in this case)
print(a)
c.update(mylist) # adds mylist value's frequency to counter value's frequency
print(a) 

# Note counters don't show values <= 0
