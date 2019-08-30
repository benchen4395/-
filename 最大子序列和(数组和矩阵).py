#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:13:35 2019

@author: chenben
"""

# 求一个数组的最大子序列和
def maxSubArray(nums):
    if len(nums)<2:
        return sum(nums)
    ans = nums[0]
    last = nums[0]
    for i in nums:
        last = max(0,last) + i
        ans = max(last,ans)
    return ans

testnums = [-2,1,-3,4,-1,2,1,-5,4]
ans = maxSubArray(testnums)
print(ans)

# 求一个矩阵的最大子矩阵和
def maxSubMatrix(mat):
    total = mat.copy()
    for i in range(1,len(mat)):
        for j in range(len(mat[0])):
            total[i][j] += total[i-1][j]
    ans = -float('inf')
    for i in range(1,len(mat)):
        for j in range(i,len(mat)):
            last = total[j][0]-total[i-1][0]
            for k in range(1,len(mat[0])):
                last = max(0,last)+total[j][k]-total[i-1][k]
                ans = max(last,ans)
    return ans
                

a = [[0,-2,-7,0],
     [9, 2,-6,2],
     [-4,1,-4,1],
     [-1,8,0,-2]]
print(maxSubMatrix(a))