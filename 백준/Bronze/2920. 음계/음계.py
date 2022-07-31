arr = list(map(int,input().split()))
if sorted(arr)==arr:print("ascending")
elif sorted(arr,reverse=True)==arr:print("descending")
else:print("mixed")