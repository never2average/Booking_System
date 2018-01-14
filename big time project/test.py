from tkinter import *
myaccount_designer=[('priyesh')]
account_page=Tk()
myusername_label=Label(account_page,text='Username:')
myusername_label.grid(row=1,column=1,sticky='E')
myusername_data_label=Label(account_page,text=myaccount_designer[0][0])
myusername_data_label.grid(row=1,column=2)
account_page.mainloop()
