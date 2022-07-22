n = int(input()); print("Gnomes:")
for _ in range(n):
    a, b, c = map(int, input().split())
    if ([a, b, c] == sorted((a, b, c))
        or [a, b, c] == sorted((c, b, a),reverse=True)): print("Ordered")
    else: print("Unordered")