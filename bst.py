import random

class Node:
	def __init__(self, value):
		self.less = None
		self.more = None
		self.value = value
	
	def find(self, value):
		if value > self.value:
			return self.more if self.more else None
		elif value < self.value:
			return self.less if self.less else None
		else:
			return self
			
	def insert(self, value):
			
		if value < self.value:
			if not self.less:
				self.less = Node(value)
			else:
				self.less.insert( value )
		elif value > self.value:
			if not self.more:
				self.more = Node(value)
			else:
				self.more.insert( value )
		else:
			return
	
	def inorder(self, callback):
		if self.less:
			self.less.inorder(callback)
			
		callback(self)
		
		if self.more:
			self.more.inorder(callback)
			
	def preorder(self, callback):
		callback(self)
		if self.less:
			self.less.inorder(callback)
		if self.more:
			self.more.inorder(callback)
				
	def postorder(self, callback):
		if self.less:
			self.less.inorder(callback)
		if self.more:
			self.more.inorder(callback)
		callback(self)

	def bft(self, callback):
		queue = [ self ]

		while( queue ):
			n = queue.popleft()
			callback( n )
			
			if n.less:
				queue.add(n.less)
			
			if n.more:
				queue.add(n.more)
				
	def print(self, indent = '', prefix = ''):
		if self.less:
			self.less.print( indent + '  ', '/' )

		print( indent, prefix, self.value )

		if self.more:
			self.more.print( indent + '  ', '\\' )

rand = [random.randint(0, 100) for x in range(1, 100)]
rand = list( set( rand ) )
random.shuffle( rand)

root = Node(rand[50])

for r in rand:
	root.insert(r)

seq = []
root.inorder( lambda x: seq.append( x.value ) )

exp = sorted( rand )
difference = [i for i, j in zip(seq, exp) if i != j]

print( "DIFF", difference )
print( "SEQ", seq )
print( "EXP", exp )

for r in rand:
	if not root.find( r ):
		print( "NOT FOUND", r )


root.print()
