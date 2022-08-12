import math 
d,H,W = map(int,input().split())
Hsq = H*H
Wsq = W*W
h,w=0,0
"""
h = H/W*w
  = H/W*sqrt(dsq-hsq)
hsq = Hsq/Wsq*(dsq-hsq)
hsq = Hsq/Wsq*(Wsq/(Wsq+Hsq))*dsq
hsq = Hsq*(Wsq+Hsq)*dsq
h = sqrt(Hsq*(Wsq+Hsq)*dsq)
"""
h = math.sqrt(Hsq/(Wsq+Hsq)*d*d)
h = math.floor(h)
w = math.sqrt(Wsq/(Wsq+Hsq)*d*d)
w = math.floor(w)
print(h,w)