# a ring buffer

class Buffer:
	cap = 4
	data = [ None, None, None, None  ]
	top = 0
	bottom = 0

	def limit( self ):
		return self.cap -1

	def size( self ):
		if self.top >= self.bottom:
			return self.top - self.bottom
		else:
			return self.cap - self.bottom + self.top 
	
	def add( self, v ):
		if self.size() >= self.limit():
			raise Exception( "full" )
		else:
			self.data[self.top] = v
			self.top = ( self.top + 1 ) % self.cap

	def pop( self ):
		if self.size() == 0:
			raise Exception( "empty" )
		else:
			v = self.data[ self.bottom ]
			self.bottom = ( self.bottom + 1 ) % self.cap
			return v
			
	def show( self ):
		print( "data", self.data )
		print( "state", self.bottom, self.top )
		print( "size:", self.size() )
				

b = Buffer()

b.add( 'A' )
b.add( 'B' )

print( b.pop() )

b.add( 'C' )
b.add( 'D' )

print( b.pop() )
print( b.pop() )
print( b.pop() )

b.add( 'E' )
b.add( 'F' )
b.add( 'G' )

print( b.pop() )
print( b.pop() )

b.add( 'H' )
b.add( 'I' )

print( b.pop() )
print( b.pop() )
print( b.pop() )
