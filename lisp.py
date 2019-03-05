# the ultimate

from enum import Enum
from functools import reduce

class L( Enum ):
	t = 0
	quote = 1
	lst = 2
	car = 11
	cdr = 12
	cons = 21
	cond = 31
	eq = 32
	atom = 33
	lda = 41
	label = 51
	defun = 52
	
	add = 101
	sub = 102
	mul = 103
	div = 104

	lt = 111
	gt = 112
	
	a = 1001
	b = 1002
	c = 1003
	d = 1004
	e = 1005
	f = 1006
	g = 1007
	h = 1008
	i = 1009
	j = 1010

	v = 2001
	w = 2002
	x = 2003
	y = 2004
	z = 2005

	def __str__( self ):
		return self.name
	
	__repr__ = __str__

class Ref:
	def __init__( self, name ):
		self.name = name
		self.value = None

	def __str__( self ):
		return "<<%s?>>" if self.value is None else "<<%s>>" % ( self.name )
	
	__repr__ = __str__

	def __eq__( self, other ):
		return self.value == other.value

	def __hash__( self ):
		raise Exception( "Ref is not hashable" )

class Sym:
	def __init__( self, name ):
		self.name = name

	def __str__( self ):
		return "%s" % self.name
		
	__repr__ = __str__

	def __eq__( self, other ):
		return self.name == other.name

	def __hash__( self ):
		return hash( self.name )

names = {}
lvl = 0

def incarnate( expr, bindings ):
	if ( type( expr ) is Ref ): # don't dive
		return expr

	if type( expr ) is list:
		return list( map( (lambda e: incarnate( e, bindings ) ) , expr ) )
	elif type( expr ) is tuple:
		return tuple( map( (lambda e: incarnate( e, bindings ) ) , expr ) )
	else:
		return bindings[expr] if expr in bindings else expr

def bind( expr, bindings ):
	if type( expr ) is Ref:
		if expr.name in bindings:
			expr.value = bindings[expr.name]
		else:
			raise Exception( "Unbound reference", expr.name )
		
	if type( expr ) is list or type( expr ) is tuple:
		for e in expr:
			bind( e, bindings )

def levall( exprs, quote = False ):
	result = map( (lambda e: leval( e )), exprs )
	
	if quote:
		result = map( (lambda e: ( L.quote, e )), result )
	
	return result

def leval( expr ):
	global lvl
	print( "leval".rjust( lvl*4 + 5 ), expr )
	lvl += 1
	
	try:
		if type( expr ) is list:
			expr = ( L.quote, tuple( expr ) )
		
		if not type( expr ) is tuple:
			return expr
		if not len( expr ):
			return expr
		
		head = expr[0]
		tail = expr[1:]
		
		if ( type( head ) is Ref ): # dereference
			head = head.value

		if ( type( head ) is str or type( head ) is Sym  ):
			if head in names:
				head = names[head]
			else:
				raise Exception( "Unbound name", head )
		
		if ( head == L.quote ):
			return tail[0]
		elif ( head == L.lst ):
			return tuple( levall( tail ) )
		elif ( head == L.atom ):
			v = leval( tail[0] )
			return L.t if type( v ) is not tuple or len( v ) == 0 else []
		elif ( head == L.car ):
			return leval( tail[0] )
		elif ( head == L.cdr ):
			v = leval( tail[0] )
			return tuple( v )[1:]
		elif ( head == L.cons ):
			return ( leval( tail[0] ), ) + tuple( levall( tail[1] ) )
		elif ( head == L.cond ):
			for x in tail:
				if leval( x[0] ) == L.t:
					return leval( x[1] )
			return []
		elif ( head == L.eq ):
			v = leval( tail[0] )
			w = leval( tail[1] )
			return L.t if v == w else []
		elif ( head == L.lt ):
			v = leval( tail[0] )
			w = leval( tail[1] )
			return L.t if v < w else []
		elif ( head == L.gt ):
			v = leval( tail[0] )
			w = leval( tail[1] )
			return L.t if v > w else []
		elif ( head == L.add ):
			return reduce( (lambda x, y: x + y ), levall( tail ) )
		elif ( head == L.sub ):
			return reduce( (lambda x, y: x - y ), levall( tail ) )
		elif ( head == L.mul ):
			return reduce( (lambda x, y: x * y ), levall( tail ) )
		elif ( head == L.div ):
			return reduce( (lambda x, y: x / y ), levall( tail ) )
		elif ( head == L.lda ): # anon lambda
			# tbd: assert lambda structure
			return expr
		elif ( head == L.label ): # lambda with label substitution
			name = leval( tail[0] )
			lda = leval( tail[1] )
			
			if not lda[0] == L.lda:
				raise Exception( "Lambda expected", lda )
			
			bind( lda[2], { name: lda } ) # magic!
			return lda
		elif ( head == L.defun ):  # lambda with label substitution and def
			name = leval( tail[0] )

			# tbd: assert lambda structure
			lda = ( L.lda, tail[1], tail[2] )
			
			bind( lda[2], { name: lda } ) # magic!
			names[name] = lda
			return lda
		elif ( type( head ) is tuple ): # if the head is lambda, it's a call
			if not head[0] == L.lda:
				raise Exception( "Lambda expected", head )
			symbols = head[1]
			params = levall( tail, quote = True ) # quote param values!
			bindings = dict( zip(symbols, params) )
			exp = incarnate( head[2], bindings )
			return leval( exp )
		elif ( callable( head ) ): # native call
			params = levall( tail, quote = True ) # quote param values!
			return head( *params )
		else:
			raise Exception( "Bad head type", type( head ), expr )
	finally:
		lvl -= 1

#cnt = Sym( "cnt" )
#print( leval( ( L.defun, cnt, ( L.x, ),
#				( L.cond,
#					[ (L.atom, L.x) , 0 ],
#					[ L.t, (L.add, 1, ( Ref( cnt ), (L.cdr, L.x) ) ) ]
#					) ) ) )

fib = Sym( "fib" )
print( leval( ( L.defun, fib, ( L.i, ),
				( L.cond,
					[ ( L.lt, L.i, 2 ), 1 ],
					[ L.t, (L.add,
							( Ref( fib ), (L.sub, L.i, 1 ) ),
							( Ref( fib ), (L.sub, L.i, 2 ) ) ) ]
					) ) ) )

print( leval( ( fib, 6 ) ) )

