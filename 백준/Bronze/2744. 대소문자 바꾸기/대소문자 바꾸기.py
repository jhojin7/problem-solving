s = input()
import string
for c in s:
    if c in string.ascii_lowercase:
        print(c.upper(),end='')
    else:
        print(c.lower(),end='')