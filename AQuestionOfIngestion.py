# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:33:11 2021

@author: thors
"""

#dp = [[2], [101],[20001]]
dp = [[]*2, []*101, []*20001]

vals = []*1000
energy_levels = []*20001

n, cap = map(int, input().split())

vals = [int(x) for x in input().split()]


c = cap
for i in range(0, cap):
    energy_levels[i] = c;
    c = c* 2/3
    if(c==0):
        break
    
    
levels = i

i = n-1
while(i>=0):
    for j in range(levels+1):
        cur_cap = energy_levels[j]
        eating_reward = min(cur_cap)
        level_if_rest = max(j-1, 0)
        dp[[0], [i], [j]] = max(dp[0][i+1][j+1] + eating_reward, dp[1][i+1][level_if_rest])
        dp[1][i][j] = max(dp[0][i+1][j+1] + eating_reward, dp[1][i+1][0])
    i=i-1
    
assert(dp[0][0][0] == dp[1][0][0])
print(dp[0][0][0])