import tkinter as tk

窗口 = tk.Tk()
窗口.title('图形应用程序')
窗口.geometry('500x300+600+300')

def 登录():
    登录窗口 = tk.Toplevel(窗口)
    登录窗口.title('请登录...')
    登录窗口.geometry('200x200+750+350')

登录按钮 = tk.Button(text='登录', command=登录)
登录按钮.place(relx=0.5, rely=0.5)

窗口.mainloop()