class Person:#定义一个Person类
	def __init__(self,name,age):#初始化name和age两个属性
		self.a=name#初始化name
		self.b=age#初始化age

	def greet(self):#输出函数
		print("Hello, my name is %s, I'm %d years old"%(self.a,self.b))#格式化输出

tom=Person('tom',10)#实例化Person
tom.greet()#调用greet函数打印Tom

jerry = Person('jerry', 12)#实例化Person
jerry.greet()#调用greet函数打印jerry