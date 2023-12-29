import mcrcon
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
import os
import pickle
import sys
import socket
import webbrowser
host = None  # ip
port = None  # 端口
password = None
s = tk.Tk
def 许可条款(event=None):
    webbrowser.open('https://github.com/lvzhiyuan0925/lvzhiyuan0925-/blob/main/MIT%E8%AE%B8%E5%8F%AF%E8%AF%81.md')
def 整体():
    global c_4,s,ccc_1
    i = 1
    v = False

    # 创建 RCON 连接
    rcon = mcrcon.MCRcon(host, password, port)
    try:
        if ccc_1.get():
            # 连接到服务器
            rcon.connect()
        else:
            if tk.messagebox.askokcancel('警告','阅读MIT许可证\n确定及我已阅读并同意MIT许可证（请返回“连接rcon”窗口查看）\n取消及我不同意MIT许可证'):
                rcon.connect()
            else:
                tk.messagebox.showinfo('再见','程序已退出')
    except (ConnectionRefusedError,socket.gaierror,mcrcon.MCRconException) as error_1:
        tk.messagebox.showinfo('错误',f'无法连接服务器：{error_1}')
        with open('数据.pkl','rb+') as file:
            file.seek(0)
            file.truncate()
        sys.exit()
    except Exception as error_2:
        tk.messagebox.showinfo('错误', f'不常见未知错误：{error_2}')
        with open('数据.pkl', 'rb+') as file:
            file.seek(0)
            file.truncate()
        sys.exit()


    s = tk.Tk()

    def 后台进程():
        global c_4,s,v
        text = c_1.get("1.0", "end-1c")
        text_2 = c_3.get()
        text___ = text.split('\n')
        if str(text_2) == '*':
            while v == True:
                time_1 = time.time()
                time_2 = time.ctime(time_1)
                for text____ in text___:
                    if text____.isdigit():
                        try:
                            c_4.insert(0, f'[{time_2}]   等待{int(text____)}秒')
                            time.sleep(int(text____))
                        except RuntimeError:
                            sys.exit()
                    elif text____.startswith('if @a == '):
                        q = text____[len("if @a == "): -1]

                        response = rcon.command(f'execute')
                        if str(response) == '':
                            text________ = text____[4:]
                            c_4.insert(0, f'[{time_2}]   已发送：{text________}')
                        else:
                            c_4.insert(0,f'[{time_2}]   {response}')
                    else:
                        # 执行 RCON 命令
                        response = rcon.command(f'{text____}')
                        if str(response) == '':
                            text________ = text____[4:]
                            try:
                                c_4.insert(0, f'[{time_2}]   已发送：{text________}')
                            except RuntimeError:
                                sys.exit()
                        else:
                            try:
                                c_4.insert(0, f'[{time_2}]   {response}')
                            except RuntimeError:
                                sys.exit()

        elif str(text_2) == '':
            tk.messagebox.showinfo('警告','输入次数')
        else:
            for _ in range(int(text_2)):
                for text____ in text___:
                    time_1 = time.time()
                    time_2 = time.ctime(time_1)
                    if text____.isdigit():

                        c_4.insert(0, f'[{time_2}]   等待{int(text____)}秒')
                        time.sleep(int(text____))
                    else:
                        # 执行 RCON 命令
                        response = rcon.command(f'{text____}')
                        if str(response) == '':
                            try:
                                text________ = text____[4:]
                                c_4.insert(0, f'[{time_2}]   已发送：{text________}')
                            except RuntimeError:
                                sys.exit()
                        else:
                            try:
                                c_4.insert(0, f'[{time_2}]   {response}')
                            except RuntimeError:
                                sys.exit()








    def button_command():
        global v
        关注点赞 = threading.Thread(target=后台进程)
        v = True

        关注点赞.start()
    def quiet():
        global s
        if tk.messagebox.askokcancel('警告','确定退出？（不保存）'):
            s.destroy()
        else:
            pass






    c_1 = tk.Text(s,width=60,height=15)
    c_2 = ttk.Label(s,text='次数')
    c_3 = ttk.Entry(s)
    c_4 = tk.Listbox(s,width=800,height=4)
    button = ttk.Button(s,text='运行',command=button_command)


    c_4.pack()
    c_1.pack()
    c_2.pack()
    c_3.pack()
    button.pack()

    s.geometry('800x350')
    s.title('minecraft命令编辑器')
    s.protocol("WM_DELETE_WINDOW", quiet)
    s.mainloop()





def 退出():
    global s_2,cc_1,cc_4,cc_6,host,port,password
    cc_1_ = cc_1.get()
    cc_4_ = cc_4.get()
    cc_6_ = cc_6.get()
    try:

        with open('数据.pkl', 'rb+') as file:
            if cc_1_ == '':
                list_1 = pickle.load(file)
                host = str(list_1[0])
                port = int(list_1[1])
                password = str(list_1[2])
                s_2.destroy()
                整体()
            else:
                file.seek(0)
                file.truncate()
                host = str(cc_1_)  # ip
                port = int(cc_4_)  # 端口
                password = str(cc_6_)
                pickle.dump((cc_1_, cc_4_, cc_6_), file)
                s_2.destroy()
                整体()







    except (FileNotFoundError, EOFError):
        with open('数据.pkl', 'wb') as file:
            host = str(cc_1_)  # ip
            port = int(cc_4_)  # 端口
            password = str(cc_6_)
            pickle.dump((cc_1_,cc_4_,cc_6_), file)
            s_2.destroy()
            整体()

s_2 = tk.Tk()
ccc_1 = tk.BooleanVar()
button_2 = ttk.Button(s_2, text='连接（rcon）',command=退出)
cc_2 = tk.Label(s_2,text='服务器ip/地址')
cc_3 = tk.Label(s_2,text='rcon端口(不是服务器)')
cc_4 = tk.Entry(s_2)
cc_1 = tk.Entry(s_2)
cc_5 = tk.Label(s_2,text='rcon密码')
cc_6 = tk.Entry(s_2)
cc_7 = tk.Label(s_2,fg='blue',text='           MIT许可证',cursor="hand2")
cc_9 = tk.Checkbutton(s_2,text='我已阅读并同意',variable=ccc_1)
c_4 = tk.Listbox()


s_2.title('连接rcon')
cc_7.bind('<Button-1>',许可条款)
cc_2.pack()
cc_1.pack()#ip
cc_3.pack()
cc_4.pack()#端口
cc_5.pack()
cc_6.pack()#密码


button_2.pack()
cc_7.pack()
cc_9.place(x=50,y=157)


s_2.geometry('350x185')
s_2.mainloop()
