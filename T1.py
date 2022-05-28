
import doctest
def length(a):
    """>>> length("hello")
5
>>> length("aaa")
3
>>> length("asdfghj")
7
>>>"""   
    count=0
    for i in a:
        count=count+1
    return count
if __name__=="__main__":
    doctest.testmod()
