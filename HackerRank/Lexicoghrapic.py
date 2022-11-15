# Not run here but its perfect in test



if __name__ =='__main__':
    x = int(input())
    
    y = int(input())
    z = int(input())

    n = int(input())
    
    x1 = [ p for p in range(x+1)]
    y1 = [ q for q in range(y+1)]
    z1 = [ r for r in range(z+1)]
    
    perm = [[i,j,k]for i in x1 for j in y1 for k in z1]
    
    req =[h  for h in perm if sum(h)!=n]
    print(req)