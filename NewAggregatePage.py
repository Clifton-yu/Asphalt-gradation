import tkinter as tk
from BasePage import BasePage
from create_entry_fields import create_entry_fields
import pandas as pd
from tkinter import filedialog


class NewAggregatePage(BasePage):
    def __init__(self, parent, controller, before_page, next_page, show_frame):
        super().__init__(parent, controller, before_page, next_page, show_frame)
        self.material = "新骨料"
        self.indices = []
        self.weights1 = []
        self.label_list = self.label_list1

        def on_submit():
            show_frame(self.next_page)

        def back():
            show_frame(self.before_page)

        create_entry_fields(self)
        self.create_submit_button(on_submit)
        self.create_back_button(back)
        self.create_excel_button(self.read_excel)
        tk.Label(self, text="矿料、水泥掺量(%)").grid(row=0, column=0)
        weight1 = [tk.DoubleVar(value=5) for _ in range(2)]
        for i, val in enumerate(weight1):
            tk.Entry(self, textvariable=val).grid(row=0, column=len(self.label_list1) - 1 + i)
        self.weights1.append(weight1)

    def create_back_button(self, back):
        back_button = tk.Button(self, text="上一页", command=back)
        back_button.grid(row=len(self.size) + 3, column=2, pady=20)

    def create_submit_button(self, on_submit):
        submit_button = tk.Button(self, text="提交", command=on_submit)
        submit_button.grid(row=len(self.size) + 3, column=4, pady=20)

    def create_excel_button(self, command):
        excel_btn = tk.Button(self, text="从excel导入", command=command)
        excel_btn.grid(row=len(self.size) + 3, column=3)

    def read_excel(self):
        filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if filepath:
            print(f"Selected file: {filepath}")
            df = pd.read_excel(filepath, index_col=0, header=0)
            for i, size in enumerate(self.size):
                for _, ind in enumerate(df.index):
                    if str(size) in str(ind):
                        for j, label in enumerate(self.label_list1):
                            for _, col in enumerate(df.columns):
                                if str(label) in str(col):
                                    value = round(df.loc[ind, col], 2)
                                    if not pd.isna(value):
                                        self.indices[i][j].set(value)
