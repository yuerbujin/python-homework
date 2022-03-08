list0 = [1,3,2,4]
list1 = [11,33,22]#初始化list0 list1

def sort(a):
	r=len(a)
	#以下为冒泡排序
	for k in range(1,r):
		for i in range(r-k):
			if a[i]>a[i+1]:
				t=a[i]
				a[i]=a[i+1]
				a[i+1]=t

def dump(a):
	print(a)#输出列表

sort(list0)#调用函数sort
dump(list0)#调用函数dump

sort(list1)#调用函数sort
dump(list1)#调用函数dump