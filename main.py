import sys
input = sys.stdin.readline
n1,n2 = map(int,input().split(' '))
ls = []
ls = list(map(int,input().rstrip().split(' ')))
mx = 0
for i in range(n1):
  for j in range(i+1,n1):
    for k in range(j+1,n1):
      if mx < ls[i]+ls[j]+ls[k] and ls[i]+ls[j]+ls[k] <= n2:
        mx = ls[i]+ls[j]+ls[k]
print(mx)
