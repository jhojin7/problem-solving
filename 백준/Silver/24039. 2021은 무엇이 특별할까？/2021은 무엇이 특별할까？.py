primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,103]
special = []
for i in range(len(primes)-1):
    special.append(primes[i]*primes[i+1])
# print(special)
N=int(input())
for x in special:
    if x>N:
        print(x)
        exit()