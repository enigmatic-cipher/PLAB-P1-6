"""
Given a list of numbers as input. Print all those numbers from this list that are multiples of 4 and fall in the range of 100 to 200 [inclusive].
Input-> [237,199,200,196,104]
Output-> 
200 196 104
"""

ls = [237,199,200,196,104]
ln = len(ls)
for i in range(0,ln):
  e = ls[i]
  if (e%4==0) and (100<=e<=200):
    print(e)
    