s = input().strip()
crelic = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for cr in crelic:
    s = s.replace(cr,".")
print(len(s))