#demonstrates 234 tree

class DataItem:

	def __init__(self, dd):	# special method to create objects
	# with instances customized to a specific initial state
		self.dData = dd # one piece of data

	def displayItem(self):	# format " /27"
		print ('/', self.dData)


class Node:
	_ORDER = 4
	def __init__(self):
		self._numItems = 0
		self._pParent = None
		self._childArray = []	# array of nodes
		self._itemArray = []	# array of data
		for j in range(self._ORDER):	# initialize arrays
			self._childArray.append(None)
		for k in range(self._ORDER - 1):
			self._itemArray.append(None)

	# connect child to this node
	def connectChild(self, childNum, pChild):
		self._childArray[childNum] = pChild
		if pChild:
			pChild._pParent = self

	# disconnect child from this node, return it
	def disconnectChild(self, childNum):
		pTempNode = self._childArray[childNum]
		self._childArray[childNum] = None
		return pTempNode

	def getChild(self, childNum):
		return self._childArray[childNum]

	def getParent(self):
		return self._pParent

	def isLeaf(self):
		return not self._childArray[0]

	def getNumItems(self):
		return self._numItems

	def getItem(self, index):	# get DataItem at index
		return self._itemArray[index]

	def isFull(self):
		return self._numItems==self._ORDER - 1

	def findItem(self, key):	# return index of
		for j in xrange(self._ORDER-1):	# item (within node)
			if not self._itemArray[j]:	# if found,
				break	# otherwise,
			elif self._itemArray[j].dData == key:	# return -1
				return j
		return -1

	def insertItem(self, pNewItem):
		# assumes node is not full
		self._numItems += 1 # will add new item
		newKey = pNewItem.dData	# key of new item

		for j in reversed(range(self._ORDER-1)):	# start on right,	# examine items
			if self._itemArray[j] == None:	# if item null,
				pass	                # go left one cell
			else:	#not null,
				itsKey = self._itemArray[j].dData	# get its key
				if newKey < itsKey:	                # if it's bigger
					self._itemArray[j+1] = self._itemArray[j]	# shift it right
				else:
					self._itemArray[j+1] = pNewItem	# insert new item
					return j+1                      # return index to new item
			# end else (not null)
		# end for 	# shifted all items,
		self._itemArray[0] = pNewItem	# insert new item
		return 0
	# end insertItem()

	def removeItem(self):	# remove largest item
		# assumes node not empty
		pTemp = self._itemArray[self._numItems-1]	# save item
		self._itemArray[self._numItems-1] = None	# disconnect it
		self._numItems -= 1                             # one less item
		return pTemp                                    # return item

	def displayNode(self):	#format "/24/56/74"
		for j in xrange(self._numItems):
			self._itemArray[j].displayItem()	#format "/56"
		print ('/')	#final "/"



class Tree234:
	def __init__(self):
		self._pRoot = Node()	# root node

	def find(self, key):
		pCurNode = self._pRoot	# start at root
		while True:
			childNumber=pCurNode.findItem(key)
			if childNumber != -1:
				return childNumber	# found it
			elif pCurNode.isLeaf():
				return -1               # can't find it
			else:	                        # search deeper
				pCurNode = self.getNextChild(pCurNode, key)
		

	def insert(self, dValue):	# insert a DataItem
		pCurNode = self._pRoot
		pTempItem = DataItem(dValue)

		while True:
			if pCurNode.isFull():	# if node full,
				self._split(pCurNode)	# split it
				pCurNode = pCurNode.getParent()	# back up
					# search once
				pCurNode = self.getNextChild(pCurNode, dValue)
			# end if(node is full)

			elif pCurNode.isLeaf():	# if node is leaf,
				break	# go insert
			# node is not full, not a leaf; so go to lower level
			else:
				pCurNode = self.getNextChild(pCurNode, dValue)
		# end while
		pCurNode.insertItem(pTempItem)	# insert new item

	def _split(self, pThisNode):	# split the node
		# assumes node is full
		
		pItemC = pThisNode.removeItem()	        # remove items from
		pItemB = pThisNode.removeItem()	        # this node
		pChild2 = pThisNode.disconnectChild(2)	# remove children
		pChild3 = pThisNode.disconnectChild(3)	# from this node

		pNewRight = Node()	# make new node

		if pThisNode == self._pRoot:	# if this is the root,
			self._pRoot = Node()	# make new root
			pParent = self._pRoot	# root is our parent
			self._pRoot.connectChild(0, pThisNode)	# connect to parent
		else:	#this node not the root
			pParent = pThisNode.getParent()	# get parent

		# deal with parent
		itemIndex = pParent.insertItem(pItemB)	# item B to parent
		n = pParent.getNumItems()	# total items?

		j = n-1                 # move parent's
		while j > itemIndex:	# connections
			pTemp = pParent.disconnectChild(j)	# one child
			pParent.connectChild(j+1, pTemp)	# to the right
			j -= 1
				# connect newRight to parent
		pParent.connectChild(itemIndex+1, pNewRight)

		# deal with newRight
		pNewRight.insertItem(pItemC)	        # item C to newRight
		pNewRight.connectChild(0, pChild2)	# connect to 0 and 1
		pNewRight.connectChild(1, pChild3)	# on newRight

	# gets appropriate child of node during search of value
	def getNextChild(self, pNode, theValue):
		# assumes node is not empty, not full, not a leaf
		numItems = pNode.getNumItems()
		
		for j in range(numItems):	# for each item in node
			if theValue < pNode.getItem(j).dData:	# are we less?
				return pNode.getChild(j)	# return left child
		else:	# end for 	# we're greater, so
			return pNode.getChild(j + 1)	# return right child

	def displayTree(self):
		self.recDisplayTree(self._pRoot, 0, 0)

	def recDisplayTree(self, pThisNode, level, childNumber):
		print ('level=', level, 'child=', childNumber,)
		pThisNode.displayNode()	# display this node

		# call ourselves for each child of this node
		numItems = pThisNode.getNumItems()
		for j in xrange(numItems+1):
			pNextNode = pThisNode.getChild(j)
			if pNextNode:
				self.recDisplayTree(pNextNode, level+1, j)
			else:
				return
	



# Testing..............

pTree = Tree234()
pTree.insert(50)
pTree.insert(40)
pTree.insert(60)
pTree.insert(30)
pTree.insert(70)

# as Python doesn't support switch, simulating the same with dictionary and functions
def show():
	pTree.displayTree()

def insert():
	value = int(raw_input('Enter value to insert: '))
	pTree.insert(value)

def find():
	value = int(raw_input('Enter value to find: '))
	found = pTree.find(value)
	if found != -1:
		print ('Found', value)
	else:
		print( 'Could not find', value)

case = { 's' : show,
	'i' : insert,
	'f' : find}
#switch simulation completed

while True:
	print
	choice = input('Enter first letter of show, insert, or find: ')
	if case.get(choice, None):
		case[choice]()
	else:
		print ('Invalid entry')
		
del pTree

