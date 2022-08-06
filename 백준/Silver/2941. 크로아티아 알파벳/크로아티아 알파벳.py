s = input().strip()
croatian = ["c=","c-","dz=","d-","lj","nj","s=","z="]
for cr in croatian:
    s = s.replace(cr,".")
print(len(s))