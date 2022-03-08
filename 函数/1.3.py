def sum(start,end):
	sum=0
	while start<=end:
		sum=sum+start# 计算范围[first, last]内的整数的累加和
		start=start+1
	return sum# 返回累加和

print(sum(1,10))#输出累加和
print(sum(1,100))#输出累加和