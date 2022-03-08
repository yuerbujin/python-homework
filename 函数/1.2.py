def max(a,b):
	if a>b:
		return a
	else:
		return b#上一题的max

def max3(a,b,c):
	b=max(b,c)#取b和c中max
	if a>b:
		return a
	else:
		return b#分别a和b中max

a=int(input())
b=int(input())
c=int(input())#输入a b c

print(max3(a,b,c))#输出max