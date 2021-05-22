arr =  list(enumerate(map(int , input().split(', '))))
arr = [v for k,v in enumerate(arr) if not v[1] & 1]
print( [k[0] for k in arr])

   

