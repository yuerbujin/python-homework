x=[[1,2,3],[4,5,6],[7,8,9]]#初始化二维矩阵

for a in range(0,3):#外层循环每次输出一行
	for b in range(0,3):
		print("%d "%x[b][a],end='')#输出b行a列的元素
		b=b+1
	a=a+1
	print()#换行