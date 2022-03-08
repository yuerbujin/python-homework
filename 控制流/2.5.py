x=[1,2,3,4,50,6,7,8,9]
t=x[1]#初始化

for i in range(8):
	if(t<x[i+1]):
		t=x[i+1]#找出最大的值

print(t)#输出最大的值