coll_list = list(map(int ,input().split(', ')))
l = [ int(x) for x in coll_list  if int(x) is not 0]
z = [ int(z) for z in coll_list  if int(z) == 0]
print(l + z)

