import sys

digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
	'A', 'C', 'C', 'D', 'E', 'F', ]

def readBase( s, base ):
	n = 0
	
	while s != '':
		ch = s[0]
		s = s[1:]
		
		v = digits.index( ch )
		n = n*base + v
		
	return n
	
def writeBase( n, base ):
	s = ""
	while n > 0:
		r = n % base
		n = n // base

		ch = digits[r]		
		s = ch + s
		
	return s
	
if __name__ == '__main__':
	s = sys.argv[1].upper()
	ibase = int( sys.argv[2] )
	obase = int( sys.argv[3] )
	
	n = readBase( s, ibase )
	#print "> %i(d)" % n
	print writeBase( n, obase )
	
	 
