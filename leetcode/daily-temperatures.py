# temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
# temperatures = [30,60,90]
# temperatures = [1,2,3,5,6]
# temperatures = [5,4,3,2,1,2,3,4,5]
temperatures = [1,2,3,4,5,4,3,2,4,5,6,7,8,9]

# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         print(temperatures)
        
"""
def dailyTemperatures(temperatures):
    days = []
    print(temperatures)
    for i in range(len(temperatures)):
        temp = temperatures[i]
        # for j in range(i,len(temperatures)):
        #     if temp < temperatures[j]:
        #         break
        
        cnt = 0
        for j in range(i+1,len(temperatures)):
            if temp < temperatures[j]:
                cnt +=1
            else: 
                continue
        # while temperatures and temp < temperatures[j]:
        #     cnt+=1
        #     j+=1
        days.append(cnt)
         
    print(days)
    return days
"""
        
"""
def dailyTemperatures(temperatures):
    days = []
    for temp in temperatures:
        today = temperatures.index(temp)
        diff = 0
        for future in temperatures[today:]:
            if today > future:
                continue
        days.append(temperatures.index(future) - temperatures.index(today))
    print(days)
    return days
"""


"""
def dailyTemperatures(temps):
    counts = []
    print(temps)
    for i in range(len(temps)):
        cnt = 0
        j = i+1
        for j in range(i,len(temps)):
            if temps[i] < temps[j]:
                break
            cnt += 1
            # if j is last value and still no higher temp, then no count
            if j == len(temps)-1:
                cnt = 0
        counts.append(cnt)
    print(counts)
    return counts
"""
def dailyTemperatures(temperatures):
    answer = [0]*len(temperatures)
    stack = []
    for i,temp in enumerate(temperatures):
        print(i,temp)
        while stack and temp > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    print(answer)
    return answer
        

            
dailyTemperatures(temperatures)
