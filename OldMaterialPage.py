import tkinter as tk
from tkinter import filedialog
import pandas as pd
from BasePage import BasePage

from create_entry_fields import create_entry_fields


class OldMaterialPage(BasePage):
    def __init__(self, parent, controller, before_page, next_page, show_frame):
        super().__init__(parent, controller, before_page, next_page, show_frame)
        self.material = "旧集料"
        self.indices = []
        self.entry_vars = []
        self.weights0 = []
        self.label_list = self.label_list0

        def on_submit():
            show_frame(self.next_page)

        def back():
            show_frame(self.before_page)

        label = tk.Label(self, text="各组料期望占比（%,可不填）")
        label.grid(row=0, column=0)
        weights0 = [tk.DoubleVar(value=30) for _ in range(len(self.label_list))]
        for j, var in enumerate(weights0):
            entry = tk.Entry(self, textvariable=var)
            entry.grid(row=0, column=j + 1)
        self.weights0.append(weights0)

        create_entry_fields(self)
        self.create_submit_button(on_submit)
        self.create_excel_button(self.read_excel)
        self.create_back_button(back)

    def create_back_button(self, back):
        back_button = tk.Button(self, text="上一页", command=back)
        back_button.grid(row=len(self.size) + 3, column=1, pady=20)

    def create_submit_button(self, command):
        submit_btn = tk.Button(self, text="提交", command=command)
        submit_btn.grid(row=len(self.size) + 3, column=3)

    def create_excel_button(self, command):
        excel_btn = tk.Button(self, text="从excel导入", command=command)
        excel_btn.grid(row=len(self.size) + 3, column=2)

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
                                        self.indices[i][j].set(value)
                    if 'weights' in str(ind):
                        for j, label in enumerate(self.label_list):
                            for _, col in enumerate(df.columns):
                                if str(label) in str(col):
                                    value = round(df.loc[ind, col], 2)
                                    if not pd.isna(value):
                                        self.weights0[0][j].set(value)
# Copyright (c) 2024 余洪福
# Created on: 2024-04-24
# Author: 余洪福
# Contact: 15391558936
# Description: 沥青级配设计