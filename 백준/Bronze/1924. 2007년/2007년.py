x,y=map(int,input().split())
dates = 0
if x>1: dates+=31
if x>2: dates+=28
if x>3: dates+=31
if x>4: dates+=30
if x>5: dates+=31
if x>6: dates+=30
if x>7: dates+=31
if x>8: dates+=31
if x>9: dates+=30
if x>10: dates+=31
if x>11: dates+=30
# if x>12: dates+=0
dates+=y
days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
print(days[(dates-1)%7])