"""
...
"""
from __solver import *

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data_0 = format(data[0],"08b")
        # bytes_cnt = data_0.find('0')
        if data_0[0] == "0": bytes_cnt = 1
        if data_0[:3] == "110": bytes_cnt = 2
        if data_0[:4] == "1110": bytes_cnt = 3
        if data_0[:5] == "11110": bytes_cnt = 4
        print(bytes_cnt, data_0)

        # if length=3 and not 1110
        if len(data) != bytes_cnt:
            return False
        # pop first byte.
        data.pop(0)
        # check all other bytes for "10xxx..."
        for i in range(bytes_cnt-1):
            byte_bin = format(data[i],"0b")
            print(byte_bin)
            if byte_bin[:2] != "10":
                return False
        return True

data = [197,130,1]
# data = [235,140,4,1,1,111]
# data = [235,140,4]
# data = [10]
# data = [230,136,145]

print(Solution().validUtf8(data))