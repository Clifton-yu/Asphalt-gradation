from tkinter import filedialog
import pandas as pd


def open_file_dialog(size, label_list):
    filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if filepath:
        print(f"Selected file: {filepath}")
        df = pd.read_excel(filepath,index_col=0,header=0)
        # , usecols=[i for i in range(len(label_list))], nrows=len(size))
        return df































# import tkinter as tk
# from tkinter import filedialog
# from openpyxl import load_workbook
#
# def select_excel_file():
#     root = tk.Tk()
#     root.withdraw()  # 隐藏主窗口
#     file_path = filedialog.askopenfilename(title='选择Excel文件', filetypes=[('Excel files', '*.xlsx')])
#     if file_path:
#         print(f'选定的文件: {file_path}')
#         return file_path
#     else:
#         print('没有选择文件')
#         return None
#
# def read_selected_area(file_path):
#     # 这里假设用户已经选定了一个矩形区域，例如'A1:C3'
#     selected_area = 'A1:C3'  # 需要替换为实际选定的区域
#     wb = load_workbook(filename=file_path, data_only=True)
#     sheet = wb.active
#     data_matrix = []
#     for row in sheet[selected_area]:
#         data_row = [cell.value for cell in row]
#         data_matrix.append(data_row)
#     return data_matrix
#
# def main():
#     excel_file = select_excel_file()
#     if excel_file:
#         selected_data = read_selected_area(excel_file)
#         print('选定区域的数据:')
#         for row in selected_data:
#             print(row)
#
# if __name__ == '__main__':
#     main()



# import xlwings as xw
#
# # 打开 Excel 文件
# wb = xw.Book('./test.xlsx')
#
# selected_range = xw.apps.active.selection
# selected_values = selected_range.value
#
# for row in selected_values:
#     print(row)



# import xlwings as xws  # 操作excel库
# import tkinter as tk  # Gui库
# import random   # 随机数
#
# def create():
#     # 获取编辑框的数据
#     if len(ebox_min.get()) == 0:
#         temperature_min = 36.0
#     else:
#         temperature_min = float(ebox_min.get())
#     if len(ebox_max.get()) == 0:
#         temperature_max = 37.0
#     else:
#         temperature_max = float(ebox_max.get())
#     if len(ebox_month.get()) == 0:
#         month = "8月"
#     else:
#         month = str(ebox_month.get()) + "月"
#     if len(ebox_start_day.get()) == 0:
#         day_min = 1
#     else:
#         day_min = int(ebox_start_day.get())
#     if len(ebox_stop_day.get()) == 0:
#         day_max = 31
#     else:
#         day_max = int(ebox_stop_day.get())
#     if len(ebox_save.get()) == 0:
#         file_name = "demo.xlsx"
#     else:
#         file_name = str(ebox_save.get())
#
#     app = xws.App(visible=True, add_book=False)
#     wb = app.books.add()
#     sht = wb.sheets["sheet1"]
#     sht.range("a1").value = ["日期", "早", "中", "晚"]
#     lst = []
#     for it in range(day_min, day_max):
#         temp = month + str(it) + "日"
#         lst.append(temp)
#     sht.range("a2").options(transpose=True).value = lst
#
#     lst.clear()
#     for it in range(day_min, day_max):
#         temp = random.uniform(temperature_min, temperature_max)
#         lst.append(round(temp, 1))
#     sht.range("b2").options(transpose=True).value = lst
#
#     lst.clear()
#     for it in range(day_min, day_max):
#         temp = random.uniform(temperature_min, temperature_max)
#         lst.append(round(temp, 1))
#     sht.range("c2").options(transpose=True).value = lst
#
#     lst.clear()
#     for it in range(day_min, day_max):
#         temp = random.uniform(temperature_min, temperature_max)
#         lst.append(round(temp, 1))
#     sht.range("d2").options(transpose=True).value = lst
#
#     wb.save(file_name + ".xlsx")
#     wb.close()
#     app.quit()
#
#
# if __name__ == "__main__":
#     # 主窗口名称
#     root = tk.Tk()
#     # 标题
#     root.title('随机体温表生成工具')
#     # 关于窗口的设置：窗口居中显示、大小不可调整
#     root.resizable(0, 0)  # 阻止Python GUI的大小调整
#     width, height = [400, 230]
#     scr_width, scr_height = root.maxsize()
#     align_str = '%dx%d+%d+%d' % (width, height,
#                                  (scr_width-width)/2, (scr_height-height)/2)
#     root.geometry(align_str)
#
#     # 按钮的放置
#     bt_start = tk.Button(text="生成", command=create, bd=3)
#     bt_start.place(x=310, y=65, width=80, height=100)
#
#     # 显示lable的放置
#     month_label = tk.Label(root, text="月份", width=10, height=2)
#     month_label.place(x=-5, y=20)
#     day_label = tk.Label(root, text="日期", width=10, height=2)
#     day_label.place(x=-5, y=70)
#     file_label = tk.Label(root, text="名字", width=10, height=2)
#     file_label.place(x=-5, y=120)
#     _label_1 = tk.Label(root, text="<-->", width=10, height=2)
#     _label_1.place(x=150, y=70)
#     minmax_label = tk.Label(root, text="温度", width=10, height=2)
#     minmax_label.place(x=-5, y=170)
#     _label_2 = tk.Label(root, text="<-->", width=10, height=2)
#     _label_2.place(x=150, y=170)
#
#     # 月份按钮编辑框
#     ebox_month = tk.StringVar()
#     month_entry = tk.Entry(root, textvariable=ebox_month, bd=2, justify="center",
#                            highlightcolor='red', highlightthickness=1)
#     month_entry.place(x=80, y=20, width=220, height=40)
#
#     # 日期按钮开始编辑框
#     ebox_start_day = tk.StringVar()
#     start_day_entry = tk.Entry(
#         root, textvariable=ebox_start_day, bd=2, justify="center", highlightcolor='red', highlightthickness=1)
#     start_day_entry.place(x=80, y=70, width=80, height=40)
#
#     # 日期按钮结束编辑框
#     ebox_stop_day = tk.StringVar()
#     stop_day_entry = tk.Entry(
#         root, textvariable=ebox_stop_day, bd=2, justify="center", highlightcolor='red', highlightthickness=1)
#     stop_day_entry.place(x=220, y=70, width=80, height=40)
#
#     # 保存名字编辑框
#     ebox_save = tk.StringVar()
#     save_entry = tk.Entry(root, textvariable=ebox_save, bd=2,
#                           justify="center", highlightcolor='red', highlightthickness=1)
#     save_entry.place(x=80, y=120, width=220, height=40)
#
#     # 温度最小数值编辑框
#     ebox_min = tk.StringVar()
#     min_entry = tk.Entry(
#         root, textvariable=ebox_min, bd=2, justify="center", highlightcolor='red', highlightthickness=1)
#     min_entry.place(x=80, y=170, width=80, height=40)
#
#     # 温度最大编辑框
#     ebox_max = tk.StringVar()
#     max_entry = tk.Entry(
#         root, textvariable=ebox_max, bd=2, justify="center", highlightcolor='red', highlightthickness=1)
#     max_entry.place(x=220, y=170, width=80, height=40)
#
#     # 默认参数
#     ebox_max.set("37.1")
#     ebox_min.set("36.0")
#     ebox_month.set("8")
#     ebox_save.set("体温表")
#     ebox_start_day.set("1")
#     ebox_stop_day.set("31")
#
#     # 窗体循环
#     root.mainloop()
#
