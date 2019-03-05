# the classic

hight = 9;

stacks = {
	"A": [ n+1 for n in range( hight )[::-1] ],
	"B": [],
	"C": []
}

def die( msg ):
	print( msg )
	exit( 23 )

def showAllStacks():
	showStack( "A", stacks["A"] )
	showStack( "B", stacks["B"] )
	showStack( "C", stacks["C"] )
	
def showStack( name, a ):
	print( name + ":", "".join( [ "%i" % n for n in a ] ).ljust( hight, "-" ) )
	
def moveDisk( idx, srcName, dstName, tmpName ):
	incarnation = "moveDisk( %s@%i -> %s via %s )" % ( srcName, idx, dstName, tmpName )
	
	src = stacks[srcName]
	dst = stacks[dstName]
	tmp = stacks[tmpName]

	tmpLen = len( tmp )

	if ( idx < 0 ):
		die( "during %s: bad index: %i" % ( incarnation, idx ) )

	if ( idx+1 > len( src ) ):
		die( "during %s: bad index: %i > %i"
			% ( incarnation, idx+1, len( src ) ) )

	if ( idx+1 < len( src ) ):
		print( "during %s: Move disk %s@%i to temp stack %s..." 
			% ( incarnation, srcName, idx+1, tmpName ) )
		moveDisk( idx +1, srcName, tmpName, dstName )
	
	srcTop = src.pop( idx )
	dstLen = len( dst )

	if dstLen > 0:
		dstTop = dst[ len( dst ) - 1 ]
		
		if ( srcTop > dstTop ):
			die( "during %s: bad oder: %i > %i"
				% ( incarnation, srcTop, dstTop ) )
		
	dst.append( srcTop )
	
	print( "moved %s:" % incarnation )
	showAllStacks()
	print( "" )
	
	if ( len( tmp ) > tmpLen ):
		print( "during %s: Move tmp stack at %s@%i to %s..." 
			% ( incarnation, tmpName, tmpLen, dstName ) )
		moveDisk( tmpLen, tmpName, dstName, srcName )

print( "Start:" )
showAllStacks()
print( "" )

moveDisk( 0, "A", "B", "C" )

print( "Done:" )
showAllStacks()
print( "" )
