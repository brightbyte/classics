import sys

def match( t, p ):
	pz = len(p) +1
	
	m = [ False ] * pz
	
	for i in range( 0, len( t )+1 ):
		n = [ False ] * pz
		tch = t[i-1] if i > 0 else ''
		
		for j in range( 0, pz ):
			pch = p[j-1] if j > 0 else ''
			
			if i == 0 and j == 0:
				n[j] = True
			elif ( pch == '*' ):
				n[j] = ( j>0 and n[j-1] ) or ( m[j] )
			elif ( pch == '?' or tch == pch ):
				n[j] = ( j>0 and m[j-1] )
		
			# print "\t[%i, %i] `%s`, `%s` -> %s" % ( i, j, tch, pch, n[j] )
		
		m = n
		
	return m[ pz-1 ]

if __name__ == '__main__':
	if match( sys.argv[1], sys.argv[2] ):
		print "YES"
	else:
		print "NO"
		sys.exit( 1 )
