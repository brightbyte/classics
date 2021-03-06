import random

class Node:
	def __init__(self, value, parent = None):
		self.parent = parent
		self.less = None
		self.more = None
		self.value = value
	
	def new(self, value, parent = None):
		return Node(value, parent)
	
	def find(self, value):
		if value > self.value:
			return self.more.find(value) if self.more else None
		elif value < self.value:
			return self.less.find(value) if self.less else None
		else:
			return self

	def findSmallest(self):
		if self.less:
			return self.less.findSmallest()
		else:
			return self

	def findGreatest(self):
		if self.more:
			return self.more.findGreatest()
		else:
			return self
			
	def insert(self, value):
		if value < self.value:
			if not self.less:
				self.less = self.new(value, self)
				return self.less
			else:
				return self.less.insert( value )
		elif value > self.value:
			if not self.more:
				self.more = self.new(value, self)
				return self.more
			else:
				return self.more.insert( value )
		else:
			return None
			
	def become(self, other):
		self.value = other.value
		# TODO: copy all fields, except less and more and parent.
			
	def replace(self, child, replacement):
		if self.less == child:
			self.less = replacement
		if self.more == child:
			self.more = replacement
		
	def delete(self):
		if not self.more and self.parent:
			self.parent.replace(self, self.less)
			return self.parent
		elif not self.less and self.parent:
			self.parent.replace(self, self.more)
			return self.parent
		else:
			if self.more:
				replacement = self.more.findSmallest()
			elif self.less:
				replacement = self.less.findGreatest()
			
			if replacement:
				self.become( replacement )
				if replacement != self:
					return replacement.delete()
		return None

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
		print( indent, prefix, self.value )

		if self.less:
			self.less.print( indent + '  ', '>' )

		if self.more:
			self.more.print( indent + '  ', '<' )

def main( new = Node ):
	rand = [random.randint(0, 100) for x in range(1, 33)]
	rand = list( set( rand ) )
	random.shuffle( rand)

	root = new(rand[len(rand)//2])

	for r in rand:
		root.insert(r)

	root.print()

	seq = []
	root.inorder( lambda x: seq.append( x.value ) )

	exp = sorted( rand )
	difference = [i for i, j in zip(seq, exp) if i != j]

	print( "DIFF", difference )
	print( "SEQ", seq )
	print( "EXP", exp )

	for r in rand:
		n = root.find( r )
		if not n:
			print( "NOT FOUND", r )
		elif n.value != r:
			print( "FOUND WRONG NODE", n.value, "for", r )

	print( "MIN", root.findSmallest().value )
	print( "MAX", root.findGreatest().value )

	delete = [
		rand.pop(),
		rand.pop(),
		rand.pop(),
		rand.pop(),
		rand.pop(),
		rand.pop(),
		rand.pop(),
		rand.pop(),
		rand.pop(),
	]
	print( "DEL", delete )

	for d in delete:
		n = root.find( d )
		n.delete()

	root.print()

	for d in delete:
		if root.find( d ):
			print( "NOT DELETED", d )

	seq = []
	root.inorder( lambda x: seq.append( x.value ) )

	exp = sorted( rand )
	difference = [i for i, j in zip(seq, exp) if i != j]

	print( "DIFF", difference )
	print( "SEQ", seq )
	print( "EXP", exp )

	#root.print()

if __name__ == '__main__':
	main()
