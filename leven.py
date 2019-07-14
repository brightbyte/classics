import sys

def dist( t, p ):
	pz = len(p) +1
	
	m = [ 0 ] * pz
	
	for i in range( 0, len( t )+1 ):
		n = [ 0 ] * pz
		tch = t[i-1] if i > 0 else ''
		
		for j in range( 0, pz ):
			pch = p[j-1] if j > 0 else ''
			
			v = 10000
			
			if i == 0 and j == 0:
				v = 0
				
			if i > 0:
				v = min( v, m[j] +1 )

			if j > 0:
				v = min( v, n[j-1] +1 )

			if i > 0 and j > 0:
				if pch == tch:
					v = min( v, m[j-1] )
				else:
					v = min( v, m[j-1] +1 )
				
			n[j] = v
		
			print "\t[%i, %i] `%s`, `%s` -> %s" % ( i, j, tch, pch, n[j] )
		
		m = n
		
	return m[ pz-1 ]

if __name__ == '__main__':
	print dist( sys.argv[1], sys.argv[2] )
