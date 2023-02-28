x, y, w, h = map(int,input().split())
row = min(w-x,x)
col = min(h-y,y)
print(min(row,col))