import doctest
def add(a,b):
    
    """>>> add(2,3)
5
>>> add(0,3)
3
>>> add(2,2)
4
>>>"""
    return a+b
if __name__=="__main__":
    doctest.testmod()
