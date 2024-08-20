def binomial_coefficient(n, k):
    if k > n:
        return 0
    result = 1
    for i in range(k):
        result *= (n - i) / (i + 1)
    return result

def binomial_probability(n, k, p):
    return binomial_coefficient(n, k) * (p ** k) * ((1 - p) ** (n - k))

for _ in range(int(input())):
    R,S,X,Y,W = map(int,input().split())
    p = (S-R+1)/S
    p_atleast_X = 0
    for k in range(X,Y+1):
        p_atleast_X += binomial_probability(Y,k,p)
    if p_atleast_X * W > 1:
        print("yes")
    else:
        print("no")