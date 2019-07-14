import sys

def pick( items, weight ):
	if weight < 1 or not items:
		return ( 0, items )
		
	it = items[-1]
	v = int( it[0] )
	w = int( it[1] )
	
	s = "for %i:%i @%i:" % ( v, w, weight )
	
	bestWithoutThis = pick( items[:-1], weight )
	
	#print "%s bestWithoutThis: %i" % ( s, bestWithoutThis[0] )
	
	if w < weight:
		r = weight - w
		bestBeforeThis = pick( items[:-1], r )
		#print "%s bestBeforeThis: %i @%i" % ( s, bestBeforeThis[0], r )

		bestWithThis = ( 
			v + bestBeforeThis[0],
			bestBeforeThis[1] + [ it ]
		)
	
		#print "%s bestWithThis: %i" % ( s, bestWithThis[0] )

		if bestWithThis[0] > bestWithoutThis[0]:
			print "%s pick %i:%i" % ( s, v, w ) 
			return bestWithThis

	print "%s keep %i" % ( s, bestWithoutThis[0] )
	return bestWithoutThis		
		
if __name__ == '__main__':
	print "BROKEN!"
	w = int( sys.argv[1] )
	p = [ s.split( ':' ) for s in sys.argv[2:] ]
	
	m = pick( p, w )
	print
	print m
