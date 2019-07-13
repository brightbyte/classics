import random

class Node:
    
    def __init__( self, value, nextv ):
        self.value = value
        self.nextv = nextv
        
    def __str__( self ):
        return "%s" % self.value
        
    def hight( self ):
        return len( self.nextv )
    
    def locate( self, value, h = None ):
        if h is None:
            h = self.hight() -1
            
        if value == self.value:
            return self
        elif value < self.value:
            return None
        else:
            while h >= 0:
                n = self.nextv[h]
                
                if n is None:
                    h -= 1
                    continue
                    
                m = n.locate( value, h )

                if m is not None:
                    return m

                h -= 1
            
        return self
    

class List:
    
    def __init__( self, maxh ):
        self.maxh = maxh
        
        nextv = [ None for n in range( 0, maxh ) ]
        self.anchor = Node( None, nextv )
        
    def contains( self, value ):
        n = self.anchor.locate( value )
        return n.value == value
     
    def add( self, value ):
        n = self.anchor.locate( value )

        if n.value == value:
            return
        
        nextv = self._newNextVect()
        node = Node( value, nextv )

        h = len( nextv ) -1
        
        while h >= 0:
            nextv[h] = n.nextv[h]
            
            if n.nextv[h] is None or n.nextv[h].value > value:
                n.nextv[h] = node
            
            h -= 1
    
    def _newNextVect( self ):
        bits = random.getrandbits(self.maxh)
        mask = 0x1
        h = 1
        while h < self.maxh:
            if mask & bits:
                break
                
            h += 1
            mask = mask << 1
        
        nextv = [ None for n in range( 0, h ) ]
        return nextv
       
    def count( self ):
        n = self.anchor
        c = -1
        while n is not None:
            n = n.nextv[0]
            c += 1
            
        return c
       
    def dump( self ):
        n = self.anchor
        
        while n is not None:
            self.dumpNode( n )
            n = n.nextv[0]
        
    def dumpNode( self, node ):
        s = "%s" % node.value if node.value else "-/-"
        s = s.ljust( 12 )
        
        for n in node.nextv:
            ns = ">%s" % n.value if n else "*"
            s += ns.ljust( 12 )
            
        print s
        
list = List( 4 )
list.dump()
print

list.add( "F" )
print list.count()
list.dump()
print

list.add( "X" )
print list.count()
list.dump()
print

list.add( "A" )
print list.count()
list.dump()
print
