from sys import exit

class Shape:
	def __init__(self,name):
		self.name=name

class Triangle(Shape):
	def __init__(self,name,a,b,c):
		Shape.__init__(self,name)
		self.a=int(a)
		self.b=int(b)
		self.c=int(c)

	def query(self):
		print("This is triangle")
		print("Sides is %d %d %d"%(self.a,self.b,self.c))

	def circle(self):
		print("circle is %d"%(self.a+self.b+self.c))

class Square(Shape):
	def __init__(self,name,side):
		Shape.__init__(self,name)
		self.side=int(side)

	def query(self):
		print("This is square")
		print("Sides is %d"%self.side)

	def circle(self):
		print("circle is %d"%self.side)

class Rectangle(Shape):
	def __init__(self,name,width,height):
		Shape.__init__(self,name)
		self.width=int(width)
		self.height=int(height)

	def query(self):
		print("This is rectangle")
		print("Sides is %d %d"%(self.width,self.height))

	def circle(self):
		print("circle is %d"%(self.width+self.height))

def help():
	print("triangle name a b c")
	print("square name side")
	print("rectangle name width height")
	print("query name")
	print("count")
	print("circle name")
	print("quit")

shapes=[]
t=0
s=0
r=0

def count():
	print("triangles",t)
	print("squre",s)
	print("rectangle",r)

while(1):
	command=input('> ')
	args=command.split()

	if(args[0]=='help'):
		help()
	if(args[0]=='triangle'):
		triangle=Triangle(args[1],args[2],args[3],args[4])
		shapes.append(triangle)
		t=t+1
	if(args[0]=='square'):
		square=Square(args[1],args[2])
		shapes.append(square)
		s=s+1
	if(args[0]=='rectangle'):
		rectangle=Rectangle(args[1],args[2],args[3])
		shapes.append(rectangle)
		r=r+1
	if(args[0]=='query'):
		for i in range(len(shapes)):
			if(args[1]==shapes[i].name):
				shapes[i].query()
	if(args[0]=='circle'):
		for i in range(len(shapes)):
			if(args[1]==shapes[i].name):
				shapes[i].circle()
	if(args[0]=='count'):
		count()
	if(args[0]=='quit'):
		exit()