from tkinter import *
from tkinter.messagebox import showinfo


window = Tk()
window.title("输入框在此")
window.geometry("450x350")

label_1 = Label(window, text="请输入数字N，表示您想生成N个数：")
label_1.pack()
point_num = StringVar()
point_num.set("")
Entry(window, textvariable=point_num).pack()

label_2 = Label(window, text="请输入数字K,代表聚类数:")
label_2.pack()
cluster_num = StringVar()
cluster_num.set("")
Entry(window, textvariable=cluster_num).pack()


def func1():
    n_points = Entry(window, textvariable=point_num).get()
    n_cluster = Entry(window, textvariable=cluster_num).get()
    string = str("点的数量：%s  聚类数: %s " % (n_points, n_cluster))
    showinfo(title="输入信息如下:", message=string)
    global n
    global k
    n = n_points
    k = n_cluster
    # return n_points, n_cluster


b = Button(window, text="Yes", width=20, height=2, command=func1).pack()

window.mainloop()
