import sqlite3
import time
import pandas as pd
import sys
import pyfiglet
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt

dbase = sqlite3.connect('estacionamento.db')
c = dbase.cursor()
# conectando...
# this is a function to get the user input from the text input box
#def getInputBoxValue():
	#userInput = console.get()
	#return userInput


# this is the function called when the button is clicked


# this is the function called when the button is clicked
def btndate():
	# this is a function to get the user input from the text input box
	def getInputBoxValue():
		userInput = dataF.get()
		return userInput

	# this is a function to get the user input from the text input box
	def getInputBoxValue():
		userInput = tInput.get()
		return userInput

	# this is the function called when the button is clicked


	root = Tk()

	# This is the section of code which creates the main window
	root.geometry('162x131')
	root.configure(background='#F0F8FF')
	root.title('DATA')

	# This is the section of code which creates a text input box
	dataF = Entry(root)
	dataF.place(x=17, y=24)
	dataF.insert(0, '2020-10-10')

	# This is the section of code which creates a text input box
	tInput = Entry(root)
	tInput.place(x=17, y=62)
	tInput.insert(0, '2021-10-10')

	def btnClickFunction():
		data1 = dataF.get()
		data2 = tInput.get()
		print("\n" * 2)
		# df = pd.read_sql_query( "SELECT * FROM estacionamento WHERE criado_em BETWEEN 2020/10/1 AND 2020/10/30", dbase)
		sql = """SELECT * FROM estacionamento WHERE criado_em BETWEEN ? AND ?"""
		df1 = pd.read_sql_query(sql, dbase, params=[data1, data2])
		text.delete('1.0', END)
		text.insert(INSERT, df1)
		dbase.commit()

	# This is the section of code which creates a button
	Button(root, text='Buscar', bg='#F0F8FF', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=44, y=89)

	root.mainloop()


#fUNCIONARIOS
def btnfunc():
	root = Tk()
	root.geometry('224x92')
	root.configure(background='#F0F8FF')
	root.title('Func')

	tInputFunc = Entry(root)
	tInputFunc.place(x=39, y=20)
	tInputFunc.insert(0, 'PGG,PGA,PGT')

	def btnClickFunction():
		func = tInputFunc.get()
		sql2 = """SELECT * FROM estacionamento WHERE funcr = ?"""
		df4 = pd.read_sql_query(sql2, dbase, params=[func])
		text.delete('1.0', END)
		text.insert(INSERT, df4)
		dbase.commit()

	Button(root, text='Buscar', bg='#575757', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=67, y=51)

	root.mainloop()


# this is the function called when the button is clicked
def btnobs():
	root = Tk()
	root.geometry('224x92')
	root.configure(background='#F0F8FF')
	root.title('Func')

	tInputObs = Entry(root)
	tInputObs.place(x=39, y=20)
	tInputObs.insert(0, 'HB20')

	def btnClickFunction():
		obsinpt = tInputObs.get()
		sql3 = """SELECT * FROM estacionamento WHERE obs = ?"""
		df6 = pd.read_sql_query(sql3, dbase, params=[obsinpt])
		text.delete('1.0', END)
		text.insert(INSERT, df6)
		dbase.commit()

	Button(root, text='Buscar', bg='#575757', font=('arial', 12, 'normal'), command=btnClickFunction).place(x=67, y=51)

	root.mainloop()



root = Tk()

# This is the section of code which creates the main window
root.geometry('837x450')
root.configure(background='#F0F8FF')
root.title('Visualizar Registros')


# This is the section of code which creates a text input box
#console=Entry(root)
#console.place(x=147, y=16)
#df1 = StringVar()
#Entry(root, textvariable=df1).grid(row=20, column=5)
#df1 = ScrolledText(root, height=25, width=100).grid(row=1, column=1)
text = Text(root)
#text.pack(expand=YES, fill=BOTH)
ScrollBar = Scrollbar(root)
ScrollBar.config(command=text.yview)
text.config(yscrollcommand=ScrollBar.set)
ScrollBar.pack(side=RIGHT, fill=Y)
text.pack(expand=YES, fill=BOTH)
sql = """SELECT id, criado_em, prod, obs, formapag, valor, funcr FROM estacionamento"""
df2 = pd.read_sql_query(sql, dbase)
def btnviewall():
	text.delete('1.0', END)
	text.insert(INSERT, df2)
	dbase.commit()
def btstats():
	...
	#ts = Series(randn(1000), index=date_range('1/1/2000', periods=1000))


# This is the section of code which creates a button
Button(root, text='Visualizar Todos', bg='#474747', font=('arial', 12, 'normal'), command=btnviewall).place(x=4, y=400)


# This is the section of code which creates a button
Button(root, text='Visualizar por Data', bg='#474747', font=('arial', 12, 'normal'), command=btndate).place(x=140, y=400)


# This is the section of code which creates a button
Button(root, text='Visualizar por Func', bg='#474747', font=('arial', 12, 'normal'), command=btnfunc).place(x=290, y=400)


# This is the section of code which creates a button
Button(root, text='Visualizar por OBS', bg='#474747', font=('arial', 12, 'normal'), command=btnobs).place(x=440, y=400)

Button(root, text='Status', bg='#474747', font=('arial', 12, 'normal'), command=btstats).place(x=590, y=400)


root.mainloop()
