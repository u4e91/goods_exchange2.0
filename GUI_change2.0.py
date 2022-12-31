'''
该程序允许添加物品的信息，删除物品的信息，显示物品列表，也允许查找物品的信息

1、物品有公共的信息（物品名称，物品说明，物品所在地址，联系人手机，邮箱）。为了便于管理和查询，物品可以分成不同的类别（例如食品、书籍、工具等），不同类别的物品可能有不同的属性（例如食品有保质期，数量；书籍有作者，出版社等）。
2、互帮互助系统有两种类型的用户：管理员和普通用户。
	管理员可以设置新的物品类型（定义物品类型的名称和各个属性），修改物品类型。
	普通用户在添加物品时先选择物品类型，然后再填入物品信息。普通用户搜寻物品时，需要先选择类型，再输入关键字，关键字可以再用户名称和说明中进行匹配。
	普通用户需要注册（填入基本信息，包括住址，联系方式等），管理员批准后才能成为正式用户。
3、为了便于使用上述功能，软件需要提供GUI。
'''

from atexit import register
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from numpy import place 
import data

Adminname = "1" #管理员登录名
Adminpass = "1" #管理员登录密码

#开始页面
class StartPage:
	data.init()
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个窗口
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('物品交换系统')
		self.window.geometry('300x410+500+100') # 这里的乘是小x，第一个参数表示窗口的长，第二个表示宽，第三个表示的距离屏幕左边界的距离，第三个为距离上边界的距离
 
		label = Label(self.window, text="物品交换系统", font=("Verdana", 20))
		label.pack(pady=100)  # pady=100 这个label距离窗口上边界的距离，这里设置为100刚好居中


 		# command=lambda:  可以带参数，注意带参数的类不要写括号，否者，这里调用会直接执行(class test:)
		Button(self.window, text="用户登录", font=tkFont.Font(size=16), command=lambda: Userlogin(self.window), width=30, height=2,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()	# pack() 方法会使得组件在窗口中自动布局
		Button(self.window, text="管理员登录", font=tkFont.Font(size=16), command=lambda: Adminlogin(self.window), width=30, height=2,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="退出系统", height=2, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		

		

		self.window.mainloop() # 主消息循环


#用户登录
class Userlogin:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('用户登录')
		self.window.geometry('450x300+500+100')

		# 创建提示信息
		tk.Label(self.window, text='用户名: ').place(x=80, y= 50)
		tk.Label(self.window, text='密码: ').place(x=80, y= 90)

		# 输入框
		self.name = tk.Entry(self.window)
		self.name.place(x=160, y=50)
		self.password = tk.Entry(self.window)
		self.password.place(x=160, y=90)


		# 按键
		btn_back = Button(self.window, text="登录", width=8, font=tkFont.Font(size=12), command=self.login)
		btn_back.place(x=200, y=170)
		btn_back = Button(self.window, text="注册", width=8, font=tkFont.Font(size=12), command=self.register)
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=250)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		StartPage(self.window) # 显示主窗口 销毁本窗口


	def login(self):
		name = self.name.get()
		password = self.password.get()
		if name not in data.get_users(): # 在users中搜索用户名
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('150x50')
			tk.Label(window_tip, text='用户不存在').place(x=30, y= 20)
			window_tip.mainloop()
		else:
			# 检验密码正确性
			uinfo = data.get_users()[name]
			pswd = uinfo[0]
			if password != pswd: 
				window_tip = tk.Tk()
				window_tip.geometry('150x50')
				tk.Label(window_tip, text='密码错误').place(x=30, y= 20)
				window_tip.mainloop()
			else:
				UserPage(self.window, name) # 密码正确，进入用户页面

	def register(self):
		Register(self.window)


#用户注册
class Register:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('用户注册')
		self.window.geometry('450x300+500+100')

		# 创建提示信息
		tk.Label(self.window, text='名称: ').place(x=80, y= 50)
		tk.Label(self.window, text='密码: ').place(x=80, y= 90)
		tk.Label(self.window, text='住址: ').place(x=80, y= 130)
		tk.Label(self.window, text='联系方式: ').place(x=80, y= 170)
		

		# 输入框
		self.name = tk.Entry(self.window)
		self.name.place(x=160, y=50)
		self.password = tk.Entry(self.window)
		self.password.place(x=160, y=90)
		self.place = tk.Entry(self.window)
		self.place.place(x=160, y=130)
		self.tel = tk.Entry(self.window)
		self.tel.place(x=160, y=170)


		# 按键
		btn_back = Button(self.window, text="注册", width=8, font=tkFont.Font(size=12), command=self.add)
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=250)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		StartPage(self.window) # 显示主窗口 销毁本窗口

	def add(self):
		name = self.name.get()
		password = self.password.get()
		place = self.place.get()
		tel = self.tel.get()
		if name == "" or password == "":
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('100x50')
			tk.Label(window_tip, text='请勿输入空值').place(x=30, y= 20)
			window_tip.mainloop()
		elif name in data.get_users():
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('100x50')
			tk.Label(window_tip, text='该用户已存在').place(x=30, y= 20)
			window_tip.mainloop()
		else:
			data.add_registers(name, password, place, tel)
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('200x50')
			tk.Label(window_tip, text='已注册等待管理员通过').place(x=30, y= 20)
			window_tip.mainloop()


#管理员登录
class Adminlogin:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('管理员登录')
		self.window.geometry('450x300+500+100')

		# 创建提示信息
		tk.Label(self.window, text='名称: ').place(x=80, y= 50)
		tk.Label(self.window, text='密码: ').place(x=80, y= 90)
		

		# 输入框
		self.name = tk.Entry(self.window)
		self.name.place(x=160, y=50)
		self.password = tk.Entry(self.window)
		self.password.place(x=160, y=90)


		# 按键
		btn_back = Button(self.window, text="登录", width=8, font=tkFont.Font(size=12), command=self.login)
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=250)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		StartPage(self.window) # 显示主窗口 销毁本窗口

	def login(self):
		
		name = self.name.get()
		password = self.password.get()

		if name == Adminname and password == Adminpass:
			AdminPage(self.window)
		else:
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('150x50')
			tk.Label(window_tip, text='用户名或密码错误').place(x=30, y= 20)
			window_tip.mainloop()


#用户界面
class UserPage:
	def __init__(self, parent_window, username):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('物品交换系统')
		self.window.geometry('300x410+500+100')

		label = Label(self.window, text="物品交换系统", font=("Verdana", 20))
		label.pack(pady=100)  # pady=100 这个label距离窗口上边界的距离，这里设置为100刚好居中

		 		# command=lambda:  可以带参数，注意带参数的类不要写括号，否者，这里调用会直接执行(class test:)
		Button(self.window, text="添加物品", font=tkFont.Font(size=16), command=lambda: Add_cla(self.window, 0, username), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()	# pack() 方法会使得组件在窗口中自动布局
		Button(self.window, text="删除物品", font=tkFont.Font(size=16), command=lambda: Del(self.window, 0, username), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="查找物品", font=tkFont.Font(size=16), command=lambda: Find_cla(self.window, 0, username), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="所有物品", font=tkFont.Font(size=16), command=lambda: Show(self.window, 0, username), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="返回首页", font=tkFont.Font(size=16), command=lambda: StartPage(self.window), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

		
		self.window.mainloop()


#管理员界面
class AdminPage:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('物品交换系统')
		self.window.geometry('300x490+500+100')

		label = Label(self.window, text="物品交换系统", font=("Verdana", 20))
		label.pack(pady=100)  # pady=100 这个label距离窗口上边界的距离，这里设置为100刚好居中

		 		# command=lambda:  可以带参数，注意带参数的类不要写括号，否者，这里调用会直接执行(class test:)
		Button(self.window, text="添加物品", font=tkFont.Font(size=16), command=lambda: Add_cla(self.window, 1, Adminname), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()	# pack() 方法会使得组件在窗口中自动布局
		Button(self.window, text="删除物品", font=tkFont.Font(size=16), command=lambda: Del(self.window,1, Adminname), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="查找物品", font=tkFont.Font(size=16), command=lambda: Find_cla(self.window,1, Adminname), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="所有物品及用户", font=tkFont.Font(size=16), command=lambda: Show(self.window,1, Adminname), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="修改类型", font=tkFont.Font(size=16), command=lambda: Change(self.window), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="审批注册", font=tkFont.Font(size=16), command=lambda: Approve(self.window), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="返回首页", font=tkFont.Font(size=16), command=lambda: StartPage(self.window), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()

		
		self.window.mainloop()


#添加(选择物品类型)
class Add_cla:
	def __init__(self, parent_window, ua, uaname):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('添加物品')
		self.window.geometry('450x300+500+100')
		self.ua = ua
		self.uaname = uaname

		types = data.get_types()

		intro = "请从以下类别中选择:"
		# 创建提示信息
		text1 = Label(self.window,bd=4,fg='black',text=intro)
		text1.place(x=160,y=70) #绝对位置，放置文本
		
		# 下拉框
		self.select = ttk.Combobox(self.window,width=12,textvariable=tk.StringVar(),state="readonly")
		lis = []
		for id in types :
			lis.append(id)
		self.select['values'] = lis
		self.select.place(x=160,y=120)
		

		# 按键
		btn_back = Button(self.window, text="继续", width=8, font=tkFont.Font(size=12), command=lambda: self.add())
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=250)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		if self.ua == 0:
			UserPage(self.window, self.uaname)
		if self.ua == 1:
			AdminPage(self.window) # 显示主窗口 销毁本窗口

	def add(self):
		type = self.select.get()
		if type == "":
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('120x50')
			tk.Label(window_tip, text='请选择').place(x=30, y= 20)
			window_tip.mainloop()
		else:
			Add(self.window, self.ua, type, self.uaname)


#添加物品详细信息
class Add:
	def __init__(self, parent_window, ua, type, uaname):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('添加物品')
		self.window.geometry('450x300+500+100')
		self.ua = ua
		self.uaname = uaname
		self.type = type
		otext = data.get_types()[type][0] + ":"

		# 创建提示信息
		tk.Label(self.window, text='ID*: ').place(x=80, y= 10)
		tk.Label(self.window, text='名称*: ').place(x=80, y= 40)
		tk.Label(self.window, text='说明: ').place(x=80, y= 70)
		tk.Label(self.window, text='地址*: ').place(x=80, y= 100)
		tk.Label(self.window, text='手机*: ').place(x=80, y= 130)
		tk.Label(self.window, text='邮箱: ').place(x=80, y= 160)
		tk.Label(self.window, text=otext).place(x=80, y= 190)


		# 输入框
		self.id = tk.Entry(self.window)
		self.id.place(x=160, y=10)
		self.name = tk.Entry(self.window)
		self.name.place(x=160, y=40)
		self.instru = tk.Entry(self.window)
		self.instru.place(x=160, y=70)
		self.place = tk.Entry(self.window)
		self.place.place(x=160, y=100)
		self.tel = tk.Entry(self.window)
		self.tel.place(x=160, y=130)
		self.email = tk.Entry(self.window)
		self.email.place(x=160, y=160)
		self.other = tk.Entry(self.window)
		self.other.place(x=160, y=210)

		# 按键
		btn_back = Button(self.window, text="添加物品", width=8, font=tkFont.Font(size=12), command=lambda: self.add())
		btn_back.place(x=200, y=230)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=260)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		if self.ua == 0:
			UserPage(self.window, self.uaname)
		if self.ua == 1:
			AdminPage(self.window) # 显示主窗口 销毁本窗口

	def add(self):
		id = self.id.get()
		name = self.name.get()
		instru = self.instru.get()
		place = self.place.get()
		tel = self.tel.get()
		email = self.email.get()
		other = self.other.get()
		if id in data.get_items():
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('120x50')
			tk.Label(window_tip, text='该id已存在').place(x=30, y= 20)
			window_tip.mainloop()
		elif id == "" or name == "" or place == "" or tel == "":
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('120x50')
			tk.Label(window_tip, text='请勿输入空值').place(x=30, y= 20)
			window_tip.mainloop()
		else:
			data.add_items(id, name, self.type, instru, place, tel, email, other, self.uaname)
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('140x50')
			tk.Label(window_tip, text='物品添加成功 ').place(x=30, y= 20)
			window_tip.mainloop()

# 删除
class Del:
	def __init__(self, parent_window, ua, uaname):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('删除物品')
		self.window.geometry('450x300+500+100')
		self.ua = ua
		self.uaname = uaname
		flag = 0

		# 滚条
		roll = tk.Scrollbar(self.window)
		roll.pack(side = tk.RIGHT,fill = tk.Y)
		# 文本
		text_input = tk.Text(self.window,width=120,height=10)
		items = data.get_items()
		self.mylist = []
		if self.uaname == Adminname:
			for i in items:
				flag = 1
				id = i
				name = items[i][0]
				type = items[i][1]
				instru = items[i][2]
				place = items[i][3]
				tel = items[i][4]
				email = items[i][5]
				other_cla = data.get_types()[type][0]
				other = items[i][6]
				text_input.insert('insert',"ID：{}\t名称：{}\t类别：{}\t说明：{}\t地址：{}\t手机：{}\t邮箱：{}\t{}:{}\n".format(id, name,
							type, instru, place, tel, email, other_cla, other))
				self.mylist.append(id)
				if not flag:
					text_input.insert('insert','无物品')
		else:
			for i in items:
				if items[i][7] == self.uaname:
					flag = 1
					id = i
					name = items[i][0]
					type = items[i][1]
					instru = items[i][2]
					place = items[i][3]
					tel = items[i][4]
					email = items[i][5]
					other = items[i][6]
					text_input.insert('insert',"ID：{}\t名称：{}\t类别：{}\t说明：{}\t地址：{}\t手机：{}\t邮箱：{}\t{}\n".format(id, name,
								type, instru, place, tel, email, other))
					self.mylist.append(id)
			if not flag:
				text_input.insert('insert','无物品')
		text_input.pack()
		# 绑定
		text_input.config(yscrollcommand=roll.set) 
		roll.config(command=text_input.yview) 

		# 创建提示信息
		tk.Label(self.window, text='ID: ').place(x=80, y= 160)
		
		self.id = tk.Entry(self.window)
		self.id.place(x=160, y=160)

		

		btn_back = Button(self.window, text="删除物品", width=8, font=tkFont.Font(size=12), command=self.delete)
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=250)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		if self.ua == 0:
			UserPage(self.window, self.uaname)
		if self.ua == 1:
			AdminPage(self.window) # 显示主窗口 销毁本窗口

	def delete(self):
		flag = 0
		id = self.id.get()
		for i in self.mylist:
			if id == i:
				data.remove_item(id)
				flag = 1
		if flag:	
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('100x50')
			tk.Label(window_tip, text='物品删除成功 ').place(x=30, y= 20)
			window_tip.mainloop()
		if not flag:
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('100x50')
			tk.Label(window_tip, text='未找到此物品').place(x=30, y= 20)
			window_tip.mainloop()


#查找(选择物品类型)
class Find_cla:
	def __init__(self, parent_window, ua, uaname):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('查找物品')
		self.window.geometry('450x300+500+100')
		self.ua = ua
		self.uaname = uaname

		# 获取类别
		types = data.get_types()
		intro = "请从以下类别中选择:"
		# 创建提示信息
		text1 = Label(self.window,bd=4,fg='black',text=intro)
		text1.place(x=160,y=70) #绝对位置，放置文本
		
		# 下拉框
		self.select = ttk.Combobox(self.window,width=12,textvariable=tk.StringVar(),state="readonly")
		lis = []
		for id in types :
			lis.append(id)
		self.select['values'] = lis
		self.select.place(x=160,y=120)

		# 按键
		btn_back = Button(self.window, text="继续", width=8, font=tkFont.Font(size=12), command=lambda: self.add())
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=250)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		if self.ua == 0:
			UserPage(self.window, self.uaname)
		if self.ua == 1:
			AdminPage(self.window) # 显示主窗口 销毁本窗口

	def add(self):
		type = self.select.get()
		if type == "":
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('120x50')
			tk.Label(window_tip, text='请选择').place(x=30, y= 20)
			window_tip.mainloop()
		else:
			Find(self.window, self.ua, type, self.uaname)


# 查找
class Find:
	def __init__(self, parent_window, ua, type, uaname):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('查找物品')
		self.window.geometry('800x300+500+100')
		self.ua = ua
		self.uaname = uaname
		self.type = type

		# 创建提示信息
		tk.Label(self.window, text='关键字: ').place(x=280, y= 100)
		
		self.name = tk.Entry(self.window)
		self.name.place(x=330, y=100)
		

		btn_back = Button(self.window, text="查找物品", width=8, font=tkFont.Font(size=12), command=self.find)
		btn_back.place(x=350, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=350, y=270)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		if self.ua == 0:
			UserPage(self.window, self.uaname)
		if self.ua == 1:
			AdminPage(self.window) # 显示主窗口 销毁本窗口

	def find(self):
		flag = 0
		key = self.name.get()
		
		# 滚条
		roll = tk.Scrollbar(self.window)
		roll.pack(side = tk.RIGHT,fill = tk.Y)
		# 文本
		text_input = tk.Text(self.window,width=120,height=20)
		items = data.get_items()
		for i in items:
			if (items[i][0] == key or items[i][2] == key) and items[i][1] == self.type:
				flag = 1
				id = i
				name = items[i][0]
				type = items[i][1]
				instru = items[i][2]
				place = items[i][3]
				tel = items[i][4]
				email = items[i][5]
				other_cla = data.get_types()[type][0]
				other = items[i][6]
				uaname = items[i][7]
				text_input.insert('insert',"ID：{}\t名称：{}\t类别：{}\t说明：{}\t地址：{}\t手机：{}\t邮箱：{}\t{}:{}用户：{}\n".format(id, name,
							type, instru, place, tel, email, other_cla, other, uaname))
		if not flag:
			text_input.insert('insert','未找到此物品')
		text_input.pack()
		# 绑定
		text_input.config(yscrollcommand=roll.set) 
		roll.config(command=text_input.yview) 
							
		self.window.mainloop()


#列出所有物品
class Show:
	def __init__(self, parent_window, ua, uaname):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('所有物品')
		self.window.geometry('800x300+500+100')
		self.ua = ua
		self.uaname = uaname

		# 滚条
		roll = tk.Scrollbar(self.window)
		roll.pack(side = tk.RIGHT,fill = tk.Y)
		# 文本
		text_input = tk.Text(self.window,width=120,height=20)
		items = data.get_items()
		text_input.insert('insert',"所有物品：\n")
		for i in items:
			id = i
			name = items[i][0]
			type = items[i][1]
			instru = items[i][2]
			place = items[i][3]
			tel = items[i][4]
			email = items[i][5]
			other_cla = data.get_types()[type][0]
			other = items[i][6]
			uaname = items[i][7]
			text_input.insert('insert',"ID：{}\t名称：{}\t类别：{}\t说明：{}\t地址：{}\t手机：{}\t邮箱：{}\t{}:{}\t用户：{}\n".format(id, name,
						type, instru, place, tel, email, other_cla, other, uaname))
		if self.uaname == Adminname:
			username = data.get_users()
			text_input.insert('insert',"\n所有用户：\n")
			for i in username:
				name = i
				password = username[i][0]
				palce = username[i][1]
				tel = username[i][2]
				text_input.insert('insert',"用户名称：{}\t密码：{}\t地址：{}\t联系方式：{}\n".format(name, password, place, tel))
		text_input.pack()
		# 绑定
		text_input.config(yscrollcommand=roll.set) 
		roll.config(command=text_input.yview) 
					
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=350, y=270)
		
		self.window.mainloop()

	# 返回
	def back(self):
		if self.ua == 0:
			UserPage(self.window, self.uaname)
		if self.ua == 1:
			AdminPage(self.window) # 显示主窗口 销毁本窗口


#修改物品类型
class Change:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('修改物品类型')
		self.window.geometry('450x300+500+100')

		# 创建提示信息
		tk.Label(self.window, text='类型名: ').place(x=80, y= 50)
		tk.Label(self.window, text='属性: ').place(x=80, y= 90)


		# 输入框
		self.name = tk.Entry(self.window)
		self.name.place(x=160, y=50)
		self.cla = tk.Entry(self.window)
		self.cla.place(x=160, y=90)


		# 按键
		btn_back = Button(self.window, text="添加/修改", width=8, font=tkFont.Font(size=12), command=self.add)
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=250)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		AdminPage(self.window) # 显示主窗口 销毁本窗口

	def add(self):
		name = self.name.get()
		cla = self.cla.get()
		if name in data.get_types():
			data.change_types(name, cla)
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('120x50')
			tk.Label(window_tip, text='类别修改成功').place(x=30, y= 20)
			window_tip.mainloop()			
		else:
			# 弹窗显示
			data.change_types(name, cla)
			window_tip = tk.Tk()
			window_tip.geometry('120x50')
			tk.Label(window_tip, text='类别添加成功').place(x=30, y= 20)
			window_tip.mainloop()
			

#审批注册用户		
class Approve:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('审批注册用户')
		self.window.geometry('450x300+500+100')

		# 滚条
		roll = tk.Scrollbar(self.window)
		roll.pack(side = tk.RIGHT,fill = tk.Y)
		# 文本
		text_input = tk.Text(self.window,width=120,height=10)
		text_input.place(x=0, y=0)
		registers = data.get_registers()
		self.mylist = []
		for i in registers:
			name = i
			password = registers[i][0]
			place = registers[i][1]
			tel = registers[i][2]
			text_input.insert('insert',"用户名：{}\t密码：{}\t住址：{}\t联系方式：{}\n".format(name, password, place, tel))
		text_input.pack()
		# 绑定
		text_input.config(yscrollcommand=roll.set) 
		roll.config(command=text_input.yview) 

		# 创建提示信息
		tk.Label(self.window, text='用户名: ').place(x=80, y= 150)

		# 输入框
		self.name = tk.Entry(self.window)
		self.name.place(x=160, y=150)


		# 按键
		btn_back = Button(self.window, text="通过", width=8, font=tkFont.Font(size=12), command=self.approve)
		btn_back.place(x=150, y=180)
		btn_back = Button(self.window, text="拒绝", width=8, font=tkFont.Font(size=12), command=self.reject)
		btn_back.place(x=250, y=180)
		btn_back = Button(self.window, text="一键通过", width=8, font=tkFont.Font(size=12), command=self.a_all)
		btn_back.place(x=200, y=220)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=260)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		AdminPage(self.window) # 显示主窗口 销毁本窗口

	# 通过
	def approve(self):
		name = self.name.get()
		if name not in data.get_registers(): # 在users中搜索用户名
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('150x50')
			tk.Label(window_tip, text='用户不存在').place(x=30, y= 20)
			window_tip.mainloop()
		else:
			# 添加用户
			password = data.get_registers()[name][0]
			place = data.get_registers()[name][1]
			tel = data.get_registers()[name][2]
			data.add_users(name, password, place, tel)
			data.remove_registers(name)
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('150x50')
			tk.Label(window_tip, text='已通过该用户申请').place(x=30, y= 20)
			window_tip.mainloop()

	# 拒绝
	def reject(self):
		name = self.name.get()
		if name not in data.get_registers(): # 在users中搜索用户名
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('150x50')
			tk.Label(window_tip, text='用户不存在').place(x=30, y= 20)
			window_tip.mainloop()
		else:
			data.remove_registers(name)
			window_tip = tk.Tk()
			window_tip.geometry('150x50')
			tk.Label(window_tip, text='已拒绝该用户申请').place(x=30, y= 20)
			window_tip.mainloop()
	
	# 一键通过
	def a_all(self):
		register = data.get_registers()
		for name in list(register):
			password = register[name][0]
			place = register[name][1]
			tel = register[name][2]
			data.add_users(name, password, place, tel)
			data.remove_registers(name)
		window_tip = tk.Tk()
		window_tip.geometry('150x50')
		tk.Label(window_tip, text='已一键通过').place(x=30, y= 20)
		window_tip.mainloop()


if __name__ == '__main__':
	# 实例化Application
	window = tk.Tk()
	StartPage(window)