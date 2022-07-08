N = int(input())
people = list(map(int,input().split()))
people.sort()
# print(people)
sum, rolling_sum = 0, 0
for i in range(N):
    sum += rolling_sum + people[i]
    rolling_sum += people[i]
print(sum)