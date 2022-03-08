def mul_matrix(a,b):
	ah=len(a)
	al=len(a[0])
	bh=len(b)
	bl=len(b[0])#计算两个列表的行和列
	
	c=[]
	ch=cl=min(ah,al)#计算c列表的行和列
	
	for h in range(ch):
		row=[]
		for l in range(cl):
			row.append(0)
		c.append(row)		#创建空的c列表
		
	for h in range(ch):
		for l in range(cl):
			for i in range(al):
				c[h][l]=c[h][l]+a[h][i]*b[i][l]#对矩阵a和矩阵b进行相乘
	
	return c#返回结果

def dump_matrix(c):
	for i in range(len(c)):
		print(c[i])#输出列表
	print()

a = [[1,1],
     [1,1]]

b = [[1,2],
     [3,4]]#初始化列表a b

c=mul_matrix(a, b)
dump_matrix(c)#调用函数

x = [[1,2,3],
     [4,5,6]]
y = [[1,4],
     [2,5],
     [3,6]]#初始化列表x y

z=mul_matrix(x, y)
dump_matrix(z)#调用函数