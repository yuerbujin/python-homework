import sys#声明退出程序

class Person:#定义一个Person类
	def __init__(self,name,address,phone):#初始化name、address和phone三个属性
		self.name=name
		self.address=address
		self.phone=phone

class AddressBook:#定义一个AddressBook类
	def __init__(self):
		self.persons=[]#设置其属性为一个persons属性，现在是空列表

	def addPerson(self):#定义创建联系人函数
		print('name:',end='')
		name=input()
		print('address:',end='')
		address=input()
		print('phone:',end='')
		phone=input()
		person=Person(name,address,phone)#实例化Person，由用户输入name、address和phone三个属性
		self.persons.append(person)##将用户是创建的一个人增加到persons列表中

	def delPerson(self):#定义删除联系人函数
		print('name:',end='')
		a=input()#由用户输入删除的联系人
		for i in range(len(self.persons)):
			if(self.persons[i].name==a):#查询该联系人
				del self.persons[i]#删除
				print('%s is deleted from the contact'%a)

	def queryPerson(self):#定义查询联系人函数
		print('name:',end='')
		a=input()
		for i in range(len(self.persons)):
			if(self.persons[i].name==a):#查询该联系人
				print(self.persons[i].name,self.persons[i].address,self.persons[i].phone)

	def listAllPerson(self):#定义列出所有联系人函数
		for i in range(len(self.persons)):
			print(self.persons[i].name,self.persons[i].address,self.persons[i].phone)

	def quit():#定义退出程序函数
		sys.exit()


x=AddressBook()#实例化通讯录


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
		AddressBook.addPerson(x)
	if(a==2):
		AddressBook.delPerson(x)
	if(a==3):
		AddressBook.queryPerson(x)
	if(a==4):
		AddressBook.listAllPerson(x)
	if(a==5):
		quit()#分别调用五个函数
	i=i+1
