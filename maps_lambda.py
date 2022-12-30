# using maps
def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return 'ODD'
names=['Andy', 'Sally', 'Eve'] 
x=list(map(splicer, names))  
print(x)