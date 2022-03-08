x=[1,9,2,8,3,7,4,6,5]#初始化列表

#冒泡排序
for a in range(8):#外层循环每次把最大值放在最后
	for b in range(a+1,9):#内层循环找出每次最大值
		if x[a]>x[b]:
			t=x[a]
			x[a]=x[b]
			x[b]=t     #交换
		else:
			continue
		b=b+1
	a=a+1

print(x)#输出排序后列表