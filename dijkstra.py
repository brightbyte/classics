import sys
from collections import deque

def readGraph():
	g = {}
	print "Input a graph as a sequence of edges"
	while True:
		s = raw_input()
		if s == "":
			break
		
		( a, b, w ) = s.strip().split( ',' )
		
		if not a in g:
			g[a] = []

		if not b in g:
			g[b] = []
			
		g[a].append( ( b, int( w ) ) )
		
	return g

def distance( g, v ):
	d = { v: 0 }
	
	if not v:
		return d
	
	m = deque( [ v ] )
	
	while m:
		w = m.popleft()
		dw = d[w]
		
		for ( u, z ) in g[w]:
			du = dw + z
			if not u in d or du < d[u]:
				d[u] = du
		
		children = [ ch[0] for ch in g[w] ]
		m.extend( children )
	
	return d

g = readGraph()
print g

v = sys.argv[1]
d = distance( g, v )
print d
