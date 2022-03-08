i=1
k=1#初始化变量

while i<=5:#外层循环每次输出一行
	k=1
	while k<=i:
		print('%d '%k,end='')#内层循环每次输出一个元素
		k=k+1
	i=i+1
	print()#换行