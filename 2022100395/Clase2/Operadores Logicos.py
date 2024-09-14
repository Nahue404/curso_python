'''
Operadores logicos
'''

a = 30
b = 40
c = 50
r = ((a<b)and(b<c))
print(r)
r = ((a<b)or(c<a))
print(r)
r = not((a<b)or(c<a))
print(r)