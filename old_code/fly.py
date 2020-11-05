import tkinter as tk

class fly:
	def __init__(self,x,y):#,root):
		self._oil=10
		self._x=x
		self._y=y
		#frame=tk.Frame(root)
		#frame.pack()
		#self.bt1=tk.Button(frame,text='move',fg='blue',command=self.move)
		#self.bt1.pack()
		kk='在'+repr((self._x,self._y))+'处生成了架飞机！'
		#tl=tk.Label(root,text=kk)
		print(kk)
		
	def move(self,x1=0,y1=0):
		if (x1==0) and (y1==0):
		    lock=0
		    print('飞机未发生移动！')
		else:
		    lock=1
		    self._oil-=1
		if self.oil()<0:
		    oil_test='油量不够，无法操作！'
		    return oil_test

		self._x+=x1
		self._y+=y1
		if y1>=0:
		    dy='前'
		else:
		    dy='后'
		if x1>=0:
		    dx='右'
		else:
		    dx='左'
		if lock==1:
		    print('\n飞机向'+dy+'移动了%3d格'%abs(y1),'飞机向'+dx+'移动了%3d格'%abs(x1))
	def __str__(self):
		a='飞机此时所在位置为'+str((self._x,self._y))+'！'
		return a
	__repr__ = __str__
	def oil(self):
	    print('剩余油量为：|'+'▇'*self._oil+'|',end='   ')
	    return self._oil
	def addoil (self):
	    self._oil=10
	    add_oil_test='|▇▇▇▇▇▇▇▇▇▇|'
	    return add_oil_test

class fighter(fly):
	def __init__(self,x,y):
	    super().__init__(x,y)
	    print('这架飞机属于战斗机！')

class civil(fly):
	def __init__(self,x,y):
	    super().__init__(x,y)
	    print('这架飞机属于民用飞机！')

