# deque class in python

# python has a default implementation of deque class in the collection module.
# so, we have to first import deque from collections.
from collections import deque

# initializing an object of Deque class.
my_deck = deque()

# appending elements to deque.
# we can append element both to the front and the end of the deque.
# apppending element to the front.
my_deck.appendleft("python")
my_deck.appendleft("java")
my_deck.appendleft("php")
print(my_deck)
# appending element to the end
my_deck.append("c")
my_deck.append("swift")
my_deck.append("ruby")
my_deck.append("powershell")
print(my_deck)

# deleting element from deque
# we can use delete element both from the front and the end of the deque.
# deleting element from front.
my_deck.popleft()
# deleting element from end.
my_deck.pop()
# we can also use remove() to delete elements using name.
my_deck.remove("java")
print(my_deck)
# we can also clear all the elements from the deque using clear() method.
#my_deck.clear()

# we can access elements in the deque just like list.
# first element
print(my_deck[0])
# last element
print(my_deck[-1])
# any arbitary element
print(my_deck[1])

# modifying arbitary element
my_deck[1]="c++"
print(my_deck)

# printing the lenth of the deque.
print(len(my_deck))

# we can count number of specific elements using count() function.
print(my_deck.count("python"))

# we can circularly shift the elements rightward by n index using rotate() function.
my_deck.rotate(2)
print(my_deck)
