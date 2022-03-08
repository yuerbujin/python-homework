a=1#初始化变量

for a in range(1,5):#外层循环每次输出一行
	b=1
	for b in range(1,a+1):
		print('%dx%d=%d '%(b,a,a*b),end='')#格式化输出每个表达式
		b=b+1
	a=a+1
	print()#换行