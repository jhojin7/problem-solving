for i in range(int(input())):
    n = int(input())
    if n <= 25:
        print(f"Case #{i+1}: World Finals")
    elif n <= 1000:
        print(f"Case #{i+1}: Round 3")
    elif n <= 4500:
        print(f"Case #{i+1}: Round 2")
    else:
        print(f"Case #{i+1}: Round 1")
