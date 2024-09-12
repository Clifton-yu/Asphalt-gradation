import tkinter as tk
from BasePage import BasePage
from tkinter import filedialog
import pandas as pd

class RequirementsPage(BasePage):
    def __init__(self, parent, controller, before_page,next_page,show_frame):
        super().__init__(parent, controller, before_page, next_page, show_frame)
        self.bounds = []
        self.label_list =['级配上限', '级配下限']

        def on_submit():
            show_frame(self.next_page)

        def back():
            show_frame(self.before_page)

        # Create a frame to center align the components
        center_frame = tk.Frame(self)
        center_frame.pack(expand=True)

        # Create two column frames for entries
        self.column_frame = tk.Frame(center_frame)
        self.column_frame.grid(row=0, column=0, padx=20)

        for i, var in enumerate(["级配上限（%）", "级配下限（%）"]):
            label = tk.Label(self.column_frame, text=var)
            label.grid(row=0, column=1 if i == 0 else 2, sticky="w")

            bounds = [tk.DoubleVar(value=100 if i == 0 else 0) for _ in range(len(self.size))]
            for j, varc in enumerate(bounds):
                entry_label = tk.Label(self.column_frame, text=str(self.size[j]) + "mm")
                entry_label.grid(row=j + 1, column=0, sticky="e")  # Add size element to the left

                entry = tk.Entry(self.column_frame, textvariable=varc)
                entry.grid(row=j + 1, column=1 if i == 0 else 2, sticky="w")
            self.bounds.append(bounds)

        back_button = tk.Button(self.column_frame, text="上一页", command=back)
        back_button.grid(row=(len(self.size)) + 4, column=0,pady=20)
        submit_btn = tk.Button(self.column_frame, text="提交级配要求", command=on_submit)
        submit_btn.grid(row=(len(self.size)) + 4, column=2)
        self.create_excel_button(self.read_excel)

    def create_excel_button(self, command):
        excel_btn = tk.Button(self.column_frame, text="从excel导入", command=command)
        excel_btn.grid(row=len(self.size) + 4, column=1)

    def read_excel(self):
        filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if filepath:
            print(f"Selected file: {filepath}")
            df = pd.read_excel(filepath, index_col=0, header=0)
            for i, size in enumerate(self.size):
                for _, ind in enumerate(df.index):
                    if str(size) in str(ind):
                        for j, label in enumerate(self.label_list):
                            for _, col in enumerate(df.columns):
                                if str(label) in str(col):
                                    value = round(df.loc[ind, col], 2)
                                    if not pd.isna(value):
                                        self.bounds[j][i].set(value)
# Copyright (c) 2024 余洪福
# Created on: 2024-04-24
# Author: 余洪福
# Contact: 15391558936
# Description: 沥青级配设计