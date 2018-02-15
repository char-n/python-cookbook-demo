#!usr/bin/env python
# encoding: utf-8
# @Author : niuzhifa 1944044667@qq.com
# @Time : 2018/2/15 11:12

# 1.4 查找最大或最小的 N 个元素
nums = [10, 2, 3, 5, 9, 4, 6]
# 情况一: 当N=1的时候,使用max,min方法比较快
print(max(nums))
print(min(nums))

# 情况二: 当N大于1,并且个数相对较小的时候,使用heapq比较快
import heapq

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

#### 底层原理 #####
'''
堆数据结构最重要的特征是 heap[0] 永远是最小的元素。并且剩余的元素可以很
容易的通过调用 heapq.heappop() 方法得到，该方法会先将第一个元素弹出来，然后
用下一个最小的元素来取代被弹出元素（这种操作时间复杂度仅仅是 O(log N)，N 是
堆大小）
'''

# heap = list(nums)
heapq.heapify(nums)
print(nums)

# 查找最小的三个元素
# print(heapq.heappop(nums))
# print(heapq.heappop(nums))
# print(heapq.heappop(nums))

# 情况三: 当N的大小和集合的大小接近的时候,先排序集合然后切片会比较快.
sort_num = sorted(nums)
print(sort_num)
print(sort_num[:6])
print(sort_num[-6:])

# 扩展:堆数据结构排序
