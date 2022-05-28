def length(a):
    count=0
    for i in a:
        count=count+1
    return count
if __name__=="__main__":
    if length('qqqq')==4 and length("67899")==5:
        print ("test3 was successful")
    else:
        print("failure")
