cmp1 = 5 + 3j
cmp2 = 6 - 5j
print(cmp1+cmp2)
print(cmp1-cmp2)
print(cmp1*cmp2)
print(cmp1/cmp2)
print(cmp1**cmp2)

#Boolean consists of true and false.Where true=1,false=0
a=1
b=5
print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
x=True
print(type(x))
print(type(True))

#Sequences-list,tuple,Strings,range

#list-collection of heterogenous  elements which are indexable.list should be given in the square brackets[].
#list is Mutable:change is allowed
#list is slower than Tuple
temp=[[1,2,3],"saranya",5,-1,0.7,True,False,[1,3,9]]
print(type(temp))
print(len(temp))
print(temp[3])#index
print(temp[6])
print(temp[-4])#negative indexing in list
print(temp[0:7])#slicing
print(temp[-4:-2])
print(temp[2:7:2])#step
print(temp[-7:-1:2])
print(temp[-2:-7:-1])#-1 in step. it print the list reverse direction.
print(temp[7][1])#indexing in list of list.
temp[3]=3 #adding new element in the list by using index number in that index position.
print(temp)
#[[1, 2, 3], 'saranya', 5, 3, 0.7, True, False, [1, 3, 9]]

#Tuple-collection of heterogenous  elements which are indexable.list should be given in the curely brackets().
#Tuple is Immutable:change is not allowed.
#tuple is faster than list.
c=(1,2,True,3,4,"saranya",(2,3),7,False)
print(type(c))
print(len(c))
print(c[3])#index
print(c[6])
print(c[-4])#negative indexing in tuple
print(c[0:7])#slicing
print(c[-4:-2])


tup1 = (1, 2, True, "Str1", 0.9)
tup1 = (1, 3)
print(tup1[1])
#tup1[1] = 5

#Range
print(list(range(0,100)))
print(list(range(0,100,-1)))
print(list(range(100,0,-1)))
print(list(range(0,100,3)))
print(list(range(0,100,10)))