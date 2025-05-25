'''Книга 1

a = int(input())
c = 0

for i in range(a+1):
	if i <10:
		c = c+1
	if i>=10:
		if i <= 100:
			c = c +2
	print(i)
print(c)
'''
a = int(input())
c = 0

for i in range(a+1):
	c = c + len(str(i))
print(c)
