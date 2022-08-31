h=int(input())
M=int(input())
def A(t): 
    return (-6)*t**4 + h*t**3 + 2*t**2 + t

for i in range(1,M+1):
    if A(i)<=0:
        print(f"The balloon first touches ground at hour: {i}")
        exit()
print("The balloon does not touch ground in the given time.")