import re

p = re.compile('S(.{2,6}?)N')
s = 'ASDFANSAAAAAFGNDASMPRKYNSAAN'
s1 = p.findall(s)

if s1:
    print (sorted(s1, key=len)[0])
    print (min(s1, key=len)) # as suggested by Nick Presta
input_text = str
input_text.split(sep = "\n")