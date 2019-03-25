
class Element:
	def __init__( self, value ):
		self.left = self;
		self.right = self;
		self.value = value;
		
	def remove( self ):
		if self.right == self:
			return # list is empty
		else:
			v = self.right
			self.right.right.left = self
			self.right = self.right.right
			return v
			
	def insert( self, elm ):
		elm.right = self.right
		elm.left = self
		
		self.right.left = elm
		self.right = elm
		
class List:
	def __init__( self ):
		self.root = Element( None )
		
	def add( self, value ):
		self.root.left.insert( Element( value ) )

	def push( self, value ):
		self.root.right.left.insert( Element( value ) )

	def pop( self ):
		v = self.root.remove()
		return v.value if v else None

	def take( self ):
		v = self.root.left.left.remove()
		return v.value if v else None

	def first( self ):
		return self.root.right.value

	def last( self ):
		return self.root.left.value
	
list = List()
print( list.first(), list.last() )
	
list.add( "A" );
print( list.first(), list.last() )
	
list.add( "B" );
print( list.first(), list.last() )
	
list.push( "X" );
print( list.first(), list.last() )

list.push( "Y" );
print( list.first(), list.last() )
	
v = list.pop();
print( v, list.first(), list.last() )
	
v = list.pop();
print( v, list.first(), list.last() )

v = list.take();
print( v, list.first(), list.last() )

v = list.take();
print( v, list.first(), list.last() )
