n= int(raw_input())
list1 =  raw_input().split()
b= int(raw_input())
list2 = raw_input().split()
a = set(list1).union(list2)
print len(a)