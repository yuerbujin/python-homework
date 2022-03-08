import sys#声明退出程序
x=[]#创建通讯录

def create():#定义创建联系人函数
	list={'name':0,'address':0,'phone':0}
	print('name:',end='')
	list['name']=input()
	print('address:',end='')
	list['address']=input()
	print('phone:',end='')
	list['phone']=input()
	x.append(list)

def delete():#定义删除联系人函数
	print('name:',end='')
	a=input()#由用户输入删除的联系人
	for i in range(len(x)):
		if(x[i]['name']==a):#查询该联系人
			del x[i]#删除
			print('%s is deleted from the contact'%a)

def query():#定义查询联系人函数
	print('name:',end='')
	a=input()
	for i in range(len(x)):
		if(x[i]['name']==a):#查询该联系人
			print(x[i]['name'],x[i]['address'],x[i]['phone'])

def list():#定义列出所有联系人函数
	for i in range(len(x)):
		print(x[i]['name'],x[i]['address'],x[i]['phone'])

def quit():#定义退出程序函数
	sys.exit()

i=0
while(1):#程序主循环
	if(i>0):
		print()#每次输入结束后换行
	print('1. create person')
	print('2. delete person')
	print('3. query person')
	print('4. list all persons')
	print('5. quit')
	print('Enter a number(1-5):',end='')

	a=int(input())
	if(a==1):#分别调用五个函数
		create()
	if(a==2):
		delete()
	if(a==3):
		query()
	if(a==4):
		list()
	if(a==5):
		quit()#分别调用五个函数
	i=i+1