#!/usr/bin/env python

def shift(data, s):
    return data[s:] + data[:s]

#a = [1, 2, 3, 4, 5, 6]
#a = [ 1, 2, 2, 2, 2, 2, 6]
a = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]

for k in range(len(a)):
    tmp = shift(a, k)
    left = 0
    right = len(a) - 1
    print(tmp)
    if (tmp[left] < tmp[right]):
        ans = tmp[right]
    else:
        while left < right - 1:
            mid = (left + right) // 2
            if tmp[mid] < tmp[left]:
                right = mid
            else:
                left = mid
        print(left, right)
        ans = tmp[left]
    if (ans != 6):
        print("Fail", k, ans)
