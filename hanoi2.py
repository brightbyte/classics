# the classic

def move( tpl ):
	( src, dst ) = tpl
	print( "move", src, dst )
	return ( src, dst ) if len( src ) == 0 else move( ( move( ( src[1:], [] ) )[1], dst + src[:1] ) )

src = [ 5, 4, 3, 2, 1 ]
dst = []

( src, dst ) = move( ( src, dst ) )
print( "result", src, dst )



