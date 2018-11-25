li=[1,32,4,6]
ki=[0,8,9,8]
vi=[0,0,0,0]
for i in range(0,len(li)):
 for j in range(0,len(ki)):
    if i == j :
      vi[i]= li[i]+ki[j]
   
print(vi)
