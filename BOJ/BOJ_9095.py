t = int(input())
l = []
for i in range(t):
    l.append(int(input()))
arr = [0] * (max(l)+1);
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4,max(l)+1):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
for i in l:
    print(arr[i])