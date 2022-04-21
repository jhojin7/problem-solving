'''
https://leetcode.com/submissions/detail/678399207/
'''
import collections
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        # ##### using heapq
        # frequent = collections.Counter(nums)
        # freq_heap = []
        # for num in frequent:
        #     # use negative count as key for minheap
        #     heapq.heappush(freq_heap,(-frequent[num],num))
        # # print(freq_heap)
        # ret = []
        # for num in range(k):
        #     ret.append(heapq.heappop(freq_heap)[1])
        # return ret

        #### pythonic
        freq = zip(*collections\
            .Counter(nums).most_common(k))
        # print(list(freq))
        return list(list(freq)[0])



# nums = [1,1,1,2,2,3]
# k = 2
# nums = [1]
# k = 1
nums = [1,2]
k = 2
sol = Solution.topKFrequent(Solution,nums,k)
print(sol)