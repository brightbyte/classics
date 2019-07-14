import sys

def knap( total, packets ):
	packets = sorted( packets, key = lambda p: p[1] )
	table = [ [ 0 ] * ( total+1 ) ]
	
	for p in packets:
		v = int( p[0] )
		w = int( p[1] )
		
		r = [ 0 ] * ( total+1 )
		
		for i in range( 0, total +1 ):
			bestWithout = table[-1][i]
			if i < w:
				# copy from above
				r[i] = bestWithout
			else:
				remain = i - w
				bestRemain = table[-1][remain]
				#print "taking %i:%i, remain %i, best %i" % ( v, w, remain, bestRemain )
				r[i] = max( bestWithout, bestRemain + v )
		
		table.append( r )
		print v, w, r
		
	selected = []
	i = total
	for j in range( len( table ) -1, 0, -1 ):
		if table[j][i] > table[j-1][i]:
			p = packets[j-1] # j-1 because of the extra zero row in tables
			selected.append( p ) 
			i -= int( p[1] )
	
	return selected
		
		
if __name__ == '__main__':
	w = int( sys.argv[1] )
	p = [ s.split( ':' ) for s in sys.argv[2:] ]
	
	m = knap( w, p )
	print
	print m
