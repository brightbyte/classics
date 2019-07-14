import sys

def median( x, y ):
	if len( x ) > len( y ):
		z = x
		x = y
		y = z
	
	i = 0
	j = len( x ) # why no -1?
	
	inf = float("inf")
	
	while i<=j:
		# invariant: px + py = ( len(x) + len(y) +1 ) / 2
		px = ( i+j ) // 2
		py = ( ( len(x) + len(y) +1 ) // 2 ) - px

		maxLeftX = x[px-1] if px > 0 else -inf
		minRightX = x[px] if px < len(x) else inf
		maxLeftY = y[py-1] if py > 0 else -inf
		minRightY = y[py] if py < len(y) else inf
		
		print
		print "%i..%i -> %i; %i" % ( i, j, px, py )
		print x[:px], "|", x[px:]
		print y[:py], "|", y[py:]
		print "%f|%f, %f|%f" % ( maxLeftX, minRightX, maxLeftY, minRightY )
		
		# raw_input( "step" )
		
		if ( maxLeftX <= minRightY and maxLeftY <= minRightX ):
			print "found"
			break;
		
		elif maxLeftX > minRightY:
			print "left"
			j = px # move left
		else:
			print "right"
			i = px +1 # move right (why +1?)
				
	if ( len(x) + len(y) ) % 2:
		# odd
		return max( maxLeftX, maxLeftY )
	else:
		# even, use average
		return ( max( maxLeftX, maxLeftY ) + min( minRightX, minRightY ) ) / 2.0
				
	return [ x[:px], y[:py], x[px:], y[py:]]
		
if __name__ == '__main__':
	a = [ int(s) for s in sys.argv[1].split( ',' ) ]
	b = [ int(s) for s in sys.argv[2].split( ',' ) ]
	
	m = median( a, b )
	print
	print "MEDIAN:", m
