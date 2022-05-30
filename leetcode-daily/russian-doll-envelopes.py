
class Solution:
    def maxEnvelopes(self, envelopes)->int:
        envelopes.sort()
        print(envelopes)
        if len(envelopes) == 1:
            return 1
        for i in range(1,len(envelopes)):
            if envelopes[i-1] == envelopes[i]:
                envelopes.pop(i-1)
                continue
            if envelopes[i-1][0] >= envelopes[i][0]\
            or envelopes[i-1][1] >= envelopes[i][1]:
                return i if i<=1 else i+1
        return i+1

envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes = [[1,1],[1,1],[1,1]]
envelopes = [[1,1],[1,2]]
envelopes = [[5,4],[6,6],[7,7],[2,3]]
envelopes = [[5,4]]
        
envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1],[1,1]]
print(Solution().maxEnvelopes(envelopes))