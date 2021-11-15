def solve(n):
    if n <= 2:
        return n
    if n == 3:
        return 4
    return lst[n-1] + lst[n-2] + lst[n-3]
'''
1 => 1
2 => 1+1 2 = 2
3 => 1+1+1 1+2 2+1 3 = 4
4 => 1+1+1+1 2+1+1 1+2+1 1+1+2 2+2 3+1 1+3 = 7
5 => 1+1+1+1+1 2+1+1+1(*4) 3+1+1(*3) 2+2+1(*3) 3+2(*2) = 13
6 => 1+1+1+1+1+1 2+1+1+1+1(*5) 3+1+1+1(*4) 2+2+1+1(*6)
     3+2+1(*6) 2+2+2 3+3 = 24
'''
lst = [0] * 12
for i in range(1, 12):
    lst[i] = solve(i)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print(lst[n])