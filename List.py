# difference between list and array is that list contain value different datatype other hand array contain same datatype value

# create list
list=[1,"q",["a","c"]]
print(type(list))
test=["a","b"]
print(type(test))
# list position define as array first position 0 and last position length-1
list1=["a","b","c"]
print(list1.__len__())
#concate list
list2=["a","b"]
list3=["x","y"]
print(list2 + list3)
# another way to concate list 
print(3*list3 + list2)

# list slice 
testList=list1 + list3 + ["z"]
# [:] is the slice operator for python
print(testList[2:6])
# this is slice from position 2  to end
print(testList[2:])

# this is slice from position start  to position 4
print(testList[:4])



